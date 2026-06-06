# 导航栏标准化规范

## 标准导航栏特性
- 玻璃态半透明背景 (glass-nav)
- 左侧 Logo: "📊 投资研究中心"
- 11个导航链接：首页、日报、盘中、盘后、产业链、周复盘、周三前瞻、周末速递、明日催化、S级催化、月报
- 移动端汉堡菜单，点击展开全屏菜单
- 固定在顶部 (fixed top-0)
- 内容最大宽度: max-w-5xl

## 组件文件位置
- `components/navbar.json` - JSON格式组件数据（程序使用）
- `components/navbar.html` - HTML格式组件（参考使用）

## 批量修复工具
```bash
# 检查所有文件导航栏状态
python tools/fix_navbar.py --check

# 修复单个文件
python tools/fix_navbar.py path/to/file.html

# 批量修复所有文件
python tools/fix_navbar.py --all
```

## 新页面生成规范

任何新生成的HTML页面，必须包含以下标准导航栏代码：

### 1. 在 <head> 中引入依赖
```html
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
<style>
    /* 标准导航栏样式 - 从 components/navbar.json 复制 */
</style>
```

### 2. 在 <body> 开头添加导航栏
```html
<nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
    <!-- 导航栏内容 - 从 components/navbar.json 复制 -->
</nav>
```

### 3. 在 </body> 前添加移动端菜单和脚本
```html
<div id="mobileMenu" class="mobile-menu">
    <!-- 移动端菜单内容 -->
</div>
<script>
    function toggleMobileMenu() {
        var menu = document.getElementById('mobileMenu');
        menu.classList.toggle('show');
    }
</script>
```

### 4. 内容区域顶部间距
页面主要内容区域必须添加 `mt-24` 或 `pt-24` 类，避免被固定导航栏遮挡。

## 校验标准
检查页面是否符合标准导航栏规范：
- ✅ 包含 `glass-nav` 类
- ✅ 包含 "投资研究中心" 文字
- ✅ 包含 `max-w-5xl` 宽度
- ✅ 包含11个导航链接
- ✅ 包含 `mobileMenu` 移动端菜单
- ✅ 包含 `toggleMobileMenu` 函数
- ✅ 引入了 Tailwind CSS

## Git提交前检查
建议在提交前运行：
```bash
python tools/fix_navbar.py --check
```
确保所有页面导航栏符合标准。
