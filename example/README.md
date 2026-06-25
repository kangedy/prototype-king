<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><title>原型示例 · 说明</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif}
body{background:#f5f5f5;padding:48px;color:#333;max-width:800px;margin:0 auto}
h1{font-size:24px;margin-bottom:8px}
p{color:#666;margin-bottom:24px;line-height:1.6}
.card{background:#fff;border-radius:8px;padding:24px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.06)}
.card h2{font-size:16px;margin-bottom:8px}
.card ul{padding-left:20px;color:#555;line-height:1.8}
code{background:#f0f0f0;padding:2px 6px;border-radius:3px;font-size:13px}
a{color:#1677ff;text-decoration:none}
</style></head>
<body>
<h1>🔨 原型示例 · 订单管理系统</h1>
<p>展示 <strong>prototype-king</strong> 8 Phase 工作流的典型产出物结构。<br>
这是从 PRD 翻译为可交互 HTML 原型后的结果。</p>

<div class="card">
  <h2>📂 示例文件结构</h2>
  <pre style="background:#f8f8f8;padding:16px;border-radius:6px;font-size:13px;line-height:1.7">
example/
├── admin/
│   └── index.html                 ← 管理后台原型（双击打开）
├── data/
│   └── mock-data.js               ← Mock数据池
└── README.md                      ← 本文件</pre>
</div>

<div class="card">
  <h2>▶️ 运行方式</h2>
  <ul>
    <li>直接双击 <code>admin/index.html</code> 在浏览器打开（零依赖）</li>
    <li>或运行 <code>python3 scripts/verify-prototype.py</code> 验收</li>
    <li>从 <code>data/mock-data.js</code> 切换数据源测试空态/加载态</li>
  </ul>
</div>

<div class="card">
  <h2>📋 示例覆盖的验收门禁</h2>
  <ul>
    <li>✅ 模态框：<code>showModal('modalReview')</code> → 有对应 id</li>
    <li>✅ 函数完整性：search/submitReview/closeModal/showToast 均有定义</li>
    <li>✅ 事件委托：data-action 事件分发机制</li>
    <li>✅ 空态：无数据时显示引导文案</li>
    <li>✅ 加载态：数据加载时显示骨架屏/shimer</li>
    <li>✅ Token引用：引用了 design-tokens.css</li>
  </ul>
</div>

<div class="card">
  <h2>🔗 相关资源</h2>
  <ul>
    <li><a href="https://github.com/kangedy/prototype-king">prototype-king</a> — 8 Phase 工作流</li>
    <li><a href="https://github.com/kangedy/prd-king">prd-king</a> — 10章PRD标准</li>
  </ul>
</div>
</body>
</html>
