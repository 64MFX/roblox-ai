#!/usr/bin/env python3
"""Turn data/github-repos.json and data/devforum-topics.json into browsable markdown pages."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PER_PAGE = 500


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").replace("<", "&lt;").replace(">", "&gt;").strip()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def pages(kind, items, title, header, row, intro):
    out = os.path.join(ROOT, "resources", kind)
    for fn in os.listdir(out) if os.path.isdir(out) else []:
        if fn.startswith("page-"):
            os.remove(os.path.join(out, fn))
    n = (len(items) + PER_PAGE - 1) // PER_PAGE
    index = [f"# {title}", "", intro, "", f"{len(items)} entries in {n} pages, sorted by popularity.", "",
             "| Page | Range |", "|---|---|"]
    for i in range(n):
        chunk = items[i * PER_PAGE:(i + 1) * PER_PAGE]
        name = f"page-{i + 1:02d}.md"
        lines = [f"# {title}: page {i + 1} of {n}", "", f"[Index](README.md)", "", header[0], header[1]]
        lines += [row(x) for x in chunk]
        write(os.path.join(out, name), "\n".join(lines) + "\n")
        index.append(f"| [{i + 1}]({name}) | #{i * PER_PAGE + 1}-{i * PER_PAGE + len(chunk)} |")
    write(os.path.join(out, "README.md"), "\n".join(index) + "\n")
    return n


def main():
    total = 0
    gp = os.path.join(ROOT, "data", "github-repos.json")
    if os.path.exists(gp):
        g = json.load(open(gp, encoding="utf-8"))
        repos = g["repos"]
        total += len(repos)
        pages(
            "github", repos, "GitHub repositories tagged Roblox / Luau",
            ("| Repo | Stars | Language | License | Description |", "|---|---:|---|---|---|"),
            lambda r: "| [{n}](https://github.com/{n}){a} | {s} | {l} | {lic} | {d} |".format(
                n=r["name"], a=" (archived)" if r["archived"] else "", s=r["stars"], l=esc(r["lang"]),
                lic=esc(r["license"] if r["license"] not in (None, "NOASSERTION") else ""), d=esc(r["desc"])),
            f"Harvested {g['generated']} from the GitHub search API with `scripts/harvest_github.py`. "
            "Every row was a public, non-fork repository when harvested. Descriptions are the repo owners' own. "
            "Exploit, executor and cheat tooling is filtered out. Check licence and maintenance before using any code.",
        )
    dp = os.path.join(ROOT, "data", "devforum-topics.json")
    if os.path.exists(dp):
        d = json.load(open(dp, encoding="utf-8"))
        topics = d["topics"]
        total += len(topics)
        pages(
            "devforum", topics, "DevForum resource topics",
            ("| Topic | Likes | Views | Category | Created |", "|---|---:|---:|---|---|"),
            lambda t: "| [{ti}](https://devforum.roblox.com/t/{sl}/{id}) | {lk} | {vw} | {c} | {cr} |".format(
                ti=esc(t["title"]), sl=t["slug"], id=t["id"], lk=t["likes"], vw=t["views"], c=esc(t["cat"]), cr=t["created"]),
            f"Harvested {d['generated']} from the public DevForum JSON API with `scripts/harvest_devforum.py`. "
            "Titles belong to their authors; follow the links to read them.",
        )
    print("rows:", total)


if __name__ == "__main__":
    main()
