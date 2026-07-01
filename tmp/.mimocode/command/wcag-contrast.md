---
description: 计算主题文件中所有前景色的 WCAG 对比度，输出合规报告
---

# WCAG 对比度计算

对指定主题文件执行 WCAG AA 对比度审计。

## 输入

- `$1` — 主题文件路径（如 `themes/dawn-suxiang.json`）
- 可选：背景色覆盖（默认从 `colors.editor.background` 读取）

## 执行步骤

### 1. 读取主题文件

读取 `$1` 指定的 JSON 文件，提取：
- 背景色：`colors.editor.background`（若无则用 `colors.sideBarBackground`）
- 所有前景色：遍历 `tokenColors[].settings.foreground` 和 `semanticTokenColors[*].foreground`

### 2. 计算对比度

对每个前景色，运行以下 Python 代码计算与背景色的 WCAG 相对亮度和对比度：

```python
import json, sys

def srgb_to_linear(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def relative_luminance(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return 0.2126 * srgb_to_linear(r) + 0.7152 * srgb_to_linear(g) + 0.0722 * srgb_to_linear(b)

def contrast_ratio(color1, color2):
    l1 = relative_luminance(color1)
    l2 = relative_luminance(color2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

# 用法：contrast_ratio(前景色, 背景色)
```

### 3. 判定标准

| 用途 | 最低对比度 | 标准 |
|:---|:---|:---|
| 正文文字 | ≥ 4.5:1 | WCAG AA |
| 大字标题（≥18pt 或 ≥14pt bold） | ≥ 3:1 | WCAG AA |

### 4. 输出格式

```
## WCAG 对比度报告 — {主题名}

背景色: #{hex}

| 前景色 | 来源 | 对比度 | 判定 |
|:---|:---|:---|:---|
| #423729 | 正文/变量 | 9.71:1 | ✅ PASS |
| #756858 | 注释 | 4.53:1 | ✅ PASS |
| #B83A2B | 关键字 | 4.78:1 | ✅ PASS |
| ... | ... | ... | ... |

### 汇总
- PASS: N 项
- FAIL: N 项（需加深色值）
- WARN: N 项（接近阈值）
```

### 5. 修复建议

对 FAIL 项，建议加深前景色以达到 4.5:1。可参考 zhongguose.com 选取更暗的传统色。

## 停止条件

报告输出完毕，列出所有不达标项及修复建议。
