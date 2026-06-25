# PRD → 高保真原型 · 工作流

> 将PRD文档翻译为可交互的HTML原型，交付给甲方评审或开发参考。
> **PRD输入来源：** `../templates/`（商用交付版或AI原型生成版）

---

## 核心理念

**原型不是「照着PRD画页面」，而是「把PRD每条需求翻译成可视化的、可交互的、可评审的产品实物」。**

---

## 流水线：8个Phase

### Phase 0 · 前置检查（10min）

- [ ] PRD是否为最终版（有版本号、日期）
- [ ] PRD是否遵循10章原型导向标准（检查P0章节是否存在）
- [ ] PRD缺失P0章节？→ 退回补充
- [ ] 设计体系选择（从PRD Ch1读取，或按决策树）
- [ ] 输出格式（单HTML / 多HTML）
- [ ] 生成 `{project}/prototype/` 目录

### Phase 1 · 结构化清单（30min）

从PRD Ch6（功能点清单）提取逐按钮/逐弹窗/逐操作，输出 `checklist.yaml`：

```yaml
modules:
  - id: order
    name: 订单管理
    pages:
      - id: page-order-list
        name: 订单列表
    operations:
      - type: modal
        name: 审核订单
        action: showModal('modalReview')
      - type: button
        name: 导出Excel
        action: data-action="exportOrder"
      - type: navigation
        name: 查看详情
        action: navigateTo('order-detail?id=')
```

**每个模块必答3问：**
1. **List** — 数据在哪里展示？（表格/卡片/树）
2. **Detail** — 点击一行能看到什么？（弹窗/新页面）
3. **Action** — 用户能做什么？（新增/编辑/删除/审核/导出）

### Phase 2 · 架构规划（15min）

写入 `spec.md`：

- 引擎：纯原生JS + CSS（零CDN依赖，双击运行）
- 路由：window.location.hash
- 事件：data-action 委托（禁止inline onclick）
- 数据：mockData.js 统一数据池

### Phase 3 · 设计系统搭建（1h）

从PRD Ch1 读取设计体系，生成 `design-tokens.css`。

默认 Ant Design 5.x Token：

```css
:root {
  --brand-primary: #1677FF;
  --brand-bg: #F5F7FA;
  --sidebar-bg: #001529;
  --text-primary: #1D1D1F;
  --text-secondary: #595959;
  --border: #E5E6EB;
  --color-success: #52C41A;
  --color-warning: #FA8C16;
  --color-danger: #FF4D4F;
  --fs-title: 18px;
  --fs-body: 14px;
  --fs-table: 13px;
  --radius: 6px;
  --sp-xs: 8px;
  --sp-sm: 12px;
  --sp-md: 16px;
  --sp-lg: 24px;
  --touch-min: 48px;
}
```

> 其他设计体系Token → 见 `references/design-system-tokens.md`

**组件库清单（每个覆盖4态）：**

| 组件 | 有数据 | 空态 | 加载态 | 报错态 |
|------|--------|------|--------|--------|
| Table | ✅ | 无数据引导 | 骨架屏 | 网络错误 |
| Modal | 内容展示 | — | 加载中 | 加载失败 |
| Form | 填写中 | — | 提交中 | 校验失败 |
| Search | 有结果 | 无结果引导 | 搜索中 | 网络错误 |

### Phase 4 · 页面实现（核心）

按PRD Ch5（页面清单）逐页实现。

每个页面结构：

```html
<div id="page-{name}" class="page">
  <!-- 搜索区（如有） -->
  <div class="search-bar">...</div>
  <!-- 数据展示 -->
  <table class="data-table">...</table>
  <!-- 分页 -->
  <div class="pagination">...</div>
</div>
```

交互 handler 使用事件委托：

```javascript
document.addEventListener('click', function(e) {
  const action = e.target.closest('[data-action]')?.dataset.action;
  if (!action) return;
  switch(action) {
    case 'review': showModal('modalReview'); break;
    case 'export': exportExcel(); break;
    case 'refresh': loadData(); break;
  }
});
```

