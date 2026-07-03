#!/bin/bash
cd /root/daily-news-insight

echo "=== O. CodeAct脚本目录 ==="
ls codeact/scripts/ 2>/dev/null | head -25
echo ""

echo "=== P. 预判验证现状 ==="
python3 -c "
import json
try:
    d = json.load(open('data/predictions.json'))
    if isinstance(d, list):
        print(f'预判记录数: {len(d)}')
        for i,p in enumerate(d[:3]):
            print(f'  #{i+1}: {list(p.keys()) if isinstance(p,dict) else p}')
    elif isinstance(d, dict):
        print(f'预判键数: {len(d)}')
        for k in list(d.keys())[:5]:
            print(f'  {k}: {str(d[k])[:100]}')
except Exception as e:
    print(f'Error: {e}')
"
echo ""

echo "=== Q. 错误教训库 ==="
if [ -f "基础设定/错误教训库.md" ]; then
    wc -l 基础设定/错误教训库.md
    head -50 基础设定/错误教训库.md
else
    echo "不存在"
    ls 基础设定/ 2>/dev/null
fi
echo ""

echo "=== R. 报告内容密度 ==="
python3 << 'PYEOF'
import re, os
files = [
    'docs/daily/20260703_每日新闻洞察.html',
    'docs/s_level_catalyst/20260703_盘前_S级催化扫描_宇树IPO+非农爆冷+费半超跌反弹.html',
]
for f in files:
    if os.path.exists(f):
        html = open(f).read()
        text = re.sub(r'<script[^>]*>.*?</script>','',html,flags=re.S)
        text = re.sub(r'<style[^>]*>.*?</style>','',text,flags=re.S)
        text = re.sub(r'<[^>]+>','',text)
        text = re.sub(r'\s+',' ',text).strip()
        cn = len(re.findall(r'[\u4e00-\u9fff]', text))
        print(f'{os.path.basename(f)}:')
        print(f'  HTML={len(html):,}bytes, 纯文本={len(text):,}chars, 中文={cn:,}字')
PYEOF
echo ""

echo "=== S. CodeAct脚本工具调用情况 ==="
for f in codeact/scripts/*.py; do
    if [ -f "$f" ]; then
        calls=$(grep -c "search_web\|fetch_web\|MultiServerMCPClient\|tool_manager" "$f" 2>/dev/null)
        echo "  $(basename $f): 工具调用=$calls"
    fi
done
echo ""

echo "=== T. validate覆盖项 ==="
grep -E "^(echo|validate|check_)" validate_system.sh 2>/dev/null | head -30
