import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

url = "https://newtoki1.org/webtoon/769209"
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req, context=ctx, timeout=8)
html = res.read().decode('utf-8', errors='ignore')

# Print scripts or HTML structure
print("HTML length:", len(html))
print("Contains list-body:", "list-body" in html)
print("Contains serial-list:", "serial-list" in html)
print("Contains episode:", "episode" in html)
print("Contains 173화:", "173화" in html)
print("Contains 171화:", "171화" in html)

matches = [m.start() for m in re.finditer(r'173화', html)]
for idx in matches[:3]:
    print("\nSnippet around 173화:")
    print(html[max(0, idx-100):min(len(html), idx+200)])