### Phase 5 · Mock数据池（30min）

从PRD Ch8 提取 Mock数据，生成 `data/mock-data.js`。

```javascript
var MOCK = {
  orders: {
    list: [
      { id: 1, order_no: "ORD202601010001", customer: "张三",
        amount: 3842.50, status: "pending_review",
        created_at: "2026-01-01 10:28" },
      // ... 至少5条有业务意义的真实数据
    ],
    emptyList: [],
    longList: Array.from({length: 100}, (_, i) => ({...})),
  },
  getOrderById: function(id) {
    return this.orders.list.find(o => o.id === id) || null;
  },
};
```

**约束：**
- 同一实体跨页面数据一致
- 金额计算真实可验证
- 空态/极限态只需切换数据源

### Phase 6 · 自动化验收（30min）

运行 `scripts/verify-prototype.py`：

```bash
cd {project}/prototype && python3 scripts/verify-prototype.py
```

**门禁：** ≥90% 通过才允许交付。

| 检查项 | 说明 |
|--------|------|
| 1.1 模态框完整性 | 每个showModal有对应id元素 |
| 1.2 函数完整性 | 每个onclick有函数定义 |
| 1.3 页面路由完整性 | 每个data-page有对应id |
| 1.4 事件处理完整性 | 每个data-action有case |
| 2.1 Emoji使用率 | ≤20% |
| 2.2 Token引用 | HTML引用design-tokens.css |
| 2.3 字号合规 | ≥12px |
| 3.1 空态覆盖 | 有「暂无数据」等文案 |
| 3.2 加载态覆盖 | 有skeleton/loading |

### Phase 7 · 评审走查

在HTML末尾添加评审模式快捷键：

| 快捷键 | 功能 |
|--------|------|
| **R** | 评审标注 — 每个元素标注属性引用 |
| **L** | 骨架屏加载态 |
| **D** | 恢复真实数据 |

### Phase 8 · 交付

产出物结构：

```
{project}/prototype/
├── index.html              ← 预览入口
├── spec.md                 ← 架构规划
├── checklist.yaml          ← 勾选清单
├── design-tokens.css       ← 设计Token
├── data/
│   └── mock-data.js        ← Mock数据池
├── scripts/
│   └── verify-prototype.py ← 验收脚本
└── admin/
    └── index.html          ← 管理后台原型
```

---

## 设计体系选择

从PRD Ch1读取，或按以下决策树选择：

```
React B端 → Ant Design 5.x（默认）
Vue 3 B端 → Element Plus（#409EFF）
全端统一 → TDesign（#0052D9）
现代B端 → Arco Design（#165DFF）
数据密集型 → Semi Design（#0077FA）
移动电商 → NutUI（#FA2C19, 375px基准）
小程序 → 微信WeUI（#07C160）
```

> 详细Token参考：`references/design-system-tokens.md`

---

## 大规模原型并行工作流（30+页面）

当PRD包含30+页面、5+功能域时，使用此增强流程可显著提速（已验证36页/7域原型在30分钟内完成）。

### 架构选型：纯原生JS SPA

```
引擎：原生JS（零CDN/零React依赖，双击可运行）
路由：window.location.hash
交互：data-action 事件委托（全局document监听）
数据：data/mock-data.js 统一数据池
页面注册：registerRender(pageId, fn) 模式
```

**为什么选原生JS而非React/Babel：**
- WSL/headless下Babel standalone 3MB编译常超时导致空白页
- 单HTML文件Hash路由支持直接 `file://` 打开
- 纯JS更易由多个开发者并行生成

### 三阶段流程

