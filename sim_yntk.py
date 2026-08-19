import urllib.request, ssl, re
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

url = "https://newtoki1.org/webtoon/769209"
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req, context=ctx, timeout=8)
html = res.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
lis = soup.select('.serial-list .list-body li')
print(f"Found {len(lis)} li elements in .serial-list .list-body li")

for index, element in enumerate(lis[:10]):
    a = element.select_one('.wr-subject .item-subject, a[href*="/webtoon/"]')
    if not a:
        continue
    raw_href = a.get('href', '')
    
    # Clone and clean
    # Remove span, small, font, em, i, metrics, badges
    for tag in a.find_all(['span', 'small', 'font', 'em', 'i']):
        tag.decompose()
    
    text = a.get_text().strip()
    text = re.sub(r'(?i)\[\s*(?:up|new)\s*\]|\(\s*(?:up|new)\s*\)', '', text)
    text = re.sub(r'(?i)\b(?:up|new)\b', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Parse chapter number logic
    cnum = -1.0
    m = re.search(r'(?:제\s*)?(\d+(?:\.\d+)?)\s*화', text)
    if m:
        cnum = float(m.group(1))
    
    print(f"#{index+1:2d} | text: '{text:25}' | parsed chapter_number: {cnum} | href: {raw_href}")
