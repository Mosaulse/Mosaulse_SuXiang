# Theme Naming Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use compose:subagent (recommended) or compose:execute to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign all theme naming system: file names (lowercase-hyphen English), display names (poetic-series format), and fix package.json inconsistencies.

**Architecture:** Rename 6 theme JSON files, update their internal `name` fields, update package.json to reference all themes correctly, and update README documentation.

**Tech Stack:** JSON, Markdown

---

## File Mapping

| Original File | New File | Original Display | New Display |
|---------------|----------|------------------|-------------|
| `themes/Suxiang-Light.json` | `themes/dawn-suxiang.json` | 素缃·朝霞 | 朝霞·素缃 |
| `themes/Suxiang-Dark.json` | `themes/dusk-suxiang.json` | 素缃·暮色 | 暮色·素缃 |
| `themes/Zixiang-Light.json` | `themes/dawnmist-zixiang.json` | 紫缃·晓烟 | 晓烟·紫缃 |
| `themes/Zixiang-Dark.json` | `themes/candlelight-zixiang.json` | 紫缃·烛影 | 烛影·紫缃 |
| `themes/ClearLotus-Light.json` | `themes/morningdew-fuqu.json` | 菡萏·清莲 | 晨露·芙蕖 |
| `themes/LotusShadow-Dark.json` | `themes/moonshadow-fuqu.json` | 菡萏·荷影 | 月影·芙蕖 |

---

### Task 1: Rename Theme Files and Update Display Names

**Covers:** All naming changes

**Files:**
- Rename: `themes/Suxiang-Light.json` → `themes/dawn-suxiang.json`
- Rename: `themes/Suxiang-Dark.json` → `themes/dusk-suxiang.json`
- Rename: `themes/Zixiang-Light.json` → `themes/dawnmist-zixiang.json`
- Rename: `themes/Zixiang-Dark.json` → `themes/candlelight-zixiang.json`
- Rename: `themes/ClearLotus-Light.json` → `themes/morningdew-fuqu.json`
- Rename: `themes/LotusShadow-Dark.json` → `themes/moonshadow-fuqu.json`

- [ ] **Step 1: Rename Suxiang-Light.json**

```bash
cd D:\Documents\MyToys\suxiang-theme
git mv themes/Suxiang-Light.json themes/dawn-suxiang.json
```

- [ ] **Step 2: Update display name in dawn-suxiang.json**

Edit `themes/dawn-suxiang.json`, change line 3:
```json
"name": "朝霞·素缃",
```

- [ ] **Step 3: Rename Suxiang-Dark.json**

```bash
git mv themes/Suxiang-Dark.json themes/dusk-suxiang.json
```

- [ ] **Step 4: Update display name in dusk-suxiang.json**

Edit `themes/dusk-suxiang.json`, change line 3:
```json
"name": "暮色·素缃",
```

- [ ] **Step 5: Rename Zixiang-Light.json**

```bash
git mv themes/Zixiang-Light.json themes/dawnmist-zixiang.json
```

- [ ] **Step 6: Update display name in dawnmist-zixiang.json**

Edit `themes/dawnmist-zixiang.json`, change line 3:
```json
"name": "晓烟·紫缃",
```

- [ ] **Step 7: Rename Zixiang-Dark.json**

```bash
git mv themes/Zixiang-Dark.json themes/candlelight-zixiang.json
```

- [ ] **Step 8: Update display name in candlelight-zixiang.json**

Edit `themes/candlelight-zixiang.json`, change line 3:
```json
"name": "烛影·紫缃",
```

- [ ] **Step 9: Rename ClearLotus-Light.json**

```bash
git mv themes/ClearLotus-Light.json themes/morningdew-fuqu.json
```

- [ ] **Step 10: Update display name in morningdew-fuqu.json**

Edit `themes/morningdew-fuqu.json`, change line 3:
```json
"name": "晨露·芙蕖",
```

- [ ] **Step 11: Rename LotusShadow-Dark.json**

```bash
git mv themes/LotusShadow-Dark.json themes/moonshadow-fuqu.json
```

