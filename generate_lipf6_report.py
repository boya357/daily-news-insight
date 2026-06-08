from v3.generators.deep_dive import DeepDiveGenerator
from components.data import StatCard
import os

# 创建报告生成器
gen = DeepDiveGenerator(
    title='六氟磷酸锂产业链深度研究报告',
    subtitle='供需紧平衡下的周期反转与核心标的全景分析'
)

# 1. 核心观点摘要
gen.add_summary(
    core_view='六氟磷酸锂正处于新一轮周期上行通道，供需紧平衡格局至少持续至2026年三季度。经历2023-2025年行业出清后，中小产能永久性退出，CR3市占率升至78%，龙头议价权显著增强。储能需求爆发成为核心增量，2026年全球需求预计达40-45万吨，同比增长30%以上。价格中枢有望维持在16-19万元/吨，头部企业盈利弹性巨大。',
    bull_points=[
        '供需紧平衡：2026年需求40-45万吨，有效供给仅34-36万吨，缺口6-11万吨',
        '行业格局优化：CR3达78%，龙头控产保价，价格战概率大幅降低',
        '储能需求爆发：储能占比突破40%，成为第一大需求源，增速超50%',
        '供给刚性：扩产周期18-24个月，2026上半年几乎无新增产能',
        '成本支撑：碳酸锂价格高位运行，行业综合成本约7万元/吨'
    ],
    bear_points=[
        '周期品属性：价格波动大，业绩随周期起伏',
        '产能释放风险：2026Q4-2027年新增产能集中落地',
        '技术替代风险：半固态/固态电池减少电解液用量',
        '需求不及预期：若新能源车或储能增速放缓将影响需求',
        '成本波动：碳酸锂价格波动直接影响生产成本'
    ]
)

# 2. 关键数据卡片
stat_cards = [
    StatCard(title='2026年全球需求', value='42万吨', subtitle='+30% YoY', variant='green'),
    StatCard(title='有效供给', value='35万吨', subtitle='紧平衡', variant='red'),
    StatCard(title='供需缺口', value='7万吨', subtitle='缺口扩大', variant='orange'),
    StatCard(title='价格中枢', value='17.5万/吨', subtitle='周期反转', variant='purple'),
    StatCard(title='CR3市占率', value='78%', subtitle='格局优化', variant='blue'),
    StatCard(title='行业库存', value='1周用量', subtitle='历史低位', variant='indigo'),
    StatCard(title='龙头单吨净利', value='6-10万', subtitle='弹性巨大', variant='green'),
    StatCard(title='扩产周期', value='18-24月', subtitle='供给刚性', variant='orange')
]
gen.add_stat_cards(stat_cards, cols=4)

