#!/usr/bin/env python3
"""兼容入口：请使用 update_list_pages.py"""
import subprocess, sys
if __name__ == "__main__":
    subprocess.run([sys.executable, str(__import__('pathlib').Path(__file__).parent / "update_list_pages.py")] + sys.argv[1:])
