import urllib.request, ssl, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.jjaptoon006.com/',
    'Origin': 'https://www.jjaptoon006.com'
}

for idx in ['1', '0']:
    url = f'https://www.jjaptoon006.com/data/webtoon_{idx}.js'
    try:
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req, context=ctx, timeout=5)
        text = res.read().decode('utf-8', errors='ignore')
        json_text = text.split(' = ', 1)[1].rstrip(';').strip() if ' = ' in text else text
        data = json.loads(json_text)
        for item in data:
            if '화산' in item.get('name', ''):
                sid = item.get('id')
                sname = item.get('name')
                print(f"Found in webtoon_{idx}.js -> ID: {sid}, Name: {sname}")
                ch_url = f"https://www.jjaptoon006.com/data/toonlist/{sid}.js"
                res2 = urllib.request.urlopen(urllib.request.Request(ch_url, headers=headers), context=ctx, timeout=5)
                text2 = res2.read().decode('utf-8', errors='ignore')
                ch_json = json.loads(text2.split(' = ', 1)[1].rstrip(';').strip() if ' = ' in text2 else text2)
                print(f"  Total chapters: {len(ch_json)}")
                print(f"  Top 3 chapter names: {[c.get('n') for c in ch_json[:3]]}")
    except Exception as e:
        print(f"webtoon_{idx}.js err:", e)
