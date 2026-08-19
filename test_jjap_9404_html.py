import urllib.request, ssl, re, sys

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = "https://www.jjaptoon006.com/comics/9404"
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req, context=ctx, timeout=5)
html = res.read().decode('utf-8', errors='ignore')
print("Page length:", len(html))

# Find chapter links or titles
chapters = re.findall(r'href=["\']([^"\']*/chapters/\d+[^"\']*)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
print("Chapters found on page:", len(chapters))
for href, text in chapters[:10]:
    clean = re.sub(r'<[^>]+>', '', text).strip()
    clean = ' '.join(clean.split())
    print(f" - href: {href:30} | text: {clean}")
