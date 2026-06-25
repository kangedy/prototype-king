---
name: prototype-king
description: 'PRD→高保真原型工作流 — 8个Phase，从产品需求文档到可交互HTML原型。配套 prd-king 的10章PRD标准使用，含自动化验收脚本。'
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [prototype, prd, html, design-system, workflow, verification]
    category: product
---

# Prototype King — PRD → 原型工作流

> 消费 `prd-king` 产出的10章PRD，按8个Phase翻译为DOM元素+交互逻辑+Mock数据。
> 详细工作流文档见 `WORKFLOW.md`

## 核心理念

**原型不是「照着PRD画页面」，而是「把PRD每条需求翻译成可视化的、可交互的、可评审的产品实物」。**

## 快速开始

```bash
# 创建工作目录
mkdir -p my-project/prototype

# 复制工作流文件
cp -r <prototype-king-path>/* my-project/prototype/

# 打开工作流，按8 Phase执行
```

## 8 Phase 一览

| Phase | 名称 | 工时 | 产出 |
|-------|------|------|------|
| P0 | 前置检查 | 10min | 确认PRD完整性+设计体系 |
| P1 | 结构化清单 | 30min | checklist.yaml（逐按钮/弹窗/操作） |
| P2 | 架构规划 | 15min | spec.md（路由/事件/数据） |
| P3 | 设计系统搭建 | 1h | design-tokens.css |
| P4 | 页面实现 | 核心 | 每页HTML+JS交互 |
| P5 | Mock数据 | 30min | data/mock-data.js |
| P6 | 自动化验收 | 30min | verify-prototype.py 运行 |
| P7 | 评审走查 | 30min | 快捷键R/L/D模式 |
| P8 | 交付 | — | admin/index.html |

## 设计体系选择

从PRD Ch1读取，或按决策树：

```
React B端 → Ant Design 5.x（默认）
Vue 3 B端 → Element Plus（#409EFF）
全端统一 → TDesign（#0052D9）
现代B端 → Arco Design（#165DFF）
数据密集型 → Semi Design（#0077FA）
移动电商 → NutUI（#FA2C19）
小程序 → 微信WeUI（#07C160）
```

## 验收门禁

```bash
cd my-project/prototype && python3 scripts/verify-prototype.py
```

通过标准 ≥90%。

| 检查项 | 说明 |
|--------|------|
| 模态框完整性 | 每个showModal有对应id |
| 函数完整性 | 每个onclick有函数定义 |
| 页面路由完整性 | 每个data-page有对应id |
| 事件处理完整性 | 每个data-action有case |
| Emoji使用率 | ≤20% |
| Token引用 | HTML引用design-tokens.css |
| 字号合规 | ≥12px |
| 空态覆盖 | 有「暂无数据」等文案 |
| 加载态覆盖 | 有skeleton/loading |

## 配套项目

- **prd-king** — 10章原型导向PRD标准 https://github.com/kangedy/prd-king

## 参考文件

| 文件 | 用途 |
|------|------|
| `WORKFLOW.md` | 8 Phase 完整工作流 |
| `references/design-system-tokens.md` | 6大设计体系Token对照 |
| `references/ant-design-5-tokens.md` | Ant Design 5.x 完整Token手册 |
| `scripts/verify-prototype.py` | 自动化验收脚本 |
