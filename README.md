# 🔨 原型之王 · PRD到高保真原型工作流

**把产品需求文档变成可点击的HTML原型，8个Phase一次搞定。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 这是什么

从PRD到可交互HTML原型的**完整工作流**。消费 `prd-king` 产出的10章PRD，按8个Phase翻译为DOM元素+交互逻辑+Mock数据。

### 核心理念

> **原型不是「照着PRD画页面」，而是「把PRD每条需求翻译成可视化的、可交互的、可评审的产品实物」。**

---

## 📂 目录结构

```
prototype-king/
├── SKILL.md                          ← Codex/Hermes skill 安装入口
├── WORKFLOW.md                       ← 8 Phase 工作流
├── references/
│   ├── design-system-tokens.md       ← 6大设计体系Token对照
│   └── ant-design-5-tokens.md        ← Ant Design 5.x 完整Token
├── scripts/
│   └── verify-prototype.py           ← 自动化验收脚本（≥90%门禁）
├── README.md
├── LICENSE
└── CHANGELOG.md
```

## 🚀 快速开始

### 前提

你已经有一份符合 **10章原型导向PRD标准** 的文档（参见 [prd-king](https://github.com/kangedy/prd-king)）。

### 安装为技能（Codex / Hermes Agent）

```bash
# Codex 用户
codex skills install kangedy/prototype-king

# Hermes Agent 用户
mkdir -p ~/.hermes/skills/product/prototype-king/
cp -r * ~/.hermes/skills/product/prototype-king/
# → 说「根据PRD做原型」
```

### 手动执行

先确认你已经有一份符合10章PRD标准的文档，然后：

```bash
# 1. 创建工作目录
mkdir -p my-project/prototype && cd my-project/prototype

# 2. 复制工作流文件
cp -r <path-to-prototype-king>/* ./

# 3. 打开工作流，按8 Phase执行
open WORKFLOW.md

# 4. Phase 6: 运行自动化验收
python3 scripts/verify-prototype.py
```

### 如果你是 AI Agent 用户

| 工具 | 使用方式 |
|------|---------|
| **Hermes Agent** | `skill_view(name='prototype-workflow')` → 说「根据PRD做原型」 |
| **OpenClaw** | 对话中说「按 workflow 做原型，参考 prototype/ 目录」 |
| **Claude Code** | 追加 `CLAUDE.md` 引用 WORKFLOW.md |
| **Codex CLI** | 对话中说「读取 WORKFLOW.md 执行原型生成」 |

---

## 🏗 8个Phase一览

| Phase | 名称 | 工时 | 产出 |
|-------|------|------|------|
| P0 | 前置检查 | 10min | 确认PRD完整性+设计体系 |
| P1 | 结构化清单 | 30min | `checklist.yaml`（逐按钮/弹窗/操作） |
| P2 | 架构规划 | 15min | `spec.md`（路由/事件/数据） |
| P3 | 设计系统搭建 | 1h | `design-tokens.css` |
| P4 | 页面实现 | 核心 | 每页HTML+JS交互 |
| P5 | Mock数据 | 30min | `data/mock-data.js` |
| P6 | 自动化验收 | 30min | `verify-prototype.py` 运行 |
| P7 | 评审走查 | 30min | 快捷键R/L/D模式 |
| P8 | 交付 | — | admin/index.html |

---

## 🎨 设计体系选择

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

---

## ✅ 验收门禁

运行 `python3 scripts/verify-prototype.py`，通过标准 ≥90%：

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

---

## 配套项目

- [prd-king](https://github.com/kangedy/prd-king) — 10章原型导向PRD标准（写需求的）

---

## 开源协议

MIT License
