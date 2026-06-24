import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = ROOT / 'themes'
BASE_PATH = THEMES / 'base.json'
LIGHT = THEMES / 'dawn-suxiang.json'
DARK = THEMES / 'dusk-suxiang.json'

with BASE_PATH.open('r', encoding='utf-8') as f:
    base = json.load(f) or {}

def remove_matching(base_val, theme_val):
    # returns cleaned theme_val or None if should remove entirely
    if base_val is None:
        return theme_val
    if isinstance(base_val, dict) and isinstance(theme_val, dict):
        tv = dict(theme_val)
        for k, bv in base_val.items():
            if k in tv:
                new = remove_matching(bv, tv[k])
                if new is None:
                    tv.pop(k, None)
                else:
                    tv[k] = new
        return tv if tv else None
    if isinstance(base_val, list) and isinstance(theme_val, list):
        # For lists, attempt element-wise cleaning; if lengths differ, skip
        if len(base_val) != len(theme_val):
            return theme_val
        cleaned = []
        changed = False
        for bv, tv in zip(base_val, theme_val):
            new = remove_matching(bv, tv)
            cleaned.append(new if new is not None else None)
            if new != tv:
                changed = True
        return cleaned if any(x is not None for x in cleaned) else None
    # primitive
    if base_val == theme_val:
        return None
    return theme_val


def clean_theme(theme_path: Path):
    with theme_path.open('r', encoding='utf-8') as f:
        theme = json.load(f)

    # ensure include
    theme_changed = False
    rel_base = './' + BASE_PATH.name
    if theme.get('include') != rel_base:
        theme['include'] = rel_base
        theme_changed = True

    # Clean semanticTokenColors (object)
    if 'semanticTokenColors' in base and isinstance(base['semanticTokenColors'], dict):
        if 'semanticTokenColors' in theme and isinstance(theme['semanticTokenColors'], dict):
            for key, bval in base['semanticTokenColors'].items():
                if key in theme['semanticTokenColors']:
                    tval = theme['semanticTokenColors'][key]
                    new = remove_matching(bval, tval)
                    if new is None:
                        theme['semanticTokenColors'].pop(key, None)
                        theme_changed = True
                    elif new != tval:
                        theme['semanticTokenColors'][key] = new
                        theme_changed = True
            if not theme['semanticTokenColors']:
                theme.pop('semanticTokenColors', None)

    # Clean colors
    if 'colors' in base and isinstance(base['colors'], dict):
        if 'colors' in theme and isinstance(theme['colors'], dict):
            for key, bval in list(base['colors'].items()):
                if key in theme['colors'] and theme['colors'][key] == bval:
                    theme['colors'].pop(key, None)
                    theme_changed = True
            if not theme['colors']:
                theme.pop('colors', None)

    # Clean tokenColors (array of rules)
    if 'tokenColors' in base and isinstance(base['tokenColors'], list):
        if 'tokenColors' in theme and isinstance(theme['tokenColors'], list):
            # For each base rule try find matching rule in theme by name+scope
            for b_rule in base['tokenColors']:
                b_name = b_rule.get('name')
                b_scope = b_rule.get('scope')
                b_settings = b_rule.get('settings', {})
                for t_rule in theme['tokenColors']:
                    if t_rule.get('name') == b_name and t_rule.get('scope') == b_scope:
                        # remove matching settings keys
                        t_settings = t_rule.get('settings', {})
                        for sk, sv in list(b_settings.items()):
                            if sk in t_settings and t_settings[sk] == sv:
                                t_settings.pop(sk, None)
                                theme_changed = True
                        if t_settings:
                            t_rule['settings'] = t_settings
                        else:
                            # remove settings entirely so include supplies it
                            t_rule.pop('settings', None)
            # remove any token rule that became empty (no settings and no other meaningful keys)
            new_token_colors = []
            for r in theme['tokenColors']:
                # keep rule if has settings or has other properties besides name/scope
                keys = set(r.keys()) - {'name', 'scope'}
                if 'settings' in r or keys:
                    new_token_colors.append(r)
                else:
                    theme_changed = True
            if new_token_colors:
                theme['tokenColors'] = new_token_colors
            else:
                theme.pop('tokenColors', None)

    # semanticHighlighting / semationicHighlighting typo handling
    for key in ['semanticHighlighting', 'semationicHighlighting']:
        if key in base:
            if key in theme and theme[key] == base[key]:
                theme.pop(key, None)
                theme_changed = True

    if theme_changed:
        with theme_path.open('w', encoding='utf-8') as f:
            json.dump(theme, f, indent=4, ensure_ascii=False)
        print(f'Cleaned {theme_path.name}')
    else:
        print(f'No changes for {theme_path.name}')


if __name__ == '__main__':
    for theme_file in sorted(THEMES.glob('*.json')):
        if theme_file.name == BASE_PATH.name:
            continue
        clean_theme(theme_file)