**Phase A · 建基（5min）**
1. 创建目录结构
2. 设计 design-tokens.css（Ant Design Token）
3. 编写 data/mock-data.js（统一数据池）
4. 编写 index.html（壳：侧栏导航 + 路由系统 + 事件委托 + modal/drawer/toast系统）
   - 侧栏每个菜单项 `data-page="DS-Xxx-001"`
   - 全局事件委托：`data-action` 按钮 / `.nav-item[data-page]` / `tr[data-id][data-page]` / 遮罩层关闭
   - 工具函数：`registerRender()` / `tag()` / `pagination()` / `emptyState()` / `openModal()` / `showToast()`

**Phase B · 并行实现（各域10-15min）**
```
分工：每个功能域一个独立JS文件（pages-{domain}.js）
每个页面通过 registerRender('pageId', fn) 注册
渲染函数返回HTML字符串，使用MOCK数据和全局工具函数
```

每个域JS的注册模式：
```javascript
registerRender('DS-Agg-001', function() {
  var data = MOCK.aggregation.interfaces;
  var html = '<div class="card">'
    + '<div class="card-header"><h3>接口管理</h3>'
    + '<button class="btn btn-primary" data-action="new">新建</button></div>'
    + '<div class="card-body">'
    + '<table class="data-table"><tr><th>名称</th><th>状态</th><th>操作</th></tr>'
    + data.map(function(item) {
        return '<tr data-id="' + item.id + '" data-page="DS-Agg-001">'
          + '<td>' + item.name + '</td>'
          + '<td>' + tag(item.status) + '</td>'
          + '<td class="col-actions"><a data-action="edit">编辑</a><a data-action="delete">删除</a></td>'
        + '</tr>';
      }).join('')
    + '</table></div></div>';
  return html;
});
```

**Phase C · 组装验证（5min）**
```bash
# 1. 语法验证（每个域文件必须通过）
for f in pages-*.js; do node --check "$f" || echo "FAILED: $f"; done

# 2. 交叉比对：所有data-action是否有对应handler
grep -noP 'data-action="([^"]*)"' pages-*.js | sed 's/.*data-action="//;s/"//' | sort -u > /tmp/actions.txt
grep -noP 'window\.on[A-Za-z][A-Za-z0-9]*\s*=' pages-*.js index.html | sed 's/.*window\.//;s/\s*=.*//' | sort -u > /tmp/handlers.txt
for a in $(cat /tmp/actions.txt); do
  cap="on$(echo $a | sed 's/^\(.\)/\U\1/')"
  low="on$a"
  if ! grep -q -e "$cap" -e "$low" /tmp/handlers.txt 2>/dev/null; then
    echo "❌ 无handler: $a"
  fi
done

# 3. 启动HTTP服务 + headless截图验证
python3 -m http.server 8899 &
chromium-browser --headless --no-sandbox --disable-gpu \
  --screenshot=./screenshot-xxx.png --window-size=1440,900 \
  "http://localhost:8899/index.html#DS-Agg-001"

# 4. 截图健康检查
ls -la screenshot-*.png
# 正常：100-200KB，且不同页面大小差异明显
# 异常：全部等大且18-20KB → 渲染失败
```

### 常见陷阱补充

| # | 陷阱 | 预防 |
|---|------|------|
| 1 | 按钮有内容无交互 | 验收脚本扫所有button有handler |
| 2 | 模态框有按钮无对应弹窗 | 检查showModal('x')→id="x" |
| 3 | 只有理想态，缺空态/加载态 | 每个列表页手动切换数据源 |
| 4 | JS插入破坏函数边界 | 修改后运行 node --check |
| 5 | 「多种入库方式」只做了两三种 | 枚举值必须从PRD列全 |
| 6 | 底部Tab随页面滚动 | Tab在滚动容器外，flex-shrink:0 |
| 7 | 并行子Agent handler名大小写不一致 | 事件委托加fallback：`window[驼峰] \|\| window[原样]` |
| 8 | Headless截图全等大18KB | 服务器未响应或JS语法错误，先curl验证服务器连通性 |
