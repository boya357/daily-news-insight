#!/bin/bash
# ==========================================
# 一键部署脚本 - 投资研究中心
# ==========================================

set -e

echo "🚀 开始部署投资研究中心..."
echo "=============================="

# 1. 数据更新
echo ""
echo "📊 [1/4] 更新数据..."
python3 scripts/fetch_market_data.py

# 2. 生成Pro页面
echo ""
echo "🔧 [2/4] 生成Pro工具页面..."
python3 scripts/run_workflow.py --pages

# 3. 构建状态
echo ""
echo "📋 [3/4] 更新工作流状态..."
# 这里可以添加更多状态更新

# 4. Git部署
echo ""
echo "🌐 [4/4] 部署到GitHub Pages..."

git add -A

# 检查是否有变更
if git diff --cached --quiet; then
    echo "   ℹ️  没有新内容需要提交"
else
    COMMIT_MSG="deploy: 自动部署 $(date '+%Y-%m-%d %H:%M:%S')"
    git commit -m "$COMMIT_MSG"
    git push
    echo "   ✅ 部署成功！"
fi

echo ""
echo "=============================="
echo "🎉 部署完成！"
echo "📅 时间: $(date)"

