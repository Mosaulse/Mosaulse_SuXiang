import urllib.request
import json
import sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Fetch all colors from zhongguose.com API
url = 'https://zhongguose.com/api/colors'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as response:
    data = json.loads(response.read().decode('utf-8'))

# Build lookup by hex (case-insensitive)
color_map = {}
for item in data:
    hex_val = item['hex'].lower()
    color_map[hex_val] = {
        'name': item['name'],
        'pinyin': item['pinyin'],
        'hex': item['hex'],
        'rgb': item['RGB']
    }

# Our colors to check
our_colors = [
    '#157558', '#256F5E', '#423729', '#5A8A78', '#5F5548',
    '#756050', '#756858', '#7DA494', '#7E6B5C', '#924D78',
    '#938A7A', '#9A8878', '#A29583', '#B04830', '#B83A2B',
    '#C49BB2', '#C54131', '#C5B79F', '#D0C3AE', '#D95B4A',
    '#D96C4A', '#E3947C'
]

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def color_distance(c1, c2):
    r1, g1, b1 = hex_to_rgb(c1)
    r2, g2, b2 = hex_to_rgb(c2)
    return ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2) ** 0.5

print('=== Exact matches ===')
matched = []
unmatched = []
for c in our_colors:
    key = c.lower()
    if key in color_map:
        info = color_map[key]
        matched.append((c, info))
        print(f'  {c} -> {info["name"]} ({info["pinyin"]})')
    else:
        unmatched.append(c)
        print(f'  {c} -> NOT FOUND')

print(f'\nMatched: {len(matched)}/{len(our_colors)}')

if unmatched:
    print('\n=== Closest matches (distance < 15) ===')
    for c in unmatched:
        distances = []
        for hex_val in color_map:
            dist = color_distance(c, hex_val)
            distances.append((dist, hex_val, color_map[hex_val]))
        distances.sort()
        # Show top 3 closest
        print(f'\n  {c}:')
        for dist, hex_val, info in distances[:3]:
            marker = ' *' if dist < 15 else ''
            print(f'    d={dist:.1f} {hex_val} {info["name"]} ({info["pinyin"]}){marker}')
