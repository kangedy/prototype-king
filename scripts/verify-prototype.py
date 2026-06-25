#!/usr/bin/env python3
"""PRD → 原型质量门禁 · 自动化验收脚本
用途：交付前自动扫描原型文件，检查功能完整性、设计一致性、状态覆盖
通过标准：≥90%
安装：复制到 prototype/scripts/ 目录，python3 verify-prototype.py 直接运行
"""
import os, re, sys
from collections import OrderedDict

# Windows GBK 编码兼容
if sys.platform == 'win32' and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
elif sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROTOTYPE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_file(path):
    try:
        with open(os.path.join(PROTOTYPE_DIR, path), 'r') as f:
            return f.read()
    except: return None

G = lambda t: f"\033[92m{t}\033[0m"
Y = lambda t: f"\033[93m{t}\033[0m"
R = lambda t: f"\033[91m{t}\033[0m"

def check_modals(content):
    calls = re.findall(r"showModal\('([^']+)'\)", content)
    defs = set(re.findall(r'id="([^"]*[Mm]odal[^"]*)"', content))
    total = len(calls)
    passed = sum(1 for c in calls if c in defs)
    return total, passed

def check_functions(content):
    calls = set()
    for m in re.finditer(r'onclick="([^"]+)"', content):
        for f in re.finditer(r'([a-zA-Z_]\w+)\s*\(', m.group(1)):
            calls.add(f.group(1))
    defs = set(re.findall(r'^function\s+(\w+)\s*\(', content, re.MULTILINE))
    defs.update(set(re.findall(r'^var\s+(\w+)\s*=\s*function', content, re.MULTILINE)))
    calls -= {'showToast'}
    total = len(calls)
    passed = sum(1 for c in calls if c in defs)
    return total, passed

def check_routes(content):
    pages = set(re.findall(r'data-page="([^"]+)"', content))
    ids = set(re.findall(r'id="page-([^"]+)"', content))
    pages -= {'${pageId}'}
    total = len(pages)
    passed = sum(1 for p in pages if p in ids)
    return total, passed

def check_actions(content):
    actions = set()
    for m in re.finditer(r'data-action="([^"]+)"', content):
        val = m.group(1)
        if '${' not in val:
            actions.add(val)
    cases = set(re.findall(r"case\s+'([^']+)':|case\s+\"([^\"]+)\":", content))
    case_names = set()
    for c in cases:
        case_names.add(c[0] if c[0] else c[1])
    case_names.add('noop')
    total = len(actions)
    passed = sum(1 for a in actions if a in case_names)
    return total, passed

def check_emoji(content):
    emoji_pattern = re.compile(
        '[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF'
        '\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF'
        '\u2600-\u26FF\u2700-\u27BF\u2B50\U0001F900-\U0001F9FF'
        '\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF'
        '\u231A-\u231B\u23E9-\u23F3\u25AA-\u25FE\u2B05-\u2B55'
        '\u2934\u2935\u3030\u303D\u3297\u3299]+')
    emojis = emoji_pattern.findall(content)
    ratio = len(emojis) / max(len(content), 1) * 100
    return round(ratio, 1)

def check_min_font(content):
    sizes = re.findall(r'font-size:\s*(\d+)px', content)
    if not sizes: return 999
    return min(int(s) for s in sizes)

def check_empty_states(content):
    patterns = ['暂无', '暂无数据', 'empty', '无结果', '未找到', '还没有', '去创建', '添加第一个']
    return sum(content.count(p) for p in patterns)

def check_loading_states(content):
    patterns = ['loading', 'skeleton', '加载', 'spinner', 'shimmer', '骨架']
    return sum(content.count(p) for p in patterns)

def check_token_ref(content):
    return 'design-tokens.css' in content

