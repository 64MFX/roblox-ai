#!/usr/bin/env python3
"""Collect top DevForum resource topics through the public Discourse JSON API.

Every row is a real topic returned by devforum.roblox.com. Output: data/devforum-topics.json
Polite: one request per second with an identifying User-Agent.
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "devforum-topics.json")
BASE = "https://devforum.roblox.com"
UA = "roblox-ai-reference-harvester (+https://github.com/izzyfrm/roblox-ai)"


def get(path):
    for attempt in range(4):
        try:
            req = urllib.request.Request(BASE + path, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            if "404" in str(e):
                return None
            time.sleep(5 * (attempt + 1))
    return None


def main():
    time.sleep(1)
    cats = get("/categories.json?include_subcategories=true")
    allcats = []
    for c in cats["category_list"]["categories"]:
        allcats.append(c)
        for s in c.get("subcategory_list", []) or []:
            allcats.append(s)
    # the Resources category and its subcategories
    res_ids = {x["id"] for x in allcats if x["slug"] == "resources"}
    want = [c for c in allcats if c["id"] in res_ids or c.get("parent_category_id") in res_ids]
    seen, topics = set(), []
    for c in want:
        path_base = f"/c/{c['slug']}/{c['id']}/l/top.json?period=all&page="
        for page in range(0, 400):
            time.sleep(1)
            d = get(path_base + str(page))
            if not d:
                break
            items = d["topic_list"]["topics"]
            if not items:
                break
            for t in items:
                if t["id"] in seen:
                    continue
                seen.add(t["id"])
                topics.append({
                    "id": t["id"],
                    "title": t["title"],
                    "slug": t["slug"],
                    "likes": t.get("like_count", 0),
                    "views": t.get("views", 0),
                    "created": (t.get("created_at") or "")[:10],
                    "cat": c["name"],
                })
        print(c["name"], "->", len(topics), flush=True)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        json.dump({"generated": time.strftime("%Y-%m-%d"), "count": len(topics),
                   "topics": sorted(topics, key=lambda x: -x["likes"])},
                  open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    sys.exit(main())
