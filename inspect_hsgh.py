import urllib.request, ssl, re, json, urllib.parse

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

print("=== 1. Checking YNTK (Newtoki) search for 화산귀환 ===")
try:
    url = "https://newtoki1.org/webtoon?stx=" + urllib.parse.quote("화산귀환")
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, context=ctx, timeout=8)
    html = res.read().decode('utf-8', errors='ignore')
    
    # Print titles found in search
    titles = re.findall(r'<span[^>]*class=["\']title["\'][^>]*>(.*?)</span>', html)
    print("Titles found in Newtoki search:", [t.strip() for t in titles if "화산" in t or "귀환" in t])
    
    links = re.findall(r'href=["\'](https?://newtoki1\.org/webtoon/\d+[^"\']*)["\']', html)
    if not links:
        links = re.findall(r'href=["\'](/webtoon/\d+[^"\']*)["\']', html)
        links = ["https://newtoki1.org" + l for l in links]
    print("Newtoki webtoon links found:", list(set(links))[:5])
    
    for wt_url in list(set(links))[:3]:
        print(f"\nFetching Newtoki detail page: {wt_url}")
        res_wt = urllib.request.urlopen(urllib.request.Request(wt_url, headers=headers), context=ctx, timeout=8)
        html_wt = res_wt.read().decode('utf-8', errors='ignore')
        
        wt_title_m = re.search(r'<meta property="og:title" content=["\']([^"\']+)["\']', html_wt)
        print("Page Title:", wt_title_m.group(1) if wt_title_m else "Unknown")
        
        ch_titles = re.findall(r'<a[^>]*class=["\']item-subject[^"\']*["\'][^>]*>(.*?)</a>', html_wt, re.DOTALL)
        if not ch_titles:
            ch_titles = re.findall(r'<li[^>]*class=["\']item[^"\']*["\'][^>]*>.*?<span>(.*?)</span>', html_wt, re.DOTALL)
        print(f"Total chapters found on page: {len(ch_titles)}")
        print("First 10 chapters:")
        for ch in ch_titles[:10]:
            clean_ch = re.sub(r'<[^>]+>', '', ch).strip()
            clean_ch = ' '.join(clean_ch.split())
            print(" -", clean_ch)
except Exception as e:
    import traceback
    traceback.print_exc()

print("\n=== 2. Checking YJJAPTOON (Jjaptoon) search for 화산귀환 ===")
try:
    url = "https://www.jjaptoon006.com/data/webtoon_1.js"
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, context=ctx, timeout=8)
    text = res.read().decode('utf-8', errors='ignore')
    json_text = text.substringAfter(" = ") if " = " in text else text
    if " = " in text:
        json_text = text.split(" = ", 1)[1].rstrip(";").strip()
    data = json.loads(json_text)
    matched = [item for item in data if "화산" in item.get("name", "") and "귀환" in item.get("name", "")]
    print(f"Jjaptoon matching series count: {len(matched)}")
    for m in matched:
        print(" Series:", m.get("name"), "ID:", m.get("id"))
        # Fetch chapter list
        ch_url = f"https://www.jjaptoon006.com/data/toonlist/{m.get('id')}.js"
        res_ch = urllib.request.urlopen(urllib.request.Request(ch_url, headers=headers), context=ctx, timeout=8)
        ch_text = res_ch.read().decode('utf-8', errors='ignore')
        if " = " in ch_text:
            ch_text = ch_text.split(" = ", 1)[1].rstrip(";").strip()
        ch_data = json.loads(ch_text)
        print(f" Total chapters in Jjaptoon: {len(ch_data)}")
        print(" Top 5 chapter titles in Jjaptoon:")
        for c in ch_data[:5]:
            print("  -", c.get("n"))
except Exception as e:
    import traceback
    traceback.print_exc()
