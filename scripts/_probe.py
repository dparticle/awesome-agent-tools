"""Throwaway probe 4: resolve remaining named tools."""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
UA = {"User-Agent": "awesome-agent-tools-probe", "Accept": "application/vnd.github+json"}

QUERIES = [
    "orca multi agent",
    "orca agent manager",
    "command code",
    "commandcode",
]


def search(q, per_page=8):
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(
        {"q": q, "per_page": per_page, "sort": "stars", "order": "desc"}
    )
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as f:
            return json.loads(f.read())
    except urllib.error.HTTPError as e:
        return {"_error": e.code, "_body": e.read()[:200].decode("utf-8", "replace")}
    except Exception as e:  # noqa: BLE001
        return {"_error": type(e).__name__, "_body": str(e)}


for q in QUERIES:
    r = search(q)
    print(f"\n### {q}")
    if "_error" in r:
        print("   ERR", r)
    else:
        for it in r.get("items", []):
            print(
                f"   {it['full_name']:<42} {it['stargazers_count']:>7} "
                f"pushed={it['pushed_at'][:10]} arch={str(it['archived']):<5} "
                f"{(it.get('description') or '')[:76]}"
            )
    time.sleep(7)

print("\n### direct lookups")
for full in ["slopus/happy", "yetone/magpie", "farion1231/cc-switch", "Wei-Shaw/sub2api", "getpaseo/paseo"]:
    req = urllib.request.Request(f"https://api.github.com/repos/{full}", headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as f:
            r = json.loads(f.read())
        print(
            f"   {r['full_name']:<28} stars={r['stargazers_count']:<7} forks={r['forks_count']:<6} "
            f"pushed={r['pushed_at'][:10]} created={r['created_at'][:10]} arch={r['archived']} "
            f"lic={(r.get('license') or {}).get('spdx_id')} topics={r.get('topics')}"
        )
    except Exception as e:  # noqa: BLE001
        print(f"   {full}: ERR {e}")
    time.sleep(1)
