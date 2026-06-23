import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Fetch all colors from zhongguose.com API
url = 'https://zhongguose.com/api/colors'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as response:
    data = json.loads(response.read().decode('utf-8'))

# Build lookup by hex
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

def find_closest(hex_val, n=1):
    distances = []
    for zh_hex, info in color_map.items():
        dist = color_distance(hex_val, zh_hex)
        distances.append((dist, zh_hex, info))
    distances.sort()
    return distances[:n]

# Proposed color mapping with traditional Chinese color names
# Format: (our_hex, proposed_zh_name, zh_pinyin, zh_hex, distance, usage)
proposed = [
    # Dawn colors
    ('#157558', '薄荷绿', 'bohelv', '#207f4c', 'Function'),
    ('#256F5E', '海王绿', 'haiwanglv', '#248067', 'Type'),
    ('#423729', '緇', 'zi', '#3b3131', 'Default fg'),
    ('#5F5548', '燕羽灰', 'yanyuhui', '#685e48', 'Parameter'),
    ('#756050', '鼠背灰', 'shubeihui', '#73575c', 'Property'),
    ('#756858', '鼠背灰', 'shubeihui', '#73575c', 'Comment/Punct'),
    ('#7E6B5C', '烟褐', 'yanhe', '#8b6d5c', '(UI only)'),
    ('#924D78', '芓紫', 'zizi', '#894276', 'Decorator'),
    ('#A29583', '中灰', 'zhonghui', '#a49c93', '(UI only)'),
    ('#B04830', '蟹蝥红', 'xiemaohong', '#b14b28', 'String'),
    ('#B83A2B', '鹅血石红', 'exueshihong', '#ab372f', 'Keyword'),
    ('#C54131', '社红配', 'shehongpei', '#c83737', '(UI error)'),
    ('#D96C4A', '纁色', 'xun', '#d46d3a', '(UI only)'),

    # Dusk colors
    ('#5A8A78', '蛋白石绿', 'danbaishilv', '#579572', 'Type'),
    ('#7DA494', '松霜绿', 'songshuanglv', '#83a78d', 'Function'),
    ('#938A7A', '海鸥灰', 'haiouhui', '#9a8878', 'Comment/Punct'),
    ('#9A8878', '海鸥灰', 'haiouhui', '#9a8878', 'Property (exact!)'),
    ('#C49BB2', '萝兰紫', 'luolanzi', '#c08eaf', 'Decorator'),
    ('#C5B79F', '淡银灰', 'danyinhui', '#c1b2a3', 'Parameter'),
    ('#D0C3AE', '藕丝秋半', 'ousiqiuban', '#d9c6b0', 'Default fg'),
    ('#D95B4A', '纁色', 'xun', '#d46d3a', 'Keyword'),
    ('#E3947C', '淡罂粟红', 'danyingsuhong', '#eea08c', 'String'),
]

print('=== 色名溯源表 ===\n')
print(f'{"我们色值":<10} {"对应色名":<8} {"拼音":<14} {"色谱值":<10} {"距离":<6} {"用途"}')
print('-' * 75)

for hex_val, name, pinyin, zh_hex, usage in proposed:
    dist = color_distance(hex_val, zh_hex)
    exact = ' *EXACT*' if hex_val.lower() == zh_hex.lower() else ''
    print(f'{hex_val:<10} {name:<8} {pinyin:<14} {zh_hex:<10} {dist:<6.1f} {usage}{exact}')

print('\n* 距离 < 15 为佳，15-20 可接受，> 20 需考虑替换为精确色值')
