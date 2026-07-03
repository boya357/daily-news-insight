# 投资研究系统深度审计 & 修复报告
**执行时间**: 2026-07-03
**工作目录**: /root/daily-news-insight/
**GitHub Pages**: https://boya357.github.io/daily-news-insight/

## P0 修复
1. ✅ latest.html 全部修复为最新报告副本（daily 106KB/s_level 154KB/aftermarket 113KB/tomorrow 80KB/intraday 94KB 等）
2. ✅ 白卡白字：创建 docs/assets/global-dark.css（15KB 全局CSS变量+!important覆盖），注入到873个HTML文件
3. ✅ 中文目录全部改为 meta refresh 跳转页（20个中文目录），过期HTML共~250份归档
4. ✅ 生成器基类 v3/components/pro.py、v3/generators/pro_base.py、v4_base.py 已修改：
   - get_v4_theme_css() 改为直接返回深色主题（V4白底彻底废弃）
   - 默认 theme='dark'
   - 自动注入 global-dark.css link
   - validate() 加入白卡自动检测

## P1 优化
5. ✅ 新建 update_list_pages.py（v2）统一管理列表页：
   - latest.html = 最新报告的HTML副本（拷贝）
   - index.html = 深色玻璃态归档列表
   - 按文件名日期排序（不再误用mtime）
6. ✅ 首页 index.html 重建（17KB，0处白卡）：深色Hero + 今日报告快速入口 + 10个核心工具卡片 + 归档入口
7. ✅ validate_system.sh：41项自动校验

## P2 清理
8. ✅ docs/根目录测试/v4文件归档（约50个文件移至 _archives/test_v4/ 和 _archives/v4_templates/）
9. ✅ stock_analysis 精简到 11个核心个股（4持仓+7关注），其余98份归档
10. ✅ 中文目录过期HTML共250+份归档到 _archives/cn_legacy/

## 核心铁律（已固化）
- 全站深色玻璃态通过 assets/global-dark.css 统一兜底，新老页面自动生效
- latest.html 必须是最新报告副本，禁止列表脚本覆盖
- 列表页输出到 index.html
- 中文目录仅保留 index.html 跳转页
- 生成器默认 dark 主题，不再产出白卡
