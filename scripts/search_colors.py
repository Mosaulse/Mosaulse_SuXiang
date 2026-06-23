import urllib.request
import json
import re

colors = [
    '#157558', '#256F5E', '#423729', '#5A8A78', '#5F5548',
    '#756050', '#756858', '#7DA494', '#7E6B5C', '#924D78',
    '#938A7A', '#9A8878', '#A29583', '#B04830', '#B83A2B',
    '#C49BB2', '#C54131', '#C5B79F', '#D0C3AE', '#D95B4A',
    '#D96C4A', '#E3947C'
]

# Try to fetch the zhongguose.com color list
# The website uses an API endpoint
url = 'https://zhongguose.com/api/colors'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
        print(f'Got {len(data)} colors from API')
        # Print first few entries to understand structure
        for item in data[:3]:
            print(json.dumps(item, ensure_ascii=False, indent=2))
except Exception as e:
    print(f'API failed: {e}')
    print('Trying alternative approach...')
