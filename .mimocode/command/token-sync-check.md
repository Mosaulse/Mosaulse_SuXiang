---
description: 检查主题文件中 tokenColors 与 semanticTokenColors 的前景色是否同步
---

# 语义同步检查

检查指定主题文件中 `tokenColors` 和 `semanticTokenColors` 的对应 scope 前景色是否一致。

## 背景

修改 `tokenColors` 后，`semanticTokenColors` 中对应 scope 也需同步更新，否则语义高亮会覆盖语法高亮，导致实际显示颜色与预期不符。

## 输入

- `$1` — 主题文件路径（如 `themes/dawn-suxiang.json`）

## 执行步骤

### 1. 读取主题文件

读取 `$1` 指定的 JSON 文件，提取：
- `tokenColors` 数组：每个条目有 `scope`（字符串数组）和 `settings.foreground`
- `semanticTokenColors` 对象：每个 key 是语义 token 类型，value 含 `foreground`

### 2. 建立映射关系

以下是 tokenColors scope 与 semanticTokenColors key 的对应关系：

| tokenColors scope | semanticTokenColors key |
|:---|:---|
| `keyword` | `keyword` |
| `string` | `string` |
| `comment` | `comment` |
| `variable` | `variable` |
| `variable.parameter` | `parameter` |
| `entity.name.function` | `function` |
| `entity.name.class`, `entity.name.type` | `class`, `type` |
| `support.type` | `type` |
| `constant.numeric` | `number` |
| `constant.language` | `variable` |
| `entity.name.tag` | `type`（归入类型色） |
| `support.type.property-name.json` | `property`（归入属性色） |
| `entity.other.attribute-name.class.css` | `type`（归入类型色） |

### 3. 比较前景色

对每对映射，比较 `tokenColors` 中的 `settings.foreground` 与 `semanticTokenColors` 中的 `foreground`。

### 4. 输出格式

```
## 语义同步报告 — {主题名}

| Scope | tokenColors 色 | semanticTokenColors 色 | 状态 |
|:---|:---|:---|:---|
| keyword | #B83A2B | #B83A2B | ✅ 同步 |
| comment | #756858 | #A29583 | ❌ 不同步 |
| ... | ... | ... | ... |

### 汇总
- 同步: N 项
- 不同步: N 项（需修复）
```

### 5. 修复建议

对不同步项，建议将 `semanticTokenColors` 的前景色更新为与 `tokenColors` 一致。

## 停止条件

报告输出完毕，列出所有不同步项。
