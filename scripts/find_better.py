import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://zhongguose.com/api/colors'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as response:
    data = json.loads(response.read().decode('utf-8'))

color_map = {}
for item in data:
    hex_val = item['hex'].lower()
    color_map[hex_val] = {
        'name': item['name'],
        'pinyin': item['pinyin'],
        'hex': item['hex']
    }

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def color_distance(c1, c2):
    r1, g1, b1 = hex_to_rgb(c1)
    r2, g2, b2 = hex_to_rgb(c2)
    return ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2) ** 0.5

def find_closest(hex_val, n=5):
    distances = []
    for zh_hex, info in color_map.items():
        dist = color_distance(hex_val, zh_hex)
        distances.append((dist, zh_hex, info))
    distances.sort()
    return distances[:n]

# Check D95B4A (Dusk keyword)
print('=== #D95B4A (Dusk keyword) candidates ===')
for dist, zh_hex, info in find_closest('#D95B4A'):
    print(f'  d={dist:.1f} {zh_hex} {info["name"]} ({info["pinyin"]})')

print()

# Check E3947C (Dusk string)
print('=== #E3947C (Dusk string) candidates ===')
for dist, zh_hex, info in find_closest('#E3947C'):
    print(f'  d={dist:.1f} {zh_hex} {info["name"]} ({info["pinyin"]})')

print()

# Also check if we can find exact matches for D95B4A and E3947C
# by searching in the red/orange family
print('=== All red/orange colors in zhongguose.com (R > 180, G < 120) ===')
target = '#D95B4A'
tr, tg, tb = hex_to_rgb(target)
candidates = []
for zh_hex, info in color_map.items():
    r, g, b = hex_to_rgb(zh_hex)
    if r > 180 and g < 120 and b < 120:
        dist = color_distance(target, zh_hex)
        candidates.append((dist, zh_hex, info))
candidates.sort()
for dist, zh_hex, info in candidates[:10]:
    print(f'  d={dist:.1f} {zh_hex} {info["name"]} ({info["pinyin"]})')
