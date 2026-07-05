#!/bin/bash
# 投资研究系统验证脚本 v3.0 (2026-07-05)
# 检查：深色主题、latest.html、导航、内容完整性 + V5.0 L2 体验交互
cd "$(dirname "$0")"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

pass=0; fail=0; warn=0

check() {
    local desc="$1"; shift
    if "$@" >/dev/null 2>&1; then
        echo -e "${GREEN}✅ PASS${NC}  $desc"
        ((pass++))
    else
        echo -e "${RED}❌ FAIL${NC}  $desc"
        ((fail++))
    fi
}

check_warn() {
    local desc="$1"; shift
    if "$@" >/dev/null 2>&1; then
        echo -e "${GREEN}✅ PASS${NC}  $desc"
        ((pass++))
    else
        echo -e "${YELLOW}⚠️  WARN${NC}  $desc"
        ((warn++))
    fi
}

echo "============================================================"
echo "🔍 投资研究系统验证 - $(date '+%Y-%m-%d %H:%M')"
echo "============================================================"
echo ""
echo "--- 1. 基础结构 ---"

check "首页 index.html 存在" test -f docs/index.html
check "全局CSS assets/global-dark.css 存在" test -f docs/assets/global-dark.css

echo ""
echo "--- 2. latest.html 规则 ---"

for d in daily s_level_catalyst intraday aftermarket tomorrow_catalyst industry_chain weekly_review weekend_express weekly_outlook monthly; do
    f="docs/$d/latest.html"
    check_warn "$d/latest.html 存在 (>3KB)" bash -c "test -f '$f' && test \$(stat -c%s '$f') -gt 3000"
done

echo ""
echo "--- 3. 核心工具页 ---"
check "工具页 portfolio_dashboard/index.html 存在" test -f docs/portfolio_dashboard/index.html
check "工具页 longhubang/index.html 存在" test -f docs/longhubang/index.html
check "工具页 topic-picker/index.html 存在" test -f docs/topic-picker/index.html
check "工具页 alert-system/index.html 存在" test -f docs/alert-system/index.html
check "工具页 sector_heatmap/index_pro.html 存在" test -f docs/sector_heatmap/index_pro.html
check "工具页 time-machine/index.html 存在" test -f docs/time-machine/index.html
check "工具页 industry_chain_clock/index.html 存在" test -f docs/industry_chain_clock/index.html
check "工具页 stock_analysis/index.html 存在" test -f docs/stock_analysis/index.html
check "工具页 prediction_verification/index.html 存在" test -f docs/prediction_verification/index.html

echo ""
echo "--- 4. 深色主题（关键页面引入global-dark.css）---"
check "docs/index.html 引入 global-dark.css" grep -q "global-dark.css" docs/index.html
check "docs/daily/latest.html 引入 global-dark.css" grep -q "global-dark.css" docs/daily/latest.html
check "docs/s_level_catalyst/latest.html 引入 global-dark.css" grep -q "global-dark.css" docs/s_level_catalyst/latest.html
check "docs/portfolio_dashboard/index.html 引入 global-dark.css" grep -q "global-dark.css" docs/portfolio_dashboard/index.html
check "docs/longhubang/index.html 引入 global-dark.css" grep -q "global-dark.css" docs/longhubang/index.html
check "docs/topic-picker/index.html 引入 global-dark.css" grep -q "global-dark.css" docs/topic-picker/index.html
check "docs/alert-system/index.html 引入 global-dark.css" grep -q "global-dark.css" docs/alert-system/index.html
check "docs/sector_heatmap/index_pro.html 引入 global-dark.css" grep -q "global-dark.css" docs/sector_heatmap/index_pro.html

echo ""
echo "--- 5. 白卡白字检测（报告页自身硬编码 white/#fff）---"
white_count=$(grep -rlE 'background(|-color):[ ]*(white|#fff|#ffffff)' docs --include='*.html' 2>/dev/null | grep -v '.bak' | wc -l)
echo -e "${YELLOW}ℹ️  INFO${NC}  含硬编码白色背景的HTML文件数: $white_count（将被 global-dark.css !important 强制覆盖）"

