# roblox-ui-references

**Over 700 visual references for your AI** — Roblox-inspired UI, thumbnails, logos, effects, animation references, and more to inspire Claude Code, Codex, and other AI assistants.

> The "over 700" count is grounded in the existing **707 images** in `previews/`; other referenced images, catalogs, and patterns are additional. Artwork belongs to its respective creators; treat visuals as inspiration, not assets licensed for redistribution or direct reuse.
A curated collection of Roblox UI references for Claude Code, Codex, and other AI coding assistants to study and use as design inspiration

## Start here
- **AI assistants:** read [AI-GUIDE.md](AI-GUIDE.md). Everything is indexed in [INDEX.md](INDEX.md) and [index.json](index.json).
- **Humans:** browse the catalogs below.

## Contents
| Path | What | Size |
|---|---|---|
| [`ui-styles/`](ui-styles/GUI-STYLES.md) | GUI styles, one folder each, with palettes and recipes | 112 styles |
| [`animations/`](animations/ANIMATIONS.md) | UI and character/combat animation patterns | 33 |
| [`cutscenes/`](cutscenes/CUTSCENES.md) | Camera, cinematic and dialogue patterns | 18 |
| [`vfx/`](vfx/VFX.md) | Particles, beams, trails, feedback effects | 36 |
| [`sfx/`](sfx/SFX.md) | Sound design and music patterns | 54 |
| [`cookbook/`](cookbook/README.md) | Small Luau modules, compile-checked in Studio 0.743 | 23 scripts |
| [`official-docs/`](official-docs/README.md) | Roblox creator-docs subset (CC BY 4.0): guides plus class, data type and enum reference | 89 guides, 114 classes |
| [`previews/`](previews/README.md) | Credited itch.io cover galleries by tag | 61 galleries, 707 images |
| [`thumbnails/`](thumbnails/README.md) | Curated Roblox thumbnail inspirations and game links | 30 game references |
| [`logos/`](logos/README.md) | Curated Roblox game-icon/logo inspirations and game links | 30 game references |
| [`libraries.md`](libraries.md) | Open-source libraries, plugins, asset sources | |
| `studs-ui/`, `sports/`, `Icons/`, `Animation-Refs/` | Original image and video references | |

About 124 more images sit inside the entry folders, credited in [ui-styles/IMAGE-CREDITS.md](ui-styles/IMAGE-CREDITS.md) and [previews/CREDITS.md](previews/CREDITS.md).

## What to trust
- `official-docs/` is Roblox's own documentation and is the authority on API names and behaviour.
- `cookbook/` scripts were compiled in Roblox Studio and most were run against unparented instances; none were checked in a live game, and visuals/audio were not judged.
- Style descriptions, palettes and recipes outside the cookbook are synthesis from general knowledge and linked sources, and are **not tested**.
- Pictures are previews owned by their creators (itch.io listings), used as references. Check licences before using any asset.

## Roblox image references

- [Thumbnail catalog](thumbnails/README.md) and [logo catalog](logos/README.md) list Roblox experiences for visual research.
- [PNG downloader](scripts/fetch_roblox_images.py) fetches public Roblox experience artwork and records source game links in `roblox-image-manifest.json` when run.
- [GitHub Actions workflow](.github/workflows/fetch-roblox-references.yml) is configured to download and commit PNG files. **Downloaded PNGs are not included in the reference total unless actually present in this repository.**
- Artwork is owned by its respective creators; do not assume reuse rights merely because a public thumbnail is accessible.
