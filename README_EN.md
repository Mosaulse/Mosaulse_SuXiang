# Su Xiang · 素缃

|      |      |      |
| :---: | :---: | :---: |
![ThemeName](https://img.shields.io/badge/%E7%B4%A0%E7%BC%83-Su%20Xiang-%23E6DCC4)|![Theme](https://img.shields.io/badge/Theme-Light%20%7C%20Dark-%23E6DCC4)|![GitHub License](https://img.shields.io/github/license/Mosaulse/suxiang-theme?style=flat&color=%23E6DCC4)
[![VSCode](https://img.shields.io/badge/VSCode-suxiang%20theme-D95B4A?style=flat&color=greenA&logo=visual-studio-code)](https://marketplace.visualstudio.com/items?itemName=Mosaulse.suxiang-theme)|![VSCode Version](https://vsmarketplacebadges.dev/version-short/Mosaulse.suxiang-theme.svg)|![VSCode Downloads](https://vsmarketplacebadges.dev/downloads/Mosaulse.suxiang-theme.svg)
[![OpenVSX](https://img.shields.io/badge/OpenVSX-suxiang%20theme-D95B4A?style=flat&color=%23D95B4A&logo=visual-studio-code)](https://open-vsx.org/extension/Mosaulse/suxiang-theme)|![Open VSX Version](https://img.shields.io/open-vsx/v/Mosaulse/suxiang-theme?style=flat&color=%23D95B4A)|![Open VSX Downloads](https://img.shields.io/open-vsx/dt/Mosaulse/suxiang-theme?style=flat&color=%23D95B4A)

---

[Chinese](README.md)

*The color of an antique hand-copied scroll, cast upon your code.*

**Su Xiang** is a pair of VSCode color themes rooted in the aesthetics of ancient Eastern manuscripts.

"Su" (素) is raw, undyed silk — pure and serene; "Xiang" (缃) is the pale amber aged by time — the hue of an old scroll's flyleaf.

No harsh fluorescent whites, no bottomless blacks. Only the warmth of aged paper, the faded ink of settled time, the deliberate impression of a vermillion seal, and the serene jade-green of celadon headings. Like opening an old book in the afternoon sun or by candlelight — every line of code becomes hushed and warm.

---

## 🎨 Preview

### Suxiang - Light (素缃·朝霞)

> Rise at dawn, unroll the scroll.  
> Morning light on paper, the scent of ink fills the room.  
> Keywords like vermillion seals, function names like blue-and-white porcelain.

<img src="images/screenshot-light.png" alt="Suxiang Light Preview" width="60%" />

### Suxiang - Dark (素缃·暮色)

> Dusk falls, candlelight flickers.  
> Ancient pages yellowed, poetry flows.  
> Code becomes verse, its mood lingering.

<img src="images/screenshot-dark.png" alt="Suxiang Dark Preview" width="60%" />

## 🎨 Four-Symbol Color Palette

This theme follows the traditional Chinese philosophy of the "Four Symbols," building its color system around four classical motifs.

| Symbol | Light Values | Dark Values | Meaning | Role |
|--------|-------------|-------------|---------|------|
| **Raw Silk** (素绢) | `#F3EAD8` `#E6DCC4` | `#261F16` `#1F1912` | Unfurled silk, aged parchment | Editor & sidebar background |
| **Ink** (墨迹) | `#423729` `#7A6D5E` | `#D0C3AE` `#938A7A` | Year-old ink, verse-like strokes | Foreground text & comments |
| **Vermillion** (朱砂) | `#C54131` `#D96C4A` | `#D95B4A` `#E3947C` | Seal impression, deliberate & solemn | Keywords, numbers, status bar |
| **Jade Green** (青碧) | `#1F987C` `#439D88` | `#7DA494` `#9DBFAD` | Jade motif, warm & serene | Title bar, functions, types |

**Design philosophy:** Raw silk as the ground, ink as the text, vermillion to punctuate, jade green to outline — the spirit of calligraphy, the aesthetics of code.

## 📜 Installation

> Unroll the Su Xiang scroll, slowly.  
> Code becomes poetry; the mood comes of itself.

**Method 1: Install within VSCode**
1. Open VSCode
2. Click the **Extensions** icon in the sidebar (`Ctrl+Shift+X`)
3. Search for **Su Xiang**
4. Click **Install**
5. Press `Ctrl+K Ctrl+T` (Mac: `Cmd+K Cmd+T`), and choose **Suxiang - Light** or **Suxiang - Dark**

**Method 2: Marketplace**

Or find this theme directly on the [VSCode Marketplace](https://marketplace.visualstudio.com/).

## ⚙️ Recommended Configuration

> Sharpen your tools for the work ahead.  
> With the right settings, the mood deepens.

For the best classical experience, add these settings to your `settings.json`:

```json
{
  "editor.fontFamily": "'LXGW WenKai Mono', 'Maple Mono NF CN'",
  "editor.fontSize": 15,
  "editor.lineHeight": 1.6,
  "editor.renderWhitespace": "selection",
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": true,
}
```

> ✨ **Special Recommendation**: [**LXGW WenKai (霞鹜文楷)**](https://github.com/lxgw/LxgwWenKai) — an open-source Chinese font based on Klee One, blending the beauty of Kaishu and Fangsong typefaces. Warm, elegant, and perfectly complementing the Su Xiang theme. Download from the [GitHub releases page](https://github.com/lxgw/LxgwWenKai/releases).

## 📚 Language Support

> A single scroll of Su Xiang speaks a thousand tongues.  
> Any language becomes poetic.

This theme relies on standard TextMate semantic tokenization. Especially well-adapted languages include:

**Frontend Trio**: JavaScript · TypeScript · HTML/CSS
**Backend Classics**: Python · Java · C# · Go · Rust
**Data Languages**: SQL · JSON · Markdown
**System Voices**: C/C++ · Shell

> 🎨 No matter the programming language, within Su Xiang it becomes a painting — poetic and timeless.

## 🛠️ Local Development

> To study this scroll in depth, work on it locally.  
> Code is poetry; the mood reveals itself.

```bash
# Clone the scroll
git clone https://github.com/mosaulse/suxiang-theme.git
cd suxiang-theme

# Install dependencies
npm install

# Open VSCode and press F5 to launch an Extension Development Host
code .

# Package for distribution
npx vsce package
```

## 🖋️ Contributing

> A single scroll of Su Xiang is not the work of one.  
> Let us write new chapters together.

Su Xiang was born from the poetic vision of "yellowed paper and vermillion seals." If a syntax highlight could be more fitting, or if you'd like to add finer language support, you're welcome to:

1. Open an [Issue](https://github.com/mosaulse/suxiang-theme/issues) sharing your thoughts
2. Fork this scroll and submit a Pull Request, adding new scopes in `tokenColors`

> 🎨 Colors are also words — we look forward to seeing you add new hues to Su Xiang.

## 📓 Changelog

> At the end of the scroll, we record its changes and new chapters. Here are the recent milestones.

### v1.3.1 — 2026-05-22

**Ink Tuning: semantic highlighting & activity bar**

- Adjusted semantic highlighting: class, interface, type, keyword → italic; comment → back to normal
- Activity bar background unified with sidebar, seamless across light & dark
- Added `git.blame.editorDecorationForeground` — blame annotations like tiny vermillion stamps

### v1.3.0 — 2026-05-09

**Theme Refinements & Structural Enhancements**

- Added `themes/base.json`, extracting shared colors for reuse
- Optimized and tweaked several colors and UI elements in both themes
- Updated `.vscodeignore` and added local scripts for simpler packaging/testing

### v1.2.0 — 2026-05-08

**Refined Atmosphere**

- Added full `semanticTokenColors` configuration for modern language semantic highlighting
- Improved highlighting for namespace, class, interface, enum, etc.
- Added standalone colors for function, method, macro — method calls are now more distinct
- Enhanced color distinction among variable, parameter, property for clearer code layering
- Improved syntax highlighting for regex, Markdown, CSS, etc.

### v1.1.0 — 2026-05-07

**Elevated Mood**

- Revisited the Four-Symbol color philosophy — raw silk, ink, vermillion, and blue-and-white are now more harmoniously unified
- Optimized the light theme's raw silk background — warm like first-snow rice paper
- Adjusted the dark theme's ink levels for a deeper antique-scroll atmosphere
- Improved syntax highlighting — strings, comments, variables are more clearly distinguished
- Polished UI details — activity bar, sidebar, and more are visually refined

### v1.0.1 — 2026-05-06

**Mood Optimization**

- Optimized editor selection background and highlight colors for better visuals
- Adjusted title bar colors, added borders for clearer layering
- Added debug status bar colors for clearer debug state indication
- Added no-folder-open status bar colors for distinct interface states
- Unified the light/dark theme color system for a more harmonious experience

See full details in [CHANGELOG.md](./CHANGELOG.md)

## 📜 License

MIT License © Mosaulse

---

> A scroll of Su Xiang — the scent of ink for a thousand years.  
> Code becomes poetry; the mood is tranquil.  
> May you always have a sheet of Su Xiang beside you in the world of code.

---

**Poetic References**:
- *Classic of Poetry* — "White silk, five twists"
- *Songs of Chu* — "A xiang-colored silk skirt"
- Traditional Four-Symbol philosophy
- Classical Chinese aesthetic imagery
