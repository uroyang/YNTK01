import urllib.request, ssl, re, urllib.parse, sys

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

url = 'https://www.jjaptoon006.com/search?q=' + urllib.parse.quote('화산귀환')
try:
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, context=ctx, timeout=5)
    html = res.read().decode('utf-8', errors='ignore')
    print('Search HTML len:', len(html))
    links = re.findall(r'href=["\']([^"\']*)["\']', html)
    comic_links = [l for l in set(links) if 'comic' in l or 'toon' in l or 'webtoon' in l or 'work' in l]
    print('Comic links found:', comic_links[:10])
except Exception as e:
    print('Search err:', e)
