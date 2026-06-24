---
name: theme-compliance-audit
description: 审查所有主题文件是否符合 AGENTS.md 规则（include 机制、颜色数量、传统色来源、对比度）
---

# 主题合规审查

对 themes/ 目录下所有主题文件执行 AGENTS.md 合规检查，输出结构化报告。

## 前置条件

- 项目根目录存在 `themes/` 目录，含 `base.json` 及若干主题 JSON
- 项目根目录存在 `AGENTS.md`（设计总纲）
- Python 3 可用（用于颜色提取和色距计算）

## 审查步骤

### 1. include 机制检查

对每个主题文件（排除 base.json）：

- 验证第二行为 `"include": "./base.json"`
- 若缺失或位置不对，报告违规

可用 `apply_include_and_clean.py` 自动修复：

```bash
python scripts/apply_include_and_clean.py
```

### 2. 颜色数量检查（繁简有度规则）

对每个主题文件，统计 `tokenColors` 和 `semanticTokenColors` 中所有独立 `foreground` 色值数量：

- 高频色（关键字、函数、变量、类型）：5-7 种以内
- 低频色（字符串、注释、数字等）：复用高频色或合并相近色
- 总独立前景色不超过 7 种为达标

提取方法：遍历 `tokenColors[].settings.foreground` 和 `semanticTokenColors[*].foreground`，去重统计。

### 3. 传统色来源检查

将每个主题的前景色与 zhongguose.com 数据对比：

- 精确匹配（色距 = 0）：最优
- 接近匹配（色距 ≤ 15）：可接受
- 不匹配（色距 > 15）：建议替换为最近的传统色

可用已有的色距计算脚本：

```bash
python scripts/match_colors_v2.py
```

### 4. WCAG 对比度检查

对每个前景色，计算其与主题背景色的对比度：

- 正文文字：≥ 4.5:1（AA 标准）
- 大字标题：≥ 3:1

背景色从主题 `colors.editor.background` 或 `colors.sideBarBackground` 获取。

### 5. 结构一致性检查

- 确认所有主题的 `tokenColors` 使用一致的 scope 粒度（芙蕖系为展开式，素缃/紫缃系为简洁式——差异可接受但需记录）
- 确认 `semanticHighlighting` 值一致（通过 base.json 继承或显式声明）

## 输出格式

对每个主题输出一行状态表：

```
| 主题 | 类型 | 前景色数 | include | 传统色匹配 | 对比度 | 状态 |
```

状态判定：
- ✅ 达标：include 正确、颜色 ≤ 7、所有色有传统色来源、对比度达标
- ⚠️ 注意：颜色 8 种（接近上限）或个别色距 >15
- ❌ 超标：颜色 >7 种或对比度不达标

## 停止条件

全部主题审查完毕，输出汇总表和建议优化方向。