# 3. 行业分析章节 - 供需格局
gen.add_analysis_section(
    title='📊 供需格局：从全面过剩到紧平衡的结构性反转',
    content='''
    <div class="space-y-4">
        <h3 class="text-lg font-semibold text-gray-800">供给端：产能出清后刚性约束凸显</h3>
        <p class="text-gray-600 leading-relaxed">
            经历2023-2025年的行业低谷，六氟磷酸锂行业发生了深刻的供给侧变革。价格从2022年高点的59万元/吨暴跌至2025年7月的4.7万元/吨，
            全行业陷入深度亏损，大量中小产能永久性退出市场。截至2026年一季度，名义产能约50万吨/年，但实际有效产能仅37-40万吨/年，
            其中约10万吨中小产能因设备老化、人员流失、资金链断裂等原因已无法恢复生产。
        </p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-4">
            <div class="bg-blue-50 rounded-xl p-4 border border-blue-200">
                <h4 class="font-semibold text-blue-800 mb-2">供给收缩的三大不可逆因素</h4>
                <ul class="text-sm text-blue-700 space-y-2">
                    <li>• <strong>产能永久性退出</strong>：约10万吨中小产能因亏损退出，重启需3-6个月且成本高达2-3万元/吨</li>
                    <li>• <strong>龙头默契控产</strong>：CR3达78%，形成以需定产、控产保价的默契，供给弹性大幅收敛</li>
                    <li>• <strong>扩产周期漫长</strong>：环评+建设+调试需18-24个月，2026上半年几乎无新增有效产能</li>
                </ul>
            </div>
            <div class="bg-green-50 rounded-xl p-4 border border-green-200">
                <h4 class="font-semibold text-green-800 mb-2">2026年新增产能规划</h4>
                <ul class="text-sm text-green-700 space-y-2">
                    <li>• 天赐材料：3.5万吨液体六氟技改（Q4投产）</li>
                    <li>• 天际股份：1.5万吨新增（Q4投产）</li>
                    <li>• 多氟多：3万吨扩产（2026年底-2027年初）</li>
                    <li>• 永太科技：5万吨改扩建（2027年底）</li>
                </ul>
            </div>
        </div>
        
        <h3 class="text-lg font-semibold text-gray-800 mt-6">需求端：储能主导的结构性爆发</h3>
        <p class="text-gray-600 leading-relaxed">
            六氟磷酸锂的需求结构正在发生历史性变化。2025年之前，动力电池是绝对的需求主力，占比约70%。
            但进入2026年，储能需求呈现爆炸式增长，占比首次突破40%并超越动力成为第一大需求来源。
            2026年5月，国内锂电整体排产达249GWh，创月度历史新高，其中储能电芯排产占比已达42.3%。
        </p>
        
        <div class="bg-amber-50 rounded-xl p-4 border border-amber-200 my-4">
            <h4 class="font-semibold text-amber-800 mb-2">需求增长的三大驱动力</h4>
            <div class="grid grid-cols-3 gap-4">
                <div class="text-center">
                    <div class="text-2xl font-bold text-amber-600">50%+</div>
                    <div class="text-xs text-amber-700">储能需求增速</div>
                </div>
                <div class="text-center">
                    <div class="text-2xl font-bold text-amber-600">25%</div>
                    <div class="text-xs text-amber-700">动力电池增速</div>
                </div>
                <div class="text-center">
                    <div class="text-2xl font-bold text-amber-600">15%</div>
                    <div class="text-xs text-amber-700">消费电子增速</div>
                </div>
            </div>
        </div>
    </div>
    '''
)

# 4. 价格走势分析
gen.add_analysis_section(
    title='💰 价格走势：周期反转，高位震荡向上',
    content='''
    <div class="space-y-4">
        <p class="text-gray-600 leading-relaxed">
            六氟磷酸锂价格从2025年7月的4.7万元/吨历史低位开始反弹，至2025年底冲高至18万元/吨，半年涨幅超280%。
            2026年初经历理性回调后，于4月底企稳回升，6月价格中枢维持在16-19万元/吨区间。
            供需紧平衡格局下，价格有望维持高位震荡，三季度旺季存在进一步冲高可能。
        </p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-4">
            <div class="bg-gradient-to-br from-green-400 to-emerald-500 rounded-xl p-4 text-white">
                <div class="text-sm opacity-80">2025年7月低点</div>
                <div class="text-2xl font-bold">4.7万/吨</div>
                <div class="text-xs opacity-70">全行业深度亏损</div>
            </div>
            <div class="bg-gradient-to-br from-amber-400 to-orange-500 rounded-xl p-4 text-white">
                <div class="text-sm opacity-80">2025年底高点</div>
                <div class="text-2xl font-bold">18万/吨</div>
                <div class="text-xs opacity-70">半年涨幅280%</div>
            </div>
            <div class="bg-gradient-to-br from-red-400 to-rose-500 rounded-xl p-4 text-white">
                <div class="text-sm opacity-80">2026年中枢预测</div>
                <div class="text-2xl font-bold">16-19万/吨</div>
                <div class="text-xs opacity-70">Q4或冲击20万+</div>
            </div>
        </div>
        
        <h3 class="text-lg font-semibold text-gray-800">分阶段价格预测</h3>
        <div class="overflow-x-auto">
            <table class="w-full text-sm">
                <thead>
                    <tr class="bg-gray-100">
                        <th class="px-4 py-3 text-left rounded-l-lg">时间段</th>
                        <th class="px-4 py-3 text-center">价格区间</th>
                        <th class="px-4 py-3 text-center">核心逻辑</th>
                        <th class="px-4 py-3 text-right rounded-r-lg">供需状态</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3 font-medium">2026Q2</td>
                        <td class="px-4 py-3 text-center text-amber-600">14-17万/吨</td>
                        <td class="px-4 py-3 text-gray-600">需求复苏+库存低位</td>
                        <td class="px-4 py-3 text-right text-green-600">紧平衡</td>
                    </tr>
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3 font-medium">2026Q3</td>
                        <td class="px-4 py-3 text-center text-red-600">17-20万/吨</td>
                        <td class="px-4 py-3 text-gray-600">旺季来临+缺口扩大</td>
                        <td class="px-4 py-3 text-right text-red-600">明显短缺</td>
                    </tr>
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3 font-medium">2026Q4</td>
                        <td class="px-4 py-3 text-center text-amber-600">16-19万/吨</td>
                        <td class="px-4 py-3 text-gray-600">新增产能逐步释放</td>
                        <td class="px-4 py-3 text-right text-amber-600">紧平衡</td>
                    </tr>
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3 font-medium">2027年</td>
                        <td class="px-4 py-3 text-center text-blue-600">10-14万/吨</td>
                        <td class="px-4 py-3 text-gray-600">产能集中释放+需求增速放缓</td>
                        <td class="px-4 py-3 text-right text-blue-600">逐步宽松</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    '''
)

