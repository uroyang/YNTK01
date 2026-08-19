import urllib.request, ssl, re, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

print("=== 1. YNTK (Newtoki) ===")
try:
    url = "https://newtoki1.org/webtoon/769209"
    res = urllib.request.urlopen(urllib.request.Request(url, headers=headers), context=ctx, timeout=8)
    html = res.read().decode('utf-8', errors='ignore')
    m_title = re.search(r'<meta property="og:title" content=["\']([^"\']+)["\']', html)
    print("Newtoki Title:", m_title.group(1) if m_title else "N/A")
    items = re.findall(r'<a[^>]*class=["\']item-subject[^"\']*["\'][^>]*>(.*?)</a>', html, re.DOTALL)
    print("Newtoki total chapters:", len(items))
    print("Newtoki top 5 chapter names:")
    for it in items[:5]:
        clean = re.sub(r'<[^>]+>', '', it).strip()
        print("  -", clean)
except Exception as e:
    print("Newtoki err:", e)

print("\n=== 2. YWOLF (Wolf) ===")
try:
    url = "https://wfwf481.com/v/comic/769209" # or search
    url_search = "https://wfwf481.com/v/search?stx=" + urllib.parse.quote("화산귀환")
    res = urllib.request.urlopen(urllib.request.Request(url_search, headers=headers), context=ctx, timeout=8)
    html = res.read().decode('utf-8', errors='ignore')
    titles = re.findall(r'<div[^>]*class=["\']title[^"\']*["\'][^>]*>(.*?)</div>', html, re.DOTALL)
    print("Wolf Search Titles:", [re.sub(r'<[^>]+>', '', t).strip() for t in titles if "화산" in t])
except Exception as e:
    print("Wolf err:", e)

print("\n=== 3. YJJAPTOON (Jjaptoon) ===")
try:
    url = "https://www.jjaptoon006.com/data/webtoon_1.js"
    res = urllib.request.urlopen(urllib.request.Request(url, headers=headers), context=ctx, timeout=8)
    text = res.read().decode('utf-8', errors='ignore')
    json_text = text.split(" = ", 1)[1].rstrip(";").strip() if " = " in text else text
    data = json.loads(json_text)
    for d in data:
        if "화산" in d.get("name", ""):
            print("Jjaptoon Title:", d.get("name"), "ID:", d.get("id"))
            ch_url = f"https://www.jjaptoon006.com/data/toonlist/{d.get('id')}.js"
            res2 = urllib.request.urlopen(urllib.request.Request(ch_url, headers=headers), context=ctx, timeout=8)
            t2 = res2.read().decode('utf-8', errors='ignore')
            j2 = json.loads(t2.split(" = ", 1)[1].rstrip(";").strip() if " = " in t2 else t2)
            print("Jjaptoon total chapters:", len(j2))
            print("Jjaptoon top 5 chapter names:")
            for c in j2[:5]:
                print("  -", c.get("n"))
except Exception as e:
    print("Jjaptoon err:", e)

print("\n=== 4. YToonkor (Toonkor / tkor145) ===")
try:
    url = "https://tkor145.com/webtoon" # search
    req = urllib.request.Request("https://tkor145.com/bbs/search.php?stx=" + urllib.parse.quote("화산귀환"), headers=headers)
    res = urllib.request.urlopen(req, context=ctx, timeout=8)
    html = res.read().decode('utf-8', errors='ignore')
    titles = re.findall(r'<div[^>]*class=["\']title[^"\']*["\'][^>]*>(.*?)</div>', html, re.DOTALL)
    print("Toonkor Search Titles:", [re.sub(r'<[^>]+>', '', t).strip() for t in titles if "화산" in t])
except Exception as e:
    print("Toonkor err:", e)
