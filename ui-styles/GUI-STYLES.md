# Roblox GUI Style Catalog (72 styles)

A style vocabulary for AI assistants (Claude Code, Codex) and humans to pick from when designing Roblox UI.
Each entry gives the look, a palette, a Roblox implementation recipe, best-fit genres and references.

> **Honesty note.** Web research was done 2026-10-20. Sources marked ✅ were actually returned by search and are real, but most are marketplace listings and docs, not deep style analyses. The 72-style taxonomy, palettes and recipes are an original synthesis by Claude, not copied from any one source. Entries whose only reference is `S` (search) have no verified kit behind them. Check each pack's license before commercial use.

## Verified reference index

| Key | Source | What it is |
|---|---|---|
| R1 | ✅ [Roblox Creator Hub: UI appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers) | UIStroke, UIGradient, UICorner usage |
| R2 | ✅ [Roblox Creator Hub: UI compatibility](https://create.roblox.com/docs/en-us/ui/styling/compatibility) | UIAspectRatioConstraint etc. |
| R3 | ✅ [Huge Clean Stud GUI Pack (20+ frames)](https://builtbybit.com/resources/huge-clean-stud-gui-pack-20-frames.110766/) | Stud-style simulator kit |
| R4 | ✅ [Modern Cartoon Simulator UI](https://builtbybit.com/resources/modern-cartoon-simulator-ui.109159/) | Shop, rewards, rebirth, upgrades, settings |
| R5 | ✅ [Roblox Stud UI Pack](https://builtbybit.com/resources/roblox-stud-ui-pack.102644/) | Stud kit |
| R6 | ✅ [Clean Stud UI System 2](https://builtbybit.com/resources/clean-stud-ui-system-2-for-roblox.104242/) | Stud system |
| R7 | ✅ [Clean Stud UI System 3](https://builtbybit.com/resources/clean-stud-ui-system-3-for-roblox.105203/) | Stud system |
| R8 | ✅ [Ultimate Studded UI Pack](https://builtbybit.com/resources/ultimate-studded-ui-pack.115887/) | Studded kit |
| R9 | ✅ [Cartoony UI Pack Pro+](https://builtbybit.com/resources/cartoony-ui-pack-pro-ui-system.107727/) | Scripted cartoony system, tween/hover/click |
| R10 | ✅ [Cartoony UI Kit (25+ frames)](https://builtbybit.com/resources/cartoony-ui-kit-25-frames.117327/) | Codes, daily rewards, trading, voting |
| R11 | ✅ [Fantasy UI System Pack](https://builtbybit.com/resources/fantasy-ui-system-pack.105959/) | Glowing fantasy shop/inventory/rewards |
| R12 | ✅ [Modern medieval-themed design](https://builtbybit.com/resources/modern-medieval-themed-design.114952/) | RPG inventory with rarity labels |
| R13 | ✅ [GUI Asset Pack (glossy/neon)](https://builtbybit.com/resources/gui-asset-pack.104484/history) | Glossy buttons, neon panels |
| R14 | ✅ [PixelBlox Vol. 1 (itch.io)](https://bloxbuilders.itch.io/pixelblox-vol1) | Retro pixel GUI, 20+ elements |
| R15 | ✅ [GAG UI Pack (itch.io)](https://adrianart.itch.io/gag-ui-pack) | Grow-a-Garden-style PSD kit |
| R16 | ✅ [Game UI Database](https://www.gameuidatabase.com/about.php) | 55k+ game UI screenshots, filter by texture/pattern/colour |
| R17 | ✅ [Game UI Database coverage (80.lv)](https://80.lv/articles/game-ui-database-collecting-references-to-inspire-designers/) | Background on R16 |
| R18 | ✅ [creation.dev: Roblox UI design best practices](https://www.creation.dev/blog/roblox-ui-design-best-practices) | Clarity, consistency, minimal HUD |
| R19 | ✅ [DevForum: UI Designing suggestions](https://devforum.roblox.com/t/suggestions-topic-ui-designing/963950) | Community thread (dated, light on specifics) |
| R20 | ✅ [itch.io GUI assets](https://itch.io/game-assets/newest/tag-gui/tag-ux) | General GUI asset browsing |
| S | Image search (not a verified page) | `https://www.google.com/search?tbm=isch&q=roblox+<style>+gui` |

**In-repo references:** `studs-ui/` (Stud-GUI-1/2/4/5, Stud-Buttons, Stud-Shop, Stud-DailyRewards), `sports/` (Basketball, Boxing, Football menus, loading and main menu), `Icons/` (3D outline icon set).

## How to use
1. Pick **one primary style** and at most one accent style per game.
2. Copy the palette and recipe into a shared theme module (colors, corner radius, stroke, font) so every screen matches.
3. Support mobile and gamepad: `UIAspectRatioConstraint` (R2), `UIScale`, safe areas.
4. Keep HUDs minimal, with persistent stats near the top corners (R18).

Common recipe pieces: `UICorner`, `UIStroke`, `UIGradient` (R1), `UIListLayout`/`UIGridLayout`, `UIPadding`, `UIScale`, TweenService or springs.

---

## A. Stud & Block families (1-8)

1. **Classic Stud GUI.** Bright flat panel with a subtle round-stud pattern, chunky dark outline. Palette `#2B90FF #FFD23F #1B1B2F`. Recipe: Frame + tiled stud ImageLabel at 6-12% opacity, UIStroke 3-4px, UICorner 10. Best: simulators, tycoons. Refs: R3 R5 R6 R7, in-repo `studs-ui/`.
2. **Clean Stud (minimal).** Studs only on header or buttons, large flat body. Palette `#FFFFFF #3AA0FF #20263A`. Refs: R6 R7.
3. **Ultimate Studded.** Dense studs on every container, bevel highlights. Recipe: two-layer stud image, top-light UIGradient. Refs: R8.
4. **Stud Candy.** Studs plus saturated candy colours and a glossy highlight strip. Palette `#FF5FA2 #7C5CFF #FFE066`. Refs: R4 R13.
5. **LEGO-Brick UI.** Brick-shaped panels with raised cylinders, grid-aligned. Recipe: circular ImageLabels along the top edge. Refs: R5, S.
6. **Stud Dark.** Dark navy panel, faint studs, neon-coloured buttons. Palette `#12151F #1F2740 #4DE1FF`. Refs: R7, S.
7. **Stud Pastel.** Soft pastel panels with white studs. Palette `#FFD6E8 #D6F0FF #FFF3C4`. Refs: R3, S.
8. **Stud Wood/Metal.** Studs as rivets on wood or steel plates. Recipe: material texture + rivet ImageLabels. Refs: S, R16 (filter by texture).

## B. Cartoon & Simulator (9-20)

9. **Modern Cartoon Simulator.** Thick outline, saturated gradient fill, big rounded corners, bouncy buttons. Palette `#34C759 #FFB020 #3B2A6B`. Recipe: vertical UIGradient, UIStroke 4px, UICorner 14-20, scale tween on hover. Refs: R4 R9 R10.
10. **Chunky Candy Buttons.** Two-tone button with a darker "lip" duplicate offset 6px below. Refs: R9 R13.
11. **Glossy Bubble.** White highlight ellipse on the upper third, drop shadow below. Refs: R13.
12. **Hit-Game Layout (original art).** Borrow the structure seen in hit simulators (tab column, centre grid, detail panel) but never their assets. Refs: R16, S.
13. **Pet-Collector Grid.** Rarity-coloured cards in a UIGridLayout, egg/pet icons, index tab. Recipe: card Frame with rarity-coloured UIStroke. Refs: R10 R15, in-repo `Icons/`.
14. **Rebirth/Prestige Panel.** Big central button, multiplier counter, glowing aura. Refs: R4.
15. **Daily Reward Calendar.** 7/30-day grid with claimed, today and locked states. Refs: R10, in-repo `studs-ui/Stud-DailyRewards.png`, calendar icons.
16. **Garden/Farm Cozy.** Warm greens, wood trim, leaf motifs. Palette `#7BC65A #C9965A #FFF4D6`. Refs: R15.
17. **Tycoon Cash HUD.** Large money counter with coin icon, "+$" floaters. Refs: R3 R4.
18. **Idle/Clicker Orb.** Central tap target, ring progress, upgrade list below. Refs: R9, S.
19. **Gacha/Egg Hatch.** Dim full-screen, egg shake, rarity-burst reveal card. Refs: R10, in-repo `Icons/Basic Egg`.
20. **Obby Checkpoint Bar.** Thin top stage bar, stage number, skip-purchase button. Refs: R3, S.

## C. Fantasy / RPG (21-30)

21. **Glowing Fantasy.** Dark violet panels, gold filigree, glowing rarity borders. Palette `#1B1030 #D4AF37 #8E5CFF`. Refs: R11.
22. **Modern Medieval.** Parchment and iron, rarity labels, equip/sell buttons. Refs: R12.
23. **Parchment Scroll.** Aged paper, serif font, wax-seal buttons. Refs: in-repo `Icons/Scroll`, S.
24. **Stone Dungeon.** Rough grey slabs, torch-orange accents. Refs: S, R16.
25. **Elven Nature.** Vines, leaf corners, soft green glow. Refs: S.
26. **Souls-like Minimal.** Thin bars, desaturated, no outlines, serif text. Refs: R16.
27. **Anime RPG Sidebar.** Left icon menu, right info panel, diagonal cuts. Palette `#0F1226 #FF4D6D #FFFFFF`. Refs: S.
28. **Gacha Character Cards.** Tall cards with star rows and elemental badges. Refs: R16, S.
29. **Skill Tree Web.** Node-and-line canvas, locked/unlocked glow. Refs: R16.
30. **Quest Journal.** Book layout with tabs and ribbon bookmarks. Refs: in-repo `Icons/Book`, S.

## D. Sci-Fi / Tech (31-40)

31. **Neon Cyberpunk.** Black base, cyan/magenta neon strokes with glow. Palette `#0A0A14 #00F0FF #FF2BD6`. Recipe: UIStroke plus a blurred duplicate. Refs: R13, S.
32. **Holographic HUD.** Transparent blue panels, thin lines, scanline overlay. Refs: S.
33. **Military Tactical.** Olive/black, stencil font, clipped angular corners. Refs: S.
34. **Space Station.** White/grey modular panels, orange warning accents. Refs: S.
35. **Terminal/Hacker.** Monospace green on black, blinking cursor. Refs: S.
36. **Mecha Cockpit.** Segmented bars, hex readouts, red alert state. Refs: R16.
37. **Synthwave.** Purple-pink sunset gradients, grid-floor motif. Refs: S.
38. **Glitch.** Chromatic-split text, jitter tween, noise overlay. Refs: S.
39. **Vector Minimal Tech.** Flat monochrome, hairlines, whitespace. Refs: R18.
40. **Futuristic Racing.** Slanted speedometer, boost bar, italic numerals. Refs: R16.

## E. Modern / Clean (41-50)

41. **Glassmorphism.** Translucent panels, 1px light border, soft shadow. Recipe: high-transparency Frame + UIStroke + subtle gradient. Real blur is limited in Roblox UI. Refs: S (no Roblox kit found).
42. **Flat Material.** Solid colours, elevation shadows, 8px radius. Refs: R18.
43. **Dark Mode Pro.** Near-black cards, one accent. Palette `#0E0F13 #1A1C23 #5B8CFF`. Refs: R18.
44. **iOS-Soft.** Radius 24+, pill buttons, clean sans font. Refs: S.
45. **Neumorphism.** Soft inner/outer shadows on a same-colour surface. Caution: low contrast. Refs: S.
46. **Brutalist.** Hard black borders, offset hard shadows, bright flat fills. Refs: S.
47. **Minimal Monochrome.** Black and white only, type-led. Refs: R18.
48. **Pill-Tab Dashboard.** Top pill tabs, card grid, stat tiles. Refs: R10.
49. **Compact Mobile HUD.** Large thumb targets, bottom-anchored actions. Refs: R2 R18.
50. **Gamepad Radial.** Radial menu for controller, big focus ring. Refs: R16.

## F. Horror / Dark (51-56)

51. **Backrooms Liminal.** Beige/yellow, flat office-grade UI, low-res stamped font. Refs: S.
52. **Gothic Horror.** Blood red on black, ornate serif, cracked-glass border. Refs: S.
53. **VHS/Found Footage.** Timestamp, REC dot, scanlines, tracking noise. Refs: S.
54. **Asylum Paper.** Stained paper, typewriter text, ink stamps. Refs: S.
55. **Minimal Survival HUD.** Tiny vitals, vignette, nothing else. Refs: R18.
56. **Cursed Glitch Dark.** Dark base, distorted text, flicker animation. Refs: S.

## G. Retro / Pixel / Stylised (57-64)

57. **Pixel Art Retro.** Integer-scaled pixel frames, bitmap font, limited palette. Recipe: ImageLabel with `ResampleMode = Pixelated`. Refs: R14.
58. **8-bit Arcade.** Chunky borders, score ticker, blinking prompts. Refs: R14.
59. **16-bit JRPG Box.** Blue gradient dialogue box with white border. Refs: R14, S.
60. **Comic/Manga.** Halftone dots, speech-bubble panels, bold action text. Refs: S.
61. **Hand-Drawn Sketch.** Wobbly outlines, paper background, crayon fill. Refs: S.
62. **Paper Craft.** Layered cut-paper shadows, folded corners. Refs: S.
63. **Claymation.** Soft 3D blobs, fingerprint-texture highlights. Refs: S.
64. **Low-Poly Faceted.** Triangular shards, flat-shaded gradient fills. Refs: S.

## H. Genre-specific (65-72)

65. **Sports Broadcast.** Scoreboard bars, team colours, slanted ribbons. Refs: in-repo `sports/` (Basketball, Boxing, Football, Main Menu, Loading Screen).
66. **Fighting Game.** Big health bars with timer, combo counter, VS screen. Refs: R16.
67. **Shooter Tactical HUD.** Ammo counter, compass strip, hitmarkers. Refs: R16.
68. **Racing Dashboard.** As #40 plus a lap/position tower. Refs: R16.
69. **Roleplay Town.** Phone-style app grid, chat bubbles, pastel. Refs: S.
70. **Tower Defense.** Bottom tower bar with costs, wave banner, lives top-right. Refs: R16.
71. **Horror Co-op Lobby.** Vote cards, ready ticks, ominous palette. Refs: S.
72. **Holiday/Seasonal.** Snowflakes, candy-cane borders, calendar. Refs: in-repo `Icons/` (Christmas Tree, Snowman, Candy Cane, Snowflake).

---

## Research gaps
- No Behance or Dribbble Roblox pages were returned. Search those directly.
- No horror, sci-fi, glassmorphism or minimal Roblox kits were found on BuiltByBit. Those entries come from design convention, not a verified kit.
- No UI breakdowns for specific games (Pet Simulator 99, Blox Fruits, Adopt Me) were found, so no game is cited as an example. Use R16 or in-game screenshots.
- Several returned sites were low-quality spam and were excluded.
