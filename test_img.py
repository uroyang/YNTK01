import urllib.request, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://blacktoon419.com/',
    'Origin': 'https://blacktoon419.com'
}

test_urls = [
    'https://yh072c.speedwebgo.com/2020/1117/20201117015655724.jpg',
    'https://ne.speedwebgo.com/2020/1117/20201117015655724.jpg',
    'https://blacktoon419.com/2020/1117/20201117015655724.jpg'
]

for u in test_urls:
    t0 = time.time()
    try:
        req = urllib.request.Request(u, headers=headers)
        res = urllib.request.urlopen(req, context=ctx, timeout=5)
        body = res.read(1024)
        elapsed = time.time() - t0
        print(f"{u:65} -> Status: {res.getcode()}, Time: {elapsed:.2f}s, Len: {len(body)}")
    except Exception as e:
        elapsed = time.time() - t0
        print(f"{u:65} -> ERROR after {elapsed:.2f}s: {e}")
