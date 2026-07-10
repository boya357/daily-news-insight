#!/usr/bin/env python3
"""
_cli_wrapper.py — unified CLI wrapper for stock-data-skill.

Routes operations to the appropriate backend:
- Core operations (quote, kline, search, minute, analyze):
  Go CLI binary via gateway.
- Extended operations (finance, profile, technical, etc.):
  Direct CLI execution in sandbox.

Also forwards list/schema/doctor/version to Go CLI which holds all metadata.
"""

import os
import sys
import stat
import subprocess
import fcntl

INSTALL_DIR = "/tmp/_westock_cli"
LOCK_FILE = "/tmp/_westock_cli.lock"


def get_bin_path():
    return os.path.join(INSTALL_DIR, "node_modules", ".bin", "westock-data-clawhub")


def is_installed():
    p = get_bin_path()
    return os.path.exists(p) and os.access(p, os.X_OK)

GO_OPS = {"quote", "kline", "search", "minute", "analyze"}
REMOVED_OPS = {"fund-flow"}

POSITIONAL_CODE = {
    "kline", "minute", "finance", "profile", "asfund", "hkfund", "usfund",
    "lhb", "blocktrade", "margintrade", "technical", "chip", "shareholder",
    "dividend", "etf", "etf-holdings", "etf-nav", "etf-company",
    "etf-holders", "etf-financial", "exdiv", "reserve", "quote",
}

POSITIONAL_TYPE = {"hot", "search"}

POSITIONAL_MARKET = {"ipo", "suspension"}


def find_cli_binary(wrapper_dir):
    for name in os.listdir(wrapper_dir):
        path = os.path.join(wrapper_dir, name)
        if name.startswith(".") or name.startswith("_") or name.endswith(".py"):
            continue
        if os.path.isfile(path) and os.stat(path).st_mode & stat.S_IXUSR:
            return path
    return None


def parse_call_args(args):
    if not args:
        return None, {}
    op_name = args[0]
    params = {}
    i = 1
    while i < len(args):
        a = args[i]
        if a == "--param" and i + 1 < len(args):
            kv = args[i + 1]
            i += 2
        elif a.startswith("--param="):
            kv = a[len("--param="):]
            i += 1
        else:
            i += 1
            continue
        eq = kv.find("=")
        if eq > 0:
            params[kv[:eq]] = kv[eq + 1:]
    return op_name, params


def build_ext_args(command, params):
    args = [command]
    p = dict(params)

    if command in POSITIONAL_CODE and "code" in p:
        args.append(p.pop("code"))
    elif command in POSITIONAL_TYPE:
        if "type" in p:
            args.append(p.pop("type"))
        elif "keyword" in p:
            args.append(p.pop("keyword"))
    elif command in POSITIONAL_MARKET and "market" in p:
        args.append(p.pop("market"))

    for key, value in p.items():
        if not value:
            continue
        if value == "true":
            args.append(f"--{key}")
        else:
            args.append(f"--{key}")
            args.append(str(value))

    return args


def try_update():
    os.makedirs(INSTALL_DIR, exist_ok=True)
    lock_fd = open(LOCK_FILE, "w")
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except (IOError, OSError):
        lock_fd.close()
        return
    try:
        subprocess.run(
            ["npm", "install", "--prefix", INSTALL_DIR, "westock-data-clawhub@latest"],
            timeout=120,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        pass
    finally:
        fcntl.flock(lock_fd, fcntl.LOCK_UN)
        lock_fd.close()


def run_ext_op(op_name, params):
    cli_args = build_ext_args(op_name, params)
    env = dict(os.environ)
    env["NODE_NO_WARNINGS"] = "1"

    os.makedirs(INSTALL_DIR, exist_ok=True)
    bin_path = get_bin_path()

    if not is_installed():
        # 首次安装或上次安装不完整：必须等待
        lock_fd = open(LOCK_FILE, "w")
        fcntl.flock(lock_fd, fcntl.LOCK_EX)
        try:
            if not is_installed():
                try:
                    subprocess.run(
                        ["npm", "install", "--prefix", INSTALL_DIR, "westock-data-clawhub@latest"],
                        check=True, timeout=120,
                        stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                    )
                except FileNotFoundError:
                    print(f"ERROR: npm not found. Node.js is required for '{op_name}' operation.", file=sys.stderr)
                    print("Install Node.js (v16+) to enable extended operations.", file=sys.stderr)
                    sys.exit(1)
                except subprocess.CalledProcessError as e:
                    msg = (e.stderr or b"").decode("utf-8", errors="replace")
                    print(f"ERROR: failed to install data-cli: {msg}", file=sys.stderr)
                    sys.exit(1)
        finally:
            fcntl.flock(lock_fd, fcntl.LOCK_UN)
            lock_fd.close()
    else:
        try_update()

    # 读锁：并发执行安全，阻止更新期间执行
    lock_fd = open(LOCK_FILE, "w")
    fcntl.flock(lock_fd, fcntl.LOCK_SH)
    try:
        result = subprocess.run([bin_path] + cli_args, env=env, stdout=sys.stdout, stderr=subprocess.PIPE)
    finally:
        fcntl.flock(lock_fd, fcntl.LOCK_UN)
        lock_fd.close()

    if result.returncode != 0 and result.stderr:
        msg = result.stderr.decode("utf-8", errors="replace")
        msg = msg.replace("westock-data-clawhub", "data-cli")
        msg = msg.replace("westock", "upstream")
        sys.stderr.write(msg)
    sys.exit(result.returncode)


def main():
    wrapper_dir = os.path.dirname(os.path.abspath(__file__))
    cli_bin = find_cli_binary(wrapper_dir)

    if len(sys.argv) >= 3 and sys.argv[1] == "call":
        op_name = sys.argv[2]
        if op_name in REMOVED_OPS:
            print(f"unknown operation: {op_name}", file=sys.stderr)
            sys.exit(1)
        if op_name not in GO_OPS:
            _, params = parse_call_args(sys.argv[2:])
            run_ext_op(op_name, params)
            return

    if cli_bin is None:
        print("ERROR: no CLI binary found in", wrapper_dir, file=sys.stderr)
        sys.exit(1)

    result = subprocess.run(
        [cli_bin] + sys.argv[1:],
        env=os.environ,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
