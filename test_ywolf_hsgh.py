import urllib.request, ssl, re, sys

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

url = "https://wfwf481.com/list?toon=5973"
res_d = urllib.request.urlopen(urllib.request.Request(url, headers=headers), context=ctx, timeout=8)
html_d = res_d.read().decode('utf-8', errors='ignore')

links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html_d, re.DOTALL)
print("Total links on page:", len(links))

episode_links = [l for l in links if 'v=' in l[0] or 'view' in l[0] or 'id=' in l[0]]
print("Episode links found:", len(episode_links))
for href, text in episode_links[:10]:
    clean = re.sub(r'<[^>]+>', '', text).strip()
    clean = ' '.join(clean.split())
    print(f" - href: {href:30} | text: {clean}")
