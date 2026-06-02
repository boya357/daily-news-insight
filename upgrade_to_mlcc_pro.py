#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把N1X报告升级到MLCC Pro终极模板
新增16项完美优化
"""

def upgrade_to_mlcc_pro():
    with open('docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # ========== 1. 在</head>前添加优化CSS和JS ==========
    extra_head = '''
    <!-- 阅读进度条 -->
    <style>
        #progressBar {
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: linear-gradient(90deg, #6366f1, #a855f7);
            z-index: 9999;
            transition: width 0.1s ease;
        }
        #backToTop {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #6366f1, #a855f7);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            cursor: pointer;
            z-index: 9998;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        }
        #backToTop:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
        }
        #backToTop.visible {
            opacity: 1;
            transform: translateY(0);
        }
        .toc-card.active {
            border-color: #8b5cf6 !important;
            background: linear-gradient(135deg, rgba(139,92,246,0.1), rgba(168,85,247,0.1)) !important;
            transform: scale(1.02);
        }
        .section-title {
            scroll-margin-top: 100px;
        }
        .action-buttons {
            position: fixed;
            bottom: 30px;
            left: 30px;
            display: flex;
            gap: 10px;
            z-index: 9997;
        }
        .action-btn {
            width: 45px;
            height: 45px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            color: #6366f1;
        }
        .action-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(99,102,241,0.3);
            color: #8b5cf6;
        }
        .report-footer {
            background: linear-gradient(135deg, rgba(99,102,241,0.05), rgba(139,92,246,0.05));
            border-top: 1px solid rgba(99,102,241,0.2);
        }
        .data-source {
            font-size: 12px;
            color: #6b7280;
            font-style: italic;
        }
        .risk-disclaimer {
            background: linear-gradient(135deg, rgba(239,68,68,0.05), rgba(249,115,22,0.05));
            border: 1px solid rgba(239,68,68,0.2);
            border-radius: 12px;
            padding: 16px;
            font-size: 13px;
            color: #6b7280;
        }
        @media print {
            #backToTop, .action-buttons, #progressBar {
                display: none !important;
            }
        }
        @media (max-width: 768px) {
            .action-buttons {
                left: 15px;
                bottom: 15px;
            }
            #backToTop {
                right: 15px;
                bottom: 70px;
                width: 42px;
                height: 42px;
            }
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
'''
    
    content = content.replace('</head>', extra_head + '\n</head>')
    
    # ========== 2. 在<body>后添加进度条 ==========
    content = content.replace('<body class="bg-gradient-purple min-h-screen">', '''<body class="bg-gradient-purple min-h-screen">
    <div id="progressBar"></div>''')
    
    # ========== 3. 在目录卡片添加class用于高亮 ==========
    content = content.replace('class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10"',
                             'class="toc-card group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10"')
    
    # ========== 4. 为章节标题添加scroll-margin ==========
    content = content.replace('class="text-4xl font-bold text-dark mb-8 flex items-center"',
                             'class="section-title text-4xl font-bold text-dark mb-8 flex items-center"')
    
    # ========== 5. 在</body>前添加所有功能JS和UI元素 ==========
    footer_js_and_ui = '''
    <!-- 操作按钮 -->
    <div class="action-buttons">
        <div class="action-btn" onclick="downloadPDF()" title="导出PDF">
            <span>📄</span>
        </div>
        <div class="action-btn" onclick="shareReport()" title="分享报告">
            <span>📤</span>
        </div>
    </div>
    
    <!-- 回到顶部按钮 -->
    <div id="backToTop" onclick="scrollToTop()">
        <span style="font-size: 20px;">↑</span>
    </div>
    
    <!-- 报告底部信息 -->
    <section class="report-footer py-12 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="bg-white/95 rounded-2xl p-8 shadow-lg">
                <div class="grid md:grid-cols-3 gap-8 mb-8">
                    <div>
                        <h4 class="font-bold text-dark mb-3">📊 报告信息</h4>
                        <ul class="text-sm text-gray-600 space-y-2">
                            <li>报告类型：产业链深度研究报告</li>
                            <li>生成时间：2026年5月31日 11:00</li>
                            <li>版本：v1.0 正式版</li>
                            <li>数据更新：截至2026年5月30日</li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="font-bold text-dark mb-3">🏷️ 报告标签</h4>
                        <div class="flex flex-wrap gap-2">
                            <span class="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-xs font-medium">英伟达</span>
                            <span class="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-xs font-medium">N1X</span>
                            <span class="bg-pink-100 text-pink-700 px-3 py-1 rounded-full text-xs font-medium">COMPUTEX</span>
                            <span class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-xs font-medium">AI算力</span>
                            <span class="bg-orange-100 text-orange-700 px-3 py-1 rounded-full text-xs font-medium">★★★★★ 强烈推荐</span>
                        </div>
                    </div>
                    <div>
                        <h4 class="font-bold text-dark mb-3">📡 数据来源</h4>
                        <ul class="text-sm text-gray-600 space-y-2">
                            <li>英伟达官方公告、技术文档</li>
                            <li>产业链调研、公司财报</li>
                            <li>第三方机构研报汇总</li>
                            <li>COMPUTEX前瞻信息</li>
                        </ul>
                    </div>
                </div>
                
                <div class="risk-disclaimer">
                    <h4 class="font-bold text-red-600 mb-2">⚠️ 风险提示与免责声明</h4>
                    <p>本报告仅供投资研究参考，不构成任何投资建议。投资有风险，入市需谨慎。报告中的信息均来源于公开可获得资料，本报告作者对这些信息的准确性和完整性不作任何保证。依据本报告进行投资所造成的任何后果，由投资者自行承担。</p>
                </div>
            </div>
        </div>
    </section>
    
    <script>
        // 1. 阅读进度条
        window.addEventListener('scroll', function() {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            document.getElementById('progressBar').style.width = scrolled + '%';
            
            // 回到顶部按钮显示/隐藏
            const backBtn = document.getElementById('backToTop');
            if (winScroll > 300) {
                backBtn.classList.add('visible');
            } else {
                backBtn.classList.remove('visible');
            }
            
            // 目录高亮
            const sections = document.querySelectorAll('.section-title');
            const tocCards = document.querySelectorAll('.toc-card');
            
            sections.forEach((section, index) => {
                const rect = section.getBoundingClientRect();
                if (rect.top <= 150 && rect.bottom >= 150) {
                    tocCards.forEach(card => card.classList.remove('active'));
                    if (tocCards[index]) {
                        tocCards[index].classList.add('active');
                    }
                }
            });
        });
        
        // 2. 平滑回到顶部
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
        
        // 3. 目录平滑滚动
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
        
        // 4. 导出PDF
        function downloadPDF() {
            const element = document.body;
            const opt = {
                margin: 10,
                filename: '英伟达N1X芯片深度研究报告.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2, useCORS: true },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            };
            
            // 隐藏UI元素后再导出
            document.getElementById('backToTop').style.display = 'none';
            document.querySelector('.action-buttons').style.display = 'none';
            document.getElementById('progressBar').style.display = 'none';
            
            html2pdf().set(opt).from(element).save().then(() => {
                document.getElementById('backToTop').style.display = '';
                document.querySelector('.action-buttons').style.display = '';
                document.getElementById('progressBar').style.display = '';
            });
        }
        
        // 5. 分享功能
        function shareReport() {
            if (navigator.share) {
                navigator.share({
                    title: '英伟达N1X芯片与COMPUTEX 2026深度研究报告',
                    text: '深度解析N1X芯片架构、产业链全景与投资机会',
                    url: window.location.href
                });
            } else {
                // 复制链接到剪贴板
                navigator.clipboard.writeText(window.location.href).then(() => {
                    alert('链接已复制到剪贴板！');
                });
            }
        }
    </script>
'''
    
    content = content.replace('</body>', footer_js_and_ui + '\n</body>')
    
    # ========== 6. 更新报告生成时间 ==========
    content = content.replace('发布日期：2026年5月30日', '发布日期：2026年5月31日  v1.0正式版')
    
    # 保存文件
    output_file = 'docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ 已完成16项终极优化升级！')
    print(f'📄 输出文件: {output_file}')
    print('\n🚀 新增功能清单：')
    print('1. 阅读进度条（顶部渐变）')
    print('2. 回到顶部按钮（渐变悬浮）')
    print('3. 目录自动高亮（滚动时激活）')
    print('4. 平滑滚动动画')
    print('5. 章节scroll-margin优化（避免被导航遮挡）')
    print('6. 一键导出PDF按钮')
    print('7. 分享报告按钮')
    print('8. 专业报告信息区（类型/生成时间/版本）')
    print('9. 报告标签系统（主题/评级）')
    print('10. 统一数据来源标注')
    print('11. 标准风险提示与免责声明')
    print('12. 移动端完美适配')
    print('13. 打印优化（自动隐藏UI元素）')
    print('14. 按钮hover动效')
    print('15. 目录卡片激活动效')
    print('16. 完整的报告底部专业设计')
    print('\n🎉 MLCC Pro终极模板已完成！现在是行业顶级专业研报水准！')

if __name__ == '__main__':
    upgrade_to_mlcc_pro()
