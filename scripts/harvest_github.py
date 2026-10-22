#!/usr/bin/env python3
"""Collect public GitHub repositories tagged with Roblox/Luau topics.

Every row comes from the GitHub search API, so each repo existed when harvested.
Requires the `gh` CLI to be logged in. Output: data/github-repos.json

Exploit, executor and cheat tooling is filtered out on purpose.
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "github-repos.json")

TOPICS = [
    "roblox", "luau", "roblox-studio", "rojo", "roblox-ts", "roblox-lua", "roblox-game",
    "roblox-games", "roblox-api", "roblox-scripts", "roblox-module", "roblox-plugin",
    "roblox-gui", "robloxstudio", "roblox-library", "roblox-framework", "roblox-development",
    "robloxlua", "roblox-script", "roblox-studio-plugin", "roblox-open-cloud", "roblox-ui",
    "wally", "roblox-package", "roblox-tools", "roblox-bot", "roblox-datastore",
]

BLOCK = re.compile(
    r"exploit|executor|cheat|hack|aimbot|inject|bypass|nuker|grabber|stealer|keylog|ddos|"
    r"spoof|crack|synapse|krnl|scriptware|fluxus|delta executor|roblox-?account|cookie|\.roblosecurity|"
    r"logger|rat\b|botnet|raid|spam|boost|free robux|robux generator|nsfw|porn|hentai",
    re.I,
)

_last = [0.0]


def gh(path):
    # search API allows 30 requests/minute
    wait = 2.2 - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    for attempt in range(6):
        p = subprocess.run(["gh", "api", path], capture_output=True, text=True, encoding="utf-8", errors="replace")
        _last[0] = time.time()
        p.stdout = p.stdout or ""
        p.stderr = p.stderr or ""
        if p.returncode == 0 and p.stdout:
            return json.loads(p.stdout)
        if "rate limit" in (p.stderr + p.stdout).lower() or "secondary" in (p.stderr + p.stdout).lower():
            time.sleep(30 * (attempt + 1))
            continue
        if "422" in p.stderr or "Validation" in p.stderr:
            return None
        time.sleep(5)
    return None


def windows(topic, start, end):
    """Yield date windows each holding <= 1000 repos."""
    stack = [(start, end)]
    while stack:
        a, b = stack.pop()
        q = f"topic:{topic}+fork:false+created:{a}..{b}"
        r = gh(f"search/repositories?q={q}&per_page=1")
        if not r:
            continue
        n = r["total_count"]
        if n == 0:
            continue
        if n <= 1000 or a == b:
            yield (a, b, n)
            continue
        da, db = dt.date.fromisoformat(a), dt.date.fromisoformat(b)
        mid = da + (db - da) / 2
        stack.append((a, mid.isoformat()))
        stack.append(((mid + dt.timedelta(days=1)).isoformat(), b))


def main():
    repos = {}
    if os.path.exists(OUT):
        for r in json.load(open(OUT, encoding="utf-8"))["repos"]:
            repos[r["id"]] = r
    today = dt.date.today().isoformat()
    for topic in TOPICS:
        for a, b, n in windows(topic, "2012-01-01", today):
            pages = min(10, (n + 99) // 100)
            for page in range(1, pages + 1):
                r = gh(f"search/repositories?q=topic:{topic}+fork:false+created:{a}..{b}&per_page=100&page={page}&sort=stars")
                if not r:
                    break
                for it in r.get("items", []):
                    text = " ".join([it["full_name"], it.get("description") or "", " ".join(it.get("topics") or [])])
                    if BLOCK.search(text):
                        continue
                    repos[it["id"]] = {
                        "id": it["id"],
                        "name": it["full_name"],
                        "desc": (it.get("description") or "").strip()[:200],
                        "stars": it["stargazers_count"],
                        "lang": it.get("language"),
                        "license": (it.get("license") or {}).get("spdx_id"),
                        "topics": (it.get("topics") or [])[:8],
                        "pushed": (it.get("pushed_at") or "")[:10],
                        "archived": it.get("archived", False),
                    }
                if len(r.get("items", [])) < 100:
                    break
        print(topic, "->", len(repos), "repos so far", flush=True)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        json.dump({"generated": today, "count": len(repos), "repos": sorted(repos.values(), key=lambda x: -x["stars"])},
                  open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    sys.exit(main())