def main():
    admin = read_file('admin/index.html')
    mini = read_file('miniprogram/index.html')
    checklist = read_file('checklist.yaml')

    checks = OrderedDict()
    checks["📋 功能完整性"] = []
    checks["🎨 设计一致性"] = []
    checks["📊 状态覆盖"] = []

    if admin:
        t, p = check_modals(admin)
        checks["📋 功能完整性"].append({"label": "1.1 模态框完整性", "summary": f"{p}/{t} 通过", "icon": G("✅") if t == p else R("❌"), "passed": t == p})

    if admin:
        t, p = check_functions(admin)
        checks["📋 功能完整性"].append({"label": "1.2 函数完整性", "summary": f"{p}/{t} 通过", "icon": G("✅") if t == p else R("❌"), "passed": t == p})

    combined = (admin or '') + (mini or '')
    t, p = check_routes(combined)
    checks["📋 功能完整性"].append({"label": "1.3 页面路由完整性", "summary": f"{p}/{t} 通过", "icon": G("✅") if t == p else R("❌"), "passed": t == p})

    if mini:
        t, p = check_actions(mini)
        checks["📋 功能完整性"].append({"label": "1.4 事件处理完整性", "summary": f"{p}/{t} 通过", "icon": G("✅") if t == p else R("❌"), "passed": t == p})

    emoji_ratios = {}
    if admin: emoji_ratios['admin'] = check_emoji(admin)
    if mini: emoji_ratios['miniprogram'] = check_emoji(mini)
    max_ratio = max(emoji_ratios.values()) if emoji_ratios else 0
    ok = max_ratio <= 20.0
    checks["🎨 设计一致性"].append({"label": "2.1 Emoji使用率", "summary": f"{max_ratio}% ({'达标' if ok else '超标'})", "icon": G("✅") if ok else Y("⚠️"), "passed": ok, "details": [f"{k}: {v}%" for k,v in emoji_ratios.items()]})

    admin_ok = check_token_ref(admin or '')
    mini_ok = check_token_ref(mini or '')
    token_ok = admin_ok and mini_ok
    checks["🎨 设计一致性"].append({"label": "2.2 Token引用", "summary": "已引用" if token_ok else "未引用", "icon": G("✅") if token_ok else R("❌"), "passed": token_ok, "details": [f"admin: {'已引用' if admin_ok else '未引用'}", f"miniprogram: {'已引用' if mini_ok else '未引用'}"]})

    sizes = [int(s) for c in [admin or '', mini or ''] for s in re.findall(r'font-size:\s*(\d+)px', c)]
    min_s = min(sizes) if sizes else 999
    a11y_ok = min_s >= 12
    checks["🎨 设计一致性"].append({"label": "2.3 适老化合规", "summary": f"最小字号 {min_s}px (≥12px)" if a11y_ok else f"最小字号 {min_s}px (<12px!)", "icon": G("✅") if a11y_ok else R("❌"), "passed": a11y_ok})

    empty_count = check_empty_states(combined)
    checks["📊 状态覆盖"].append({"label": "3.1 空态覆盖", "summary": f"{empty_count} 处", "icon": G("✅") if empty_count > 0 else R("❌"), "passed": empty_count > 0})

    load_count = check_loading_states(combined)
    checks["📊 状态覆盖"].append({"label": "3.2 加载态覆盖", "summary": f"{load_count} 处", "icon": G("✅") if load_count > 0 else R("❌"), "passed": load_count > 0})

    total = sum(len(v) for v in checks.values())
    passed = sum(1 for v in checks.values() for c in v if c['passed'])
    pct = round(passed / total * 100) if total else 0

    print(f"{'╔' + '═'*50 + '╗'}")
    print(f"{'║':<1}{'原型 · 自动化验收报告':^48}{'║':>1}")
    print(f"{'╠' + '═'*50 + '╣'}")
    for cat, items in checks.items():
        print(f"{'║ ' + cat:<50}{'║':>1}")
        for c in items:
            det = ''
            if c.get('details'):
                det = '\n' + '\n'.join(f"{'║':>4} → {d}" for d in c['details'])
            print(f"{'║   ' + c['icon'] + ' ' + c['label'] + ' ' + c['summary']:<50}{'║':>1}{det}")
    print(f"{'╠' + '═'*50 + '╣'}")
    verdict = f"✅ 验收通过（≥90%）" if pct >= 90 else f"❌ 退回修复（需≥90%）"
    print(f"{'║ 总分: ' + str(pct) + '%':<50}{'║':>1}")
    print(f"{'║ 判定: ' + verdict:<50}{'║':>1}")
    print(f"{'╚' + '═'*50 + '╝'}")

    if checklist:
        module_count = len(re.findall(r'^\s+- id:', checklist, re.MULTILINE))
        print(f"\n📋 检查清单: {module_count} 个模块")
    print(f"\n{'✓' if admin else '✗'} admin/index.html | {'✓' if mini else '✗'} miniprogram/index.html | {'✓' if checklist else '✗'} checklist.yaml")
    sys.exit(0 if pct >= 90 else 1)

if __name__ == '__main__':
    main()
