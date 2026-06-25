# Ant Design 5.x Token Reference

B端管理后台默认风格。当用户说"换成阿里的"或没有指定风格时使用。

## 色彩

| Token | Value | 用途 |
|-------|-------|------|
| `--primary` | `#1677ff` | 主色/按钮/链接/选中态 |
| `--primary-hover` | `#4096ff` | 按钮悬停 |
| `--primary-active` | `#0958d9` | 按钮按下 |
| `--primary-bg` | `#e6f4ff` | 浅蓝背景/选中行 |
| `--primary-border` | `#91caff` | 蓝色边框 |
| `--bg` | `#f5f5f5` | 页面背景 |
| `--bg-card` | `#ffffff` | 卡片/内容区背景 |
| `--text` | `rgba(0,0,0,0.88)` | 主文字 |
| `--text-secondary` | `rgba(0,0,0,0.45)` | 次要文字 |
| `--text-tertiary` | `rgba(0,0,0,0.25)` | 禁用/占位文字 |
| `--border` | `#f0f0f0` | 分割线/边框 |
| `--border-dark` | `#d9d9d9` | 输入框边框 |
| `--success` | `#52c41a` | 成功 |
| `--warning` | `#fa8c16` | 警告 |
| `--danger` | `#ff4d4f` | 危险/错误 |

## 侧边栏（暗色导航）

| Token | Value | 用途 |
|-------|-------|------|
| `--sidebar-bg` | `#001529` | 侧栏背景 |
| `--sidebar-text` | `rgba(255,255,255,0.85)` | 侧栏文字 |
| `--sidebar-text-secondary` | `rgba(255,255,255,0.45)` | 侧栏分类标题 |
| `--sidebar-active-bg` | `rgba(22,119,255,0.2)` | 侧栏选中项背景 |

## 尺寸

| Token | Value | 用途 |
|-------|-------|------|
| `--sidebar-w` | `220px` | 侧栏宽度 |
| `--topbar-h` | `48px` | 顶栏高度 |
| `--radius` | `6px` | 标准圆角（按钮/输入框） |
| `--radius-lg` | `8px` | 大圆角（卡片） |
| `--shadow` | `0 1px 2px rgba(0,0,0,0.06), 0 1px 6px rgba(0,0,0,0.03)` | 卡片阴影 |
| `--shadow-modal` | `0 6px 30px rgba(0,0,0,0.12)` | 模态框阴影 |

## 字体

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
  'Helvetica Neue', Arial, 'Noto Sans', 'PingFang SC', 'Microsoft YaHei', sans-serif;
```

字号规范：正文14px / 表格13px / 标签角标12px（最低）。

## 表格风格

- 表头：`#fafafa` 背景，13px，`font-weight: 500`
- 单元格：上下padding 9px，左右16px
- 分割线：`#f0f0f0`
- 悬停行：`#f5f5f5`

## 按钮风格

```css
.btn-primary   { background: #1677ff; color: #fff; }
.btn-primary:hover { background: #4096ff; }
.btn-success   { background: #52c41a; color: #fff; }
.btn-warning   { background: #fa8c16; color: #fff; }
.btn-danger    { background: #ff4d4f; color: #fff; }
.btn-outline   { background: #fff; color: #1677ff; border: 1px solid #1677ff; }
```

## 用户反馈：从旧风格切换到 Ant Design

用户说"换成阿里的"时执行：
1. 更新 `:root` 中的色彩变量为 Ant Design 值
2. 替换所有 `var(--accent)` → `var(--primary)`
3. 替换 `var(--primary-light)` → `var(--primary-hover)`
4. 替换 `var(--primary-dark)` → `var(--sidebar-bg)`（侧栏专用）
5. 侧栏文本色改为 `var(--sidebar-text)` / `var(--sidebar-text-secondary)`
6. 侧栏悬停改为 `rgba(255,255,255,0.08)`
7. 侧栏选中改为 `var(--sidebar-active-bg)`
8. 表格表头改为 `#fafafa` / 13px / 500字重
