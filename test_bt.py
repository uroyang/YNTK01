import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://blacktoon419.com/',
    'Origin': 'https://blacktoon419.com'
}

try:
    req = urllib.request.Request('https://ne.speedwebgo.com/data/toonlist/1.js', headers=headers)
    res = urllib.request.urlopen(req, context=ctx, timeout=5)
    text = res.read().decode('utf-8')
    m = re.search(r'"u":"([^"]+)"', text)
    ch_url = m.group(1).replace('\\', '') if m else ''
    print("Found chapter URL:", ch_url)

    if ch_url:
        full_url = 'https://ne.speedwebgo.com' + ch_url
        req2 = urllib.request.Request(full_url, headers=headers)
        res2 = urllib.request.urlopen(req2, context=ctx, timeout=5)
        html = res2.read().decode('utf-8')
        print("Chapter HTML length:", len(html))

        imgs = re.findall(r'<img[^>]+(?:src|o_src|data-src|data-original)=["\']([^"\']+)["\']', html)
        print("Sample image URLs:")
        for img in imgs[:15]:
            print(" -", img)
except Exception as e:
    print("Error:", e)
