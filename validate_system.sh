#!/bin/bash
# 投资研究系统验证脚本 v2.0 (2026-07-03)
# 检查：深色主题、latest.html、导航、内容完整性
# set -e  (arithmetic may return nonzero)
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

for p in portfolio_dashboard/index.html longhubang/index.html topic-picker/index.html \
         alert-system/index.html sector_heatmap/index_pro.html time-machine/index.html \
         industry_chain_clock/index.html stock_analysis/index.html prediction_verification/index.html; do
    check_warn "工具页 $p 存在" test -f "docs/$p"
done

echo ""
echo "--- 4. 深色主题（关键页面引入global-dark.css）---"

for f in docs/index.html docs/daily/latest.html docs/s_level_catalyst/latest.html \
         docs/portfolio_dashboard/index.html docs/longhubang/index.html docs/topic-picker/index.html \
         docs/alert-system/index.html docs/sector_heatmap/index_pro.html; do
    if [ -f "$f" ]; then
        if grep -q "global-dark.css" "$f" 2>/dev/null; then
            echo -e "${GREEN}✅ PASS${NC}  $f 引入 global-dark.css"
            ((pass++))
        else
            echo -e "${RED}❌ FAIL${NC}  $f 未引入 global-dark.css"
            ((fail++))
        fi
    fi
done

echo ""
echo "--- 5. 白卡白字检测（报告页自身硬编码 white/#fff）---"
white_count=$(grep -rl 'background:[[:space:]]*white\|background-color:[[:space:]]*white\|background:[[:space:]]*#fff\b' docs/ --include='*.html' 2>/dev/null | grep -v _archives | grep -v .bak | wc -l)
echo -e "${YELLOW}ℹ️  INFO${NC}  含硬编码白色背景的HTML文件数: $white_count（将被 global-dark.css !important 强制覆盖）"

echo ""
echo "--- 6. 列表页（index.html 不应该是报告副本，latest 不应该是列表）---"
for d in daily s_level_catalyst aftermarket tomorrow_catalyst intraday; do
    f="docs/$d/index.html"
    if [ -f "$f" ]; then
        if grep -q "报告归档\|历史报告\|report-card\|report-grid" "$f"; then
            echo -e "${GREEN}✅ PASS${NC}  $d/index.html 是归档列表页"
            ((pass++))
        else
            echo -e "${YELLOW}⚠️  WARN${NC}  $d/index.html 未检测到列表特征"
            ((warn++))
        fi
    fi
done

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
echo "============================================================"
echo -e "结果: ${GREEN}$pass 通过${NC}, ${RED}$fail 失败${NC}, ${YELLOW}$warn 警告${NC}"
echo "============================================================"
if [ $fail -gt 0 ]; then
    exit 1
fi
exit 0
