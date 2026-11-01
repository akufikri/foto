import json, sys, urllib.parse

d = json.load(sys.stdin)
print("total hit:", d["total"])
for r in d["data"]:
    u = urllib.parse.urlparse(r["url"])
    q = urllib.parse.parse_qs(u.query)

    def g(k):
        v = q.get(k) or [""]
        return v[0]

    ev = g("ev") or ("POST" if r["method"] == "POST" else "?")
    ts = r.get("created_at", "")
    lat, lng, acc = g("lat"), g("lng"), g("acc")
    maps = "https://maps.google.com/?q=%s,%s" % (lat, lng) if lat else ""
    print("\n[%s] ev=%s ip=%s" % (ts, ev, r.get("ip")))
    if maps:
        print("  MAP:", maps, "(acc %sm)" % acc)
    if g("ip_city"):
        print("  ip-city:", g("ip_city"), g("ip_lat"), g("ip_lng"))
    if g("err"):
        print("  geo-err:", g("err"), g("msg"))
    print("  tz:", g("tz"), "| lang:", g("lang"), "| screen:", g("sw"), "x", g("sh"))
    print("  ua:", (r.get("user_agent") or "")[:110])
