import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

sources = [
    ("YNTK (Newtoki)", "https://newtoki1.org/webtoon/769209"),
    ("YWOLF (Wolf)", "https://wfwf481.com/list?toon=5973"),
    ("YJJAPTOON (Jjaptoon)", "https://www.jjaptoon006.com/data/toonlist/12630.js"),
    ("YToonkor (Toonkor)", "https://tkor145.com/webtoon/769209.html")
]

for name, url in sources:
    try:
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req, context=ctx, timeout=5)
        html = res.read().decode('utf-8', errors='ignore')
        print(f"[{name}] -> Status: {res.getcode()}, Length: {len(html)}")
    except Exception as e:
        print(f"[{name}] -> ERROR: {e}")