echo ""
echo "--- 6. 列表页（index.html 不应该是报告副本，latest 不应该是列表）---"
check "daily/index.html 是归档列表页" bash -c "grep -q '归档\|列表\|newest-card\|report-list\|archive\|📰' docs/daily/index.html"
check "s_level_catalyst/index.html 是归档列表页" bash -c "grep -q 'index-list\|archive\|list-page\|列表\|归档' docs/s_level_catalyst/index.html"
check "aftermarket/index.html 是归档列表页" bash -c "grep -q 'index-list\|archive\|list-page\|列表\|归档' docs/aftermarket/index.html"
check "tomorrow_catalyst/index.html 是归档列表页" bash -c "grep -q 'index-list\|archive\|list-page\|列表\|归档' docs/tomorrow_catalyst/index.html"
check "intraday/index.html 是归档列表页" bash -c "grep -q 'index-list\|archive\|list-page\|列表\|归档' docs/intraday/index.html"

echo ""
echo "--- 7. 中文目录跳转页 ---"
for d in 龙虎榜 个股分析 明日催化剂 周末速递 智能选题助手 持仓智能预警仪表盘 s级催化扫描; do
    f="docs/$d/index.html"
    if [ -f "$f" ]; then
        if grep -q 'http-equiv="refresh"\|meta refresh' "$f"; then
            echo -e "${GREEN}✅ PASS${NC}  中文目录 $d/index.html 是跳转页"
            ((pass++))
        else
            echo -e "${YELLOW}⚠️  WARN${NC}  $d/index.html 未检测到跳转"
            ((warn++))
        fi
    fi
done

echo ""
echo "--- 8. V5.0 L2 体验交互功能 ---"
check "V5测试报告含 TL;DR 卡片" bash -c "test -f docs/_v5_test_premarket.html && grep -q 'tldr-card' docs/_v5_test_premarket.html"
check "V5测试报告含 OG meta" bash -c "test -f docs/_v5_test_premarket.html && grep -q 'og:title' docs/_v5_test_premarket.html"
check "V5测试报告含快速锚点" bash -c "test -f docs/_v5_test_premarket.html && grep -q 'quick-anchors' docs/_v5_test_premarket.html"
check "V5测试报告含移动端底部导航" bash -c "test -f docs/_v5_test_premarket.html && grep -q 'mobile-bottom-nav' docs/_v5_test_premarket.html"
check "V5测试报告含持仓金色高亮" bash -c "test -f docs/_v5_test_premarket.html && grep -q 'holding-stock-tag\|holding-card' docs/_v5_test_premarket.html"
check "V5测试报告含 l2-toolbox 脚本" bash -c "test -f docs/_v5_test_premarket.html && grep -q 'l2-toolbox.js' docs/_v5_test_premarket.html"
check "l2-toolbox.js 静态资源存在" test -f docs/assets/l2-toolbox.js
check "global-dark.css 含 .tldr-card 样式" grep -q ".tldr-card" docs/assets/global-dark.css
check "global-dark.css 含移动端响应式" grep -q "@media (max-width: 768px)" docs/assets/global-dark.css
check "global-dark.css 含持仓金色样式" grep -q "holding-stock-tag" docs/assets/global-dark.css
check "pro_base.py 含 set_tldr 方法" grep -q "def set_tldr" v3/generators/pro_base.py
check "pro_base.py 含 stock_tag 方法" grep -q "def stock_tag" v3/generators/pro_base.py
check "pro.py 含 holding_stocks 参数" grep -q "self.holding_stocks" v3/components/pro.py
check "pro.py 含 og:title 渲染" grep -q "og:title" v3/components/pro.py
check "pro.py 含 mobile-bottom-nav" grep -q "mobile-bottom-nav" v3/components/pro.py

echo ""
echo "============================================================"
echo -e "结果: ${GREEN}$pass 通过${NC}, ${RED}$fail 失败${NC}, ${YELLOW}$warn 警告${NC}"
echo "============================================================"
if [ $fail -gt 0 ]; then
    exit 1
fi
exit 0
