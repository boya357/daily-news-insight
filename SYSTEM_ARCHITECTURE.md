
---

## 导航栏统一标准（2026年6月3日新增，强制执行

### 标准样式定义

所有页面必须使用统一的玻璃态导航栏，不得使用任何其他样式。

#### 必须严格遵守：
1. **样式类名**：`glass-nav`
2. **CSS样式**：
   ```css
   .glass-nav {
       background: rgba(255, 255, 255, 0.1);
       backdrop-filter: blur(20px);
       -webkit-backdrop-filter: blur(20px);
       border-bottom: 1px solid rgba(255, 255, 255, 0.2);
       z-index: 2147483647 !important;
       isolation: isolate !important;
       pointer-events: auto !important;
   }
   ```
3. **导航栏标题**：`投资研究中心` + 📊图标
4. **导航按钮**：11个按钮完整列表（首页、日报、盘中、盘后、产业链、周复盘、周三前瞻、周末速递、明日催化、S级催化、月报
5. **链接路径**：必须使用绝对路径`/daily-news-insight/`开头
6. **页面背景**：`linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

#### 模板位置
完整模板代码参见：`ERROR_KNOWLEDGE_BASE.md` 错误记录#4

#### 生成新页面的检查清单（必须逐项打勾后才能提交
- [ ] CSS样式与标准完全一致
- [ ] 标题为"投资研究中心" + 📊图标
- [ ] 导航按钮数量为11个（无缺失
- [ ] 所有链接使用绝对路径
- [ ] z-index层级设置正确
- [ ] 页面背景渐变正确
- [ ] 浏览器打开验证与周复盘列表页样式一致

---
