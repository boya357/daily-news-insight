# Git 工作流程规范

## 分支规范

**仓库只允许存在且仅存在一个主分支：
- `main` - 主分支，直接用于GitHub Pages部署

## 禁止操作
❌ 禁止创建 `master` 分支（历史遗留问题已清理）
❌ 禁止创建 `dev`/`develop`/`feature/*` 等开发分支
❌ 禁止不提交就直接推送

## 正确工作流程

所有修改都直接在 `main` 分支上进行：

```bash
# 1. 确保在main分支
git checkout main

# 2. 拉取最新代码
git pull origin main

# 3. 做修改...

# 4. 提交
git add -A
git commit -m "描述修改内容"

# 5. 推送（会自动推送到main分支）
git push
```

## 为什么这样做的好处
1. ✅ 简单直接，避免分支混乱
2. ✅ 推送即部署，实时生效
3. ✅ 不会出现"修了但看不到"的问题
4. ✅ 适合单人项目不需要多分支只会增加复杂度

---
*本仓库已配置 `git config push.default current，推送自动推送到当前分支*
