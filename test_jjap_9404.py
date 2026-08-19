import urllib.request, ssl, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.jjaptoon006.com/',
    'Origin': 'https://www.jjaptoon006.com'
}

url = "https://www.jjaptoon006.com/data/toonlist/9404.js"
try:
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, context=ctx, timeout=5)
    text = res.read().decode('utf-8', errors='ignore')
    json_text = text.split(" = ", 1)[1].rstrip(";").strip() if " = " in text else text
    ch_data = json.loads(json_text)
    print(f"Jjaptoon comic 9404 -> Total chapters: {len(ch_data)}")
    print("Top 5 chapter names in Jjaptoon:")
    for c in ch_data[:5]:
        print(" -", c.get("n"))
except Exception as e:
    print("Error:", e)