# 5. 技术路线对比
gen.add_tabs_section(
    title='🔬 技术路线：晶体vs液体，各有千秋',
    tabs=[
        ('晶体六氟磷酸锂', '''
        <div class="space-y-3">
            <p class="text-gray-600">
                晶体工艺是传统主流路线，通过氟化锂与五氟化磷反应生成六氟磷酸锂晶体，经过分离、干燥、包装后出厂。
                产品纯度高、稳定性好，便于运输和储存。
            </p>
            <div class="grid grid-cols-2 gap-3">
                <div class="bg-green-50 p-3 rounded-lg">
                    <h4 class="font-semibold text-green-800 text-sm">优势</h4>
                    <ul class="text-xs text-green-700 space-y-1 mt-2">
                        <li>• 纯度高（可达99.99%）</li>
                        <li>• 产品稳定性好</li>
                        <li>• 便于长途运输</li>
                        <li>• 适用于高端客户</li>
                    </ul>
                </div>
                <div class="bg-red-50 p-3 rounded-lg">
                    <h4 class="font-semibold text-red-800 text-sm">劣势</h4>
                    <ul class="text-xs text-red-700 space-y-1 mt-2">
                        <li>• 生产流程长、能耗高</li>
                        <li>• 结晶干燥过程易吸水</li>
                        <li>• 包装运输成本高</li>
                        <li>• 溶解工序增加下游成本</li>
                    </ul>
                </div>
            </div>
            <p class="text-sm text-gray-500 mt-2">
                <strong>代表企业：</strong>多氟多、天际股份、永太科技、新泰材料
            </p>
        </div>
        '''),
        ('液体六氟磷酸锂', '''
        <div class="space-y-3">
            <p class="text-gray-600">
                液体工艺是天赐材料独创的技术路线，在有机溶剂（碳酸二甲酯等）中直接合成六氟磷酸锂溶液，
                省去结晶、干燥、再溶解等工序，大幅降低生产成本。
            </p>
            <div class="grid grid-cols-2 gap-3">
                <div class="bg-green-50 p-3 rounded-lg">
                    <h4 class="font-semibold text-green-800 text-sm">优势</h4>
                    <ul class="text-xs text-green-700 space-y-1 mt-2">
                        <li>• 生产成本低15-20%</li>
                        <li>• 工艺流程短、能耗低</li>
                        <li>• 避免吸水变质风险</li>
                        <li>• 一体化配套效率高</li>
                    </ul>
                </div>
                <div class="bg-red-50 p-3 rounded-lg">
                    <h4 class="font-semibold text-red-800 text-sm">劣势</h4>
                    <ul class="text-xs text-red-700 space-y-1 mt-2">
                        <li>• 纯度相对较低</li>
                        <li>• 不便于长途运输</li>
                        <li>• 需配套电解液产线</li>
                        <li>• 对外销售受限</li>
                    </ul>
                </div>
            </div>
            <p class="text-sm text-gray-500 mt-2">
                <strong>代表企业：</strong>天赐材料（全球最大液体六氟生产商，自给率98%+）
            </p>
        </div>
        '''),
        ('新型锂盐 (LiFSI等)', '''
        <div class="space-y-3">
            <p class="text-gray-600">
                双氟磺酰亚胺锂（LiFSI）作为新型锂盐，具有更高的热稳定性、离子电导率和耐高压性能，
                是800V高压快充和高镍三元电池的重要配套材料。
            </p>
            <div class="grid grid-cols-2 gap-3">
                <div class="bg-green-50 p-3 rounded-lg">
                    <h4 class="font-semibold text-green-800 text-sm">优势</h4>
                    <ul class="text-xs text-green-700 space-y-1 mt-2">
                        <li>• 热稳定性更好</li>
                        <li>• 离子电导率更高</li>
                        <li>• 耐高压性能优异</li>
                        <li>• 适配800V快充</li>
                    </ul>
                </div>
                <div class="bg-red-50 p-3 rounded-lg">
                    <h4 class="font-semibold text-red-800 text-sm">劣势</h4>
                    <ul class="text-xs text-red-700 space-y-1 mt-2">
                        <li>• 价格是六氟的2-3倍</li>
                        <li>• 生产工艺更复杂</li>
                        <li>• 产业链配套尚不成熟</li>
                        <li>• 对铝箔有腐蚀问题</li>
                    </ul>
                </div>
            </div>
            <p class="text-sm text-gray-500 mt-2">
                <strong>发展趋势：</strong>短期内仍是"六氟为主、LiFSI为辅"的混合配方，LiFSI渗透率逐年提升但难以完全替代
            </p>
        </div>
        ''')
    ]
)

