# 设计体系选择指南

## 场景-规范映射表

| 场景 | 首选规范 | 替代选项 |
|------|---------|---------|
| **B端管理后台（React）** | **Ant Design 5.x** | Arco Design |
| **B端管理后台（Vue3）** | **Element Plus** | — |
| **全端项目（Web+小程序）** | **TDesign（腾讯）** | Ant Design |
| **现代年轻化B端** | **Arco Design（字节）** | Semi Design |
| **数据密集型后台** | **Semi Design（抖音）** | Ant Design |
| **移动端电商H5** | **NutUI（京东）** | WeUI |
| 小程序 | 微信WeUI | — |
| iOS App | Apple HIG | — |
| 电商促销页 | Ant Design + 拼多多暖色 | 自研促销色板 |

## 6大国产专业设计体系详解

### 1. Ant Design 5.x（阿里 · 默认）
- **主色** #1677FF | **背景** #F5F7FA | **侧栏** #001529
- **框架** React | **组件数** 72（6大类）
- **栅格** 8px + 24列 | **圆角** 6px
- **无障碍** WCAG AA
- **特点** 最成熟、生态最大、Token体系最完整
- **原型生成** ✅ 完美支持（默认）

### 2. Element Plus（饿了么 · Vue3首选）
- **主色** #409EFF | **背景** #F5F7FA | **侧栏** #304156
- **框架** Vue 3 | **组件数** 55+
- **栅格** 24列 | **圆角** 4px
- **特点** Vue3生态最流行，最接近Ant Design完备度
- **注意** 组件命名不同：Table→el-table, Form→el-form
- **原型生成** ✅ 支持（命名映射需调整）

### 3. TDesign（腾讯 · 全端统一）
- **主色** #0052D9 | **背景** #FFFFFF | **侧栏** #1E293B
- **框架** React/Vue2/Vue3/小程序（全覆盖）
- **组件数** 各端60+ | **圆角** 6px
- **特点** 跨端一致性最强，移动端适配好
- **原型生成** ✅ 支持

### 4. Arco Design（字节跳动 · 现代B端）
- **主色** #165DFF | **背景** #F2F3F5 | **侧栏** #232324
- **框架** React/Vue 3 | **组件数** 60+
- **栅格** 12列 | **圆角** 8px
- **特点** 比Ant Design更现代，暗色模式原生支持
- **原型生成** ✅ 支持

### 5. Semi Design（抖音/字节 · 创新体系）
- **主色** #0077FA | **背景** #F5F5F5 | **侧栏** #1C1C1E
- **框架** React（无Vue） | **组件数** 50+
- **栅格** 8px | **圆角** 6px
- **特点** Foundation/Adapter架构，表单密集型优化极好，无障碍WCAG AA+
- **原型生成** ✅ 支持

### 6. NutUI（京东 · 移动端零售C端）
- **主色** #FA2C19（京东红）| **背景** #F7F7F7
- **框架** Vue 3（无React）| **组件数** 70+
- **基准** 375px | **圆角** 12px
- **特点** 移动端优先，电商组件丰富（SKU选择器/倒计时/价格组件）
- **注意** B端能力弱，不适合纯管理后台
- **原型生成** ⚠️ 部分支持

## Token快速替换对照表

| CSS变量 | Ant Design | Element Plus | TDesign | Arco Design | Semi | NutUI |
|---------|-----------|-------------|---------|-------------|------|-------|
| --brand-primary | #1677FF | #409EFF | #0052D9 | #165DFF | #0077FA | #FA2C19 |
| --brand-bg | #F5F7FA | #F5F7FA | #FFFFFF | #F2F3F5 | #F5F5F5 | #F7F7F7 |
| --sidebar-bg | #001529 | #304156 | #1E293B | #232324 | #1C1C1E | —(移动端) |
| --text-primary | #1D1D1F | #303133 | #1A1A2E | #1D2129 | #1C1C1E | #1A1A1A |
| --border-color | #E5E6EB | #DCDFE6 | #DCDCDC | #E5E6EB | #D9D9D9 | #EEE |
| --radius | 6px | 4px | 6px | 8px | 6px | 12px |
| --font-body | 14px | 14px | 14px | 14px | 14px | 14px |

## 决策树

```
PRD是否有明确指定的设计体系？
├── 是 → 按PRD执行
└── 否 → 技术栈是？
       ├── React → Ant Design 5.x（默认）
       ├── Vue 3 → Element Plus
       ├── 全端（Web+小程序） → TDesign
       ├── 现代年轻化B端 → Arco Design
       ├── 数据密集型 → Semi Design
       ├── 移动电商H5 → NutUI
       └── 不确定 → Ant Design（最安全，事实标准）
```
