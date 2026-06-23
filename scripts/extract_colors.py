import json, re

def extract_colors(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    colors = set()
    tc_start = content.find('"tokenColors"')
    stc_start = content.find('"semanticTokenColors"')
    if tc_start != -1:
        section = content[tc_start:]
        hex_colors = re.findall(r'"#([0-9A-Fa-f]{6})"', section)
        colors.update(hex_colors)
    if stc_start != -1:
        section = content[stc_start:]
        hex_colors = re.findall(r'"#([0-9A-Fa-f]{6})"', section)
        colors.update(hex_colors)
    return sorted(colors)

dawn = extract_colors('themes/dawn-suxiang.json')
dusk = extract_colors('themes/dusk-suxiang.json')

print('=== Dawn ===')
for c in dawn:
    print(f'  #{c}')

print()
print('=== Dusk ===')
for c in dusk:
    print(f'  #{c}')

print()
all_colors = sorted(set(dawn + dusk))
print(f'=== Total unique: {len(all_colors)} ===')
for c in all_colors:
    in_dawn = c in dawn
    in_dusk = c in dusk
    tag = 'Both' if (in_dawn and in_dusk) else ('Dawn' if in_dawn else 'Dusk')
    print(f'  #{c}  [{tag}]')