- [ ] **Step 12: Update display name in moonshadow-fuqu.json**

Edit `themes/moonshadow-fuqu.json`, change line 3:
```json
"name": "月影·芙蕖",
```

---

### Task 2: Update package.json

**Covers:** Fix package.json theme references

**Files:**
- Modify: `package.json`

- [ ] **Step 1: Update contributes.themes in package.json**

Replace the `contributes.themes` array in `package.json`:

```json
"contributes": {
    "themes": [
      {
        "label": "朝霞·素缃",
        "uiTheme": "vs",
        "path": "./themes/dawn-suxiang.json"
      },
      {
        "label": "暮色·素缃",
        "uiTheme": "vs-dark",
        "path": "./themes/dusk-suxiang.json"
      },
      {
        "label": "晓烟·紫缃",
        "uiTheme": "vs",
        "path": "./themes/dawnmist-zixiang.json"
      },
      {
        "label": "烛影·紫缃",
        "uiTheme": "vs-dark",
        "path": "./themes/candlelight-zixiang.json"
      },
      {
        "label": "晨露·芙蕖",
        "uiTheme": "vs",
        "path": "./themes/morningdew-fuqu.json"
      },
      {
        "label": "月影·芙蕖",
        "uiTheme": "vs-dark",
        "path": "./themes/moonshadow-fuqu.json"
      }
    ]
  }
```

---

### Task 3: Update README.md

**Covers:** Update documentation with new names

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update theme preview section headings**

In `README.md`, update the following sections:

- Line 38: `### 素缃 · 朝霞（Suxiang — Light）` → `### 朝霞 · 素缃（Dawn — Suxiang）`
- Line 46: `### 素缃 · 暮色（Suxiang — Dark）` → `### 暮色 · 素缃（Dusk — Suxiang）`
- Line 54: `### 紫缃 · 晓烟（Zixiang — Light）` → `### 晓烟 · 紫缃（Dawnmist — Zixiang）`
- Line 60: `### 紫缃 · 烛影（Zixiang — Dark）` → `### 烛影 · 紫缃（Candlelight — Zixiang）`

- [ ] **Step 2: Add 芙蕖 theme previews**

Add two new sections after the 紫缃 previews:

```markdown
### 晨露 · 芙蕖（Morning Dew — Fuqu）

> 晨露初凝，芙蕖含苞。
> 清新如晨，碧叶承珠。

> *（预览图待补充）*

### 月影 · 芙蕖（Moon Shadow — Fuqu）

> 月影斜照，芙蕖静谧。
> 夜色如水，暗香浮动。

> *（预览图待补充）*
```

- [ ] **Step 3: Update installation guide**

In line 94, update the theme selection list:
```
择 **朝霞·素缃**、**暮色·素缃**、**晓烟·紫缃**、**烛影·紫缃**、**晨露·芙蕖** 或 **月影·芙蕖**
```

---

### Task 4: Verify Changes

**Covers:** Validation

- [ ] **Step 1: List themes directory**

```bash
ls D:\Documents\MyToys\suxiang-theme\themes\
```

Expected output should show:
```
base.json
candlelight-zixiang.json
dawn-suxiang.json
dawnmist-zixiang.json
dusk-suxiang.json
morningdew-fuqu.json
moonshadow-fuqu.json
```

- [ ] **Step 2: Verify JSON validity**

```bash
cd D:\Documents\MyToys\suxiang-theme
python -c "import json; [json.load(open(f'themes/{f}')) for f in ['dawn-suxiang.json', 'dusk-suxiang.json', 'dawnmist-zixiang.json', 'candlelight-zixiang.json', 'morningdew-fuqu.json', 'moonshadow-fuqu.json', 'package.json']]"
```

Expected: No output (all files are valid JSON)

- [ ] **Step 3: Commit changes**

```bash
cd D:\Documents\MyToys\suxiang-theme
git add -A
git commit -m "refactor: 重新设计主题命名系统

- 统一文件名为全小写连字符格式
- 显示名改为「诗意·系列」格式
- 菡萏更名为芙蕖
- 修正 package.json 主题引用
- 更新 README 文档"
```
