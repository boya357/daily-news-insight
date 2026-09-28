import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

# 读取已生成的文件
filepath = 'docs/s_level_catalyst/20260928_盘后_S级催化扫描_电子利润增1.1倍+PCB急跌.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 在风险提示前插入隔夜外盘模块
overnight_section = '''
<div class="section-block">
    <h3 class="section-title" style="color: #e2e8f0; font-size: 18px; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center;">
        <span style="margin-right: 8px;">🌍</span>隔夜外盘扫描
    </h3>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-bottom: 14px;">
        <div style="background: linear-gradient(135deg, rgba(168,85,247,0.12), rgba(139,92,246,0.06)); border-radius: 14px; padding: 18px; border: 1px solid rgba(192,132,252,0.25);">
            <div style="font-size: 13px; color: #a78bfa; font-weight: 600; margin-bottom: 10px;">📈 费城半导体指数</div>
            <div style="font-size: 26px; font-weight: 700; color: #fff; margin-bottom: 4px;">12,668.93 <span style="font-size: 14px; color: #4ade80;">+1.41%</span></div>
            <div style="font-size: 11px; color: #94a3b8;">9月25日收盘 · 周线四连涨 · 本周+6.27%</div>
            <div style="font-size: 11px; color: #64748b; margin-top: 6px;">创5月以来最长周线连涨纪录</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(236,72,153,0.12), rgba(219,39,119,0.06)); border-radius: 14px; padding: 18px; border: 1px solid rgba(244,114,182,0.25);">
            <div style="font-size: 13px; color: #f472b6; font-weight: 600; margin-bottom: 10px;">💾 存储芯片表现</div>
            <div style="font-size: 18px; font-weight: 700; color: #fff; margin-bottom: 6px;">SK海力士 +2.78%</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">西部数据 +1.44% · 闪迪 +1.38%<br>催化：Solidigm拟2027年赴美IPO</div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 13px; font-weight: 600; color: #e2e8f0; margin-bottom: 10px;">📰 核心要点</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.9;">
            • <b style="color: #f1f5f9;">费半指数周线四连涨</b>：本周累计涨6.27%，创5月以来最长连涨，AI算力需求提供支撑<br>
            • <b style="color: #f1f5f9;">高通领涨+3.97%</b>：AI终端+汽车电子双轮驱动，移动端芯片需求回暖<br>
            • <b style="color: #f1f5f9;">存储芯片普涨</b>：SK海力士旗下Solidigm拟赴美IPO，估值预期带动板块情绪<br>
            • <b style="color: #f1f5f9;">中美贸易休战延长</b>：双方同意将贸易休战延长至2027年1月10日，关税风险降低但高端芯片管制未松<br>
            • <b style="color: #f1f5f9;">Meta Muse引爆AI Agent</b>：CPU需求预期升温，AMD、Intel等受益<br>
            • <b style="color: #f1f5f9;">今晚关注</b>：9月28日美股周一开盘后半导体板块能否延续涨势
        </div>
    </div>
</div>
'''

# 在风险提示前插入
insert_marker = '<div class="section-block">\n    <h3 class="section-title"'
idx = content.find('风险提示')
if idx > 0:
    # 找到风险提示的section开头
    section_start = content.rfind('<div class="section-block">', 0, idx)
    if section_start > 0:
        content = content[:section_start] + overnight_section + content[section_start:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ 隔夜外盘模块已插入")
    else:
        print("❌ 未找到插入位置")
else:
    print("❌ 未找到风险提示")