# 6. 核心标的分析 - 梯队划分
gen.add_analysis_section(
    title='🏭 核心标的：按弹性与确定性三梯队划分',
    content='''
    <div class="space-y-4">
        <p class="text-gray-600 leading-relaxed">
            结合产能规模、技术实力、成本优势、业绩弹性等多维度因素，我们将A股六氟磷酸锂相关标的分为三个梯队，
            便于投资者根据自身风险偏好选择配置。
        </p>
        
        <div class="space-y-4">
            <!-- 第一梯队 -->
            <div class="bg-gradient-to-r from-amber-50 to-yellow-50 border border-amber-200 rounded-xl p-4">
                <h3 class="text-lg font-bold text-amber-800 flex items-center">
                    <span class="w-6 h-6 bg-amber-500 text-white rounded-full flex items-center justify-center text-sm mr-2">1</span>
                    第一梯队：行业龙头，确定性最强
                </h3>
                <p class="text-sm text-amber-700 mt-2">产能规模大、成本优势显著、客户结构优质、业绩弹性确定性高</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3">
                    <div class="bg-white rounded-lg p-4 shadow-sm">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-gray-800 text-base">多氟多 (002407)</span>
                            <span class="text-xs bg-amber-100 text-amber-700 px-2 py-1 rounded-full">晶体龙头</span>
                        </div>
                        <div class="grid grid-cols-3 gap-2 mt-3 text-xs">
                            <div>
                                <span class="text-gray-500">产能</span>
                                <div class="font-bold text-base">8.5万吨</div>
                            </div>
                            <div>
                                <span class="text-gray-500">市占率</span>
                                <div class="font-bold text-base">约20%</div>
                            </div>
                            <div>
                                <span class="text-gray-500">吨成本</span>
                                <div class="font-bold text-base text-green-600">~4.5万</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-white rounded-lg p-4 shadow-sm">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-gray-800 text-base">天赐材料 (002709)</span>
                            <span class="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded-full">液体龙头</span>
                        </div>
                        <div class="grid grid-cols-3 gap-2 mt-3 text-xs">
                            <div>
                                <span class="text-gray-500">产能</span>
                                <div class="font-bold text-base">11万吨</div>
                            </div>
                            <div>
                                <span class="text-gray-500">市占率</span>
                                <div class="font-bold text-base">约25%</div>
                            </div>
                            <div>
                                <span class="text-gray-500">自给率</span>
                                <div class="font-bold text-base text-green-600">98%+</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 第二梯队 -->
            <div class="bg-gradient-to-r from-gray-50 to-slate-50 border border-gray-200 rounded-xl p-4">
                <h3 class="text-lg font-bold text-gray-800 flex items-center">
                    <span class="w-6 h-6 bg-gray-500 text-white rounded-full flex items-center justify-center text-sm mr-2">2</span>
                    第二梯队：二线龙头，弹性较大
                </h3>
                <p class="text-sm text-gray-600 mt-2">产能规模中等、具备一定成本优势、业绩弹性可观，但波动性相对更大</p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mt-3">
                    <div class="bg-white rounded-lg p-3 shadow-sm">
                        <div class="font-bold text-gray-800">天际股份 (002759)</div>
                        <div class="text-xs text-gray-500 mt-1">产能：4.3万吨 | 弹性：★★★★☆</div>
                        <div class="text-xs text-gray-500">纯六氟标的，业绩弹性最大</div>
                    </div>
                    <div class="bg-white rounded-lg p-3 shadow-sm">
                        <div class="font-bold text-gray-800">新宙邦 (300037)</div>
                        <div class="text-xs text-gray-500 mt-1">权益产能：~3.5万吨 | 弹性：★★★☆☆</div>
                        <div class="text-xs text-gray-500">电解液+氟化工双轮驱动</div>
                    </div>
                    <div class="bg-white rounded-lg p-3 shadow-sm">
                        <div class="font-bold text-gray-800">永太科技 (002326)</div>
                        <div class="text-xs text-gray-500 mt-1">产能：4.5万吨 | 弹性：★★★☆☆</div>
                        <div class="text-xs text-gray-500">含氟精细化学品龙头</div>
                    </div>
                </div>
            </div>
            
            <!-- 第三梯队 -->
            <div class="bg-gradient-to-r from-orange-50 to-red-50 border border-orange-200 rounded-xl p-4">
                <h3 class="text-lg font-bold text-orange-800 flex items-center">
                    <span class="w-6 h-6 bg-orange-500 text-white rounded-full flex items-center justify-center text-sm mr-2">3</span>
                    第三梯队：题材概念，高风险高弹性
                </h3>
                <p class="text-sm text-orange-700 mt-2">六氟业务占比较低或产能较小，主要以题材性机会为主，波动大、风险高</p>
                
                <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-3">
                    <div class="bg-white rounded-lg p-3 shadow-sm text-center">
                        <div class="font-semibold text-gray-800 text-sm">石大胜华</div>
                        <div class="text-[10px] text-gray-500 mt-1">溶剂+六氟一体化</div>
                    </div>
                    <div class="bg-white rounded-lg p-3 shadow-sm text-center">
                        <div class="font-semibold text-gray-800 text-sm">延安必康</div>
                        <div class="text-[10px] text-gray-500 mt-1">存量产能</div>
                    </div>
                    <div class="bg-white rounded-lg p-3 shadow-sm text-center">
                        <div class="font-semibold text-gray-800 text-sm">杉杉股份</div>
                        <div class="text-[10px] text-gray-500 mt-1">偏题材性质</div>
                    </div>
                    <div class="bg-white rounded-lg p-3 shadow-sm text-center">
                        <div class="font-semibold text-gray-800 text-sm">巨化股份</div>
                        <div class="text-[10px] text-gray-500 mt-1">氟化工龙头</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''
)

# 7. 重点公司深度分析 - 多氟多
gen.add_split_layout(
    title='🌟 重点公司：多氟多 (002407) - 晶体六氟全球龙头',
    left_title='核心优势',
    right_title='业绩弹性测算',
    left_content='''
    <div class="space-y-3">
        <div class="flex items-start">
            <span class="w-2 h-2 bg-green-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
            <div>
                <span class="font-semibold text-gray-800">成本优势显著</span>
                <p class="text-sm text-gray-600">全产业链一体化，吨成本约4.5万元，低于行业平均约30%，单吨毛利空间巨大</p>
            </div>
        </div>
        <div class="flex items-start">
            <span class="w-2 h-2 bg-blue-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
            <div>
                <span class="font-semibold text-gray-800">产能规模领先</span>
                <p class="text-sm text-gray-600">现有产能8.5万吨，全球第二大晶体六氟生产商，2026年计划出货6万吨</p>
            </div>
        </div>
        <div class="flex items-start">
            <span class="w-2 h-2 bg-purple-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
            <div>
                <span class="font-semibold text-gray-800">第二增长曲线</span>
                <p class="text-sm text-gray-600">电子级氢氟酸进入台积电、三星供应链，六氟磷酸钠布局钠电赛道，打开长期成长空间</p>
            </div>
        </div>
        <div class="flex items-start">
            <span class="w-2 h-2 bg-amber-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
            <div>
                <span class="font-semibold text-gray-800">客户结构优质</span>
                <p class="text-sm text-gray-600">深度绑定比亚迪、宁德时代等头部电池厂，长单占比高，业绩确定性强</p>
            </div>
        </div>
    </div>
    ''',
    right_content='''
    <div class="bg-gray-50 rounded-lg p-3">
        <table class="w-full text-sm">
            <thead>
                <tr class="border-b border-gray-200">
                    <th class="text-left py-2">价格(万/吨)</th>
                    <th class="text-right py-2">吨净利(万)</th>
                    <th class="text-right py-2">年利润(亿)</th>
                    <th class="text-right py-2">EPS(元)</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-gray-100">
                <tr>
                    <td class="py-1.5">10万</td>
                    <td class="py-1.5 text-right text-red-500">~1.0</td>
                    <td class="py-1.5 text-right">~6</td>
                    <td class="py-1.5 text-right">~0.5</td>
                </tr>
                <tr>
                    <td class="py-1.5">15万</td>
                    <td class="py-1.5 text-right text-amber-500">~4.5</td>
                    <td class="py-1.5 text-right">~27</td>
                    <td class="py-1.5 text-right">~2.25</td>
                </tr>
                <tr class="bg-green-50">
                    <td class="py-1.5 font-semibold">17.5万</td>
                    <td class="py-1.5 text-right text-green-600 font-semibold">~6.5</td>
                    <td class="py-1.5 text-right text-green-600 font-semibold">~39</td>
                    <td class="py-1.5 text-right text-green-600 font-semibold">~3.25</td>
                </tr>
                <tr>
                    <td class="py-1.5">20万</td>
                    <td class="py-1.5 text-right text-green-500">~8.5</td>
                    <td class="py-1.5 text-right">~51</td>
                    <td class="py-1.5 text-right">~4.25</td>
                </tr>
                <tr>
                    <td class="py-1.5">25万</td>
                    <td class="py-1.5 text-right text-green-500">~12.5</td>
                    <td class="py-1.5 text-right">~75</td>
                    <td class="py-1.5 text-right">~6.25</td>
                </tr>
            </tbody>
        </table>
        <p class="text-xs text-gray-500 mt-2">*按年出货6万吨、成本4.5万/吨测算，仅为六氟业务弹性</p>
    </div>
    '''
)

# 8. 重点公司深度分析 - 天赐材料
gen.add_split_layout(
    title='🌟 重点公司：天赐材料 (002709) - 电解液全球龙头',
    left_title='核心优势',
    right_title='业绩弹性测算',
    left_content='''
    <div class="space-y-3">
        <div class="flex items-start">
            <span class="w-2 h-2 bg-green-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
            <div>
                <span class="font-semibold text-gray-800">一体化成本优势</span>
                <p class="text-sm text-gray-600">液体六氟+电解液一体化，六氟自给率98%+，成本远低于行业平均</p>
            </div>
        </div>
        <div class="flex items-start">
            <span class="w-2 h-2 bg-blue-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
            <div>
                <span class="font-semibold text-gray-800">全球市占率第一</span>
                <p class="text-sm text-gray-600">电解液全球市占率约30%，六氟产能11万吨全球最大，规模效应显著</p>
            </div>
        </div>
        <div class="flex items-start">
            <span class="w-2 h-2 bg-purple-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
            <div>
                <span class="font-semibold text-gray-800">长单锁定业绩</span>
                <p class="text-sm text-gray-600">累计锁定长单超340万吨，覆盖未来3年主要产能，业绩确定性极强</p>
            </div>
        </div>
        <div class="flex items-start">
            <span class="w-2 h-2 bg-amber-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
            <div>
                <span class="font-semibold text-gray-800">技术壁垒深厚</span>
                <p class="text-sm text-gray-600">液体六氟工艺独家，新型锂盐LiFSI布局领先，持续引领行业技术方向</p>
            </div>
        </div>
    </div>
    ''',
    right_content='''
    <div class="bg-gray-50 rounded-lg p-3">
        <div class="text-center mb-3">
            <span class="text-sm font-semibold text-gray-700">2026年业绩预测</span>
        </div>
        <div class="grid grid-cols-2 gap-2 text-sm">
            <div class="bg-white p-2 rounded text-center">
                <div class="text-gray-500 text-xs">营收预测</div>
                <div class="text-lg font-bold text-blue-600">~280亿</div>
            </div>
            <div class="bg-white p-2 rounded text-center">
                <div class="text-gray-500 text-xs">净利润</div>
                <div class="text-lg font-bold text-green-600">~65-70亿</div>
            </div>
            <div class="bg-white p-2 rounded text-center">
                <div class="text-gray-500 text-xs">EPS</div>
                <div class="text-lg font-bold text-purple-600">~3.2元</div>
            </div>
            <div class="bg-white p-2 rounded text-center">
                <div class="text-gray-500 text-xs">PE(2026E)</div>
                <div class="text-lg font-bold text-amber-600">~14倍</div>
            </div>
        </div>
        <p class="text-xs text-gray-500 mt-2">*机构一致预期，具体以实际公告为准</p>
    </div>
    '''
)

# 9. 催化因素
gen.add_catalyst_tags([
    '储能需求超预期爆发',
    '六氟价格继续上涨',
    'Q3旺季供需缺口扩大',
    '行业整合加速',
    '钠电新型锂盐放量',
    '半导体制程突破',
    '海外产能布局落地',
    '政策支持新能源'
])

# 10. 风险提示
gen.add_risk_section([
    '六氟磷酸锂价格大幅波动风险：作为强周期品种，价格下跌将直接影响企业盈利',
    '产能释放超预期风险：若新增产能投产进度快于预期，可能导致供需格局恶化',
    '下游需求不及预期风险：新能源车或储能需求增速放缓将直接影响六氟需求',
    '技术替代风险：固态电池、半固态电池商业化进度超预期可能减少电解液需求',
    '行业竞争加剧风险：新进入者或现有厂商大幅扩产可能引发新一轮价格战',
    '原材料价格波动风险：碳酸锂、氢氟酸等原材料价格波动影响生产成本'
])

# 11. 投资结论
gen.add_conclusion(
    rating='推荐',
    conclusion='''
    六氟磷酸锂行业正处于新一轮周期上行阶段，供需紧平衡格局至少持续至2026年三季度。
    经历上一轮行业出清后，行业格局大幅优化，CR3达78%，龙头议价权显著增强。
    储能需求爆发成为核心增量，2026年全球需求预计增长30%以上。
    
    <br><br>
    
    <strong>投资建议重点关注第一梯队龙头：</strong><br>
    • <strong>多氟多</strong>：晶体六氟龙头，成本优势显著，业绩弹性最大，半导体氢氟酸+钠电提供第二成长曲线<br>
    • <strong>天赐材料</strong>：电解液全球龙头，一体化优势明显，长单锁定业绩，确定性最强
    
    <br>
    第二梯队可关注天际股份、新宙邦等弹性标的。<br>
    建议逢低布局，重点关注Q3旺季行情和价格上涨催化。
    '''
)

# 生成报告
report_html = gen.generate()

# 保存文件
output_path = 'docs/industry_chain/20260608_六氟磷酸锂产业链深度研究报告.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(report_html)

print(f'报告已生成：{output_path}')
print(f'报告大小：{os.path.getsize(output_path)} bytes')
