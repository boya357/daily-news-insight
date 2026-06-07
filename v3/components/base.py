"""
基础组件类
所有组件继承自 Component，提供统一的渲染接口
"""

class Component:
    """组件基类"""
    
    def __init__(self, **kwargs):
        self.props = kwargs
    
    def render(self) -> str:
        """渲染组件为HTML字符串"""
        raise NotImplementedError("子类必须实现 render 方法")
    
    def __str__(self) -> str:
        return self.render()
    
    def __add__(self, other):
        """支持组件相加拼接"""
        if isinstance(other, Component):
            return self.render() + other.render()
        elif isinstance(other, str):
            return self.render() + other
        return NotImplemented


class HTMLComponent(Component):
    """纯HTML包装组件，直接返回HTML字符串"""
    
    def __init__(self, html: str):
        super().__init__()
        self.html = html
    
    def render(self) -> str:
        return self.html


def get_animation_css() -> str:
    """
    获取全局动效CSS样式
    包含：入场动画、悬停效果、数字滚动、渐变进度条等
    """
    return '''
<style>
/* 卡片悬停上浮效果 */
.card-hover {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.card-hover:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08), 0 4px 8px rgba(0, 0, 0, 0.04) !important;
}

/* 入场淡入上移动画 */
.fade-in-up {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}
.fade-in-up.visible {
    opacity: 1;
    transform: translateY(0);
}

/* 数字滚动动画 */
@keyframes countUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* 徽章标签系统 */
.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 16px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}
.badge-hot {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    color: #d97706;
}
.badge-good {
    background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
    color: #059669;
}
.badge-risk {
    background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
    color: #dc2626;
}
.badge-info {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
    color: #2563eb;
}

/* 表格悬停高亮 */
.table-hover tbody tr:hover {
    background: #f9fafb !important;
}

/* 折叠面板 */
.collapse-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-out;
}
.collapse-content.open {
    max-height: 2000px;
}
.collapse-toggle {
    cursor: pointer;
    user-select: none;
}
.collapse-arrow {
    transition: transform 0.3s ease;
}
.collapse-arrow.open {
    transform: rotate(180deg);
}

/* 渐变进度条 */
.progress-gradient {
    background: linear-gradient(90deg, #ef4444 0%, #f59e0b 50%, #10b981 100%);
}

/* 玻璃态悬浮效果 */
.glass-effect {
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}
</style>
'''


def get_animation_js() -> str:
    """
    获取全局动效JavaScript
    包含：入场动画触发、数字滚动动画等
    """
    return '''
<script>
// 入场动画 - 滚动时触发
document.addEventListener('DOMContentLoaded', function() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    // 观察所有带fade-in-up类的元素
    document.querySelectorAll('.fade-in-up').forEach(el => {
        observer.observe(el);
    });
});

// 数字滚动动画
function animateNumber(element, target, duration = 1500) {
    const start = 0;
    const startTime = performance.now();
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // 缓动函数 - easeOutExpo
        const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        const current = Math.floor(start + (target - start) * easeProgress);
        
        element.textContent = current.toLocaleString();
        
        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    
    requestAnimationFrame(update);
}

// 折叠面板切换
function toggleCollapse(id) {
    const content = document.getElementById('collapse-' + id);
    const arrow = document.getElementById('collapse-arrow-' + id);
    
    if (content.classList.contains('open')) {
        content.classList.remove('open');
        arrow.classList.remove('open');
    } else {
        content.classList.add('open');
        arrow.classList.add('open');
    }
}
</script>
'''


def get_animation_assets() -> str:
    """
    获取所有动效资源（CSS + JS）
    """
    return get_animation_css() + get_animation_js()
