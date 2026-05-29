# 01 — Tokens (the master index)

Every named token in the Love Church design system, in one place. The fastest "what's our X?" lookup. For deep-dive context per token, see the linked deep-dive file.

The canonical machine-readable copies live at `assets/tokens.json` and `assets/tokens.css`. If anything in this file disagrees with those, **the JSON wins** — update this file to match.

## Color

### Neutral core (90% of every layout)

| Token | Hex | Use |
|---|---|---|
| `lc-ink` | `#151515` | Primary type on cream. Rules. Default fg. |
| `lc-cream` | `#EEE4D3` | Default page background. Type-on-dark fill. |
| `lc-paper` | `#F3F1E5` | Off-white alt background — body copy paper. |
| `lc-taupe` | `#B5A090` | Warm taupe bridge. TOC backgrounds. Muted panels. |
| `lc-taupe-deep` | `#A39584` | Heavier taupe — Annual TOC weight. |

### Loud accent (the "look at me" lever)

| Token | Hex | Use |
|---|---|---|
| `lc-pink-loud` | `#F0238D` | Year pills, CTA pills, section openers, stat backgrounds, lead-paragraph color, pull-quote color. |
| `lc-pink-soft` | `#F49DC3` | Soft pink — IG story highlight covers, secondary tints. |

### Expanded palette (category / energy graphics only)

| Token | Hex | Use |
|---|---|---|
| `lc-orange` | `#E27440` | Messages bucket / orange highlight cover. |
| `lc-yellow` | `#D9C44A` | Sundays bucket / yellow highlight cover. |
| `lc-blue` | `#557EA1` | Photos bucket / blue highlight cover. |
| `lc-green` | `#5E7A56` | Self-Fed bucket / green highlight cover. |
| `lc-gold` | `#C9A24A` | Slide-system gold accent. |

> ⚠️ The expanded palette is **not** for default UI surfaces. It's for category coding (IG story highlight covers) and high-energy event graphics (REV Rally). If you reach for `lc-orange` to set a button color, you've left the system.

### Semantic mappings (use these in code)

| Token | Resolves to | Use |
|---|---|---|
| `lc-bg` | `lc-cream` | Default surface background. |
| `lc-bg-inverse` | `lc-ink` | Dark mode / hero background. |
| `lc-bg-emphasis` | `lc-pink-loud` | Section opener / stat-page / loud emphasis fill. |
| `lc-fg` | `lc-ink` | Default type color on cream. |
| `lc-fg-inverse` | `lc-cream` | Type on ink or pink-loud. |
| `lc-fg-emphasis` | `lc-pink-loud` | Lead paragraph + pull-quote color on cream. |
| `lc-rule` | `lc-ink` | Rule line color. |

For a deeper read — including the loaded-on-pink vs. loaded-on-cream rules and accessibility notes — see `references/02-color.md`.

## Typography

Two typefaces only. No third typeface enters the system without an explicit override.

| Token | Font stack | Use |
|---|---|---|
| `lc-font-display` | Neue Haas Grotesk Display, Inter, Helvetica Neue | Display headlines, body, captions. The workhorse. |
| `lc-font-accent` | Apple Garamond, Garamond, EB Garamond | Italic accent word in headlines. Pull quotes. Emotional emphasis. |

### Weights

| Token | Value | Use |
|---|---|---|
| `lc-fw-thin` | 100 | Rare. Reserved. |
| `lc-fw-light` | 300 | Body at small sizes. |
| `lc-fw-roman` | 400 | Default body. |
| `lc-fw-medium` | 500 | Inline body emphasis (the "**bolded phrase**" pattern). |
| `lc-fw-bold` | 700 | Subheads, label caps. |
| `lc-fw-black` | 900 | Display headlines. THE heroic treatment. |

### Sizes (editorial scale)

| Token | Size | Use |
|---|---|---|
| `lc-fs-display-1` | 96px | Cover headline (ANNUAL REPORT). |
| `lc-fs-display-2` | 72px | Section opener (ENCOUNTERS, LOVE OUT LOUD). |
| `lc-fs-headline-1` | 56px | IG carousel cover, web hero. |
| `lc-fs-headline-2` | 40px | Story page headline (MEET ALYSSA). |
| `lc-fs-title` | 28px | Sub-section, IG quote-card line, email hero. |
| `lc-fs-lead` | 22px | Pink lead paragraph, pull quote. |
| `lc-fs-body` | 18px | Default body. |
| `lc-fs-body-tight` | 16px | Two-column editorial body, email. |
| `lc-fs-caption` | 14px | Section labels, footer. |
| `lc-fs-micro` | 12px | Stat block labels, page numbers, badges. |

### Tracking (letter-spacing)

| Token | Value | Use |
|---|---|---|
| `lc-tracking-display-tight` | -0.030em | Display-1 caps — heroic and tight. |
| `lc-tracking-display-default` | -0.020em | Display-2 / headline caps. The Core Style spec. |
| `lc-tracking-body` | 0 | Default. |
| `lc-tracking-caption` | +0.060em | Section labels in caps — tracked out for editorial spacing. |

### Leading

| Token | Value | Use |
|---|---|---|
| `lc-lh-display-tight` | 0.92 | Stacked display caps (ANNUAL / REPORT). |
| `lc-lh-headline` | 1.05 | Single-line headlines. |
| `lc-lh-body` | 1.45 | Body. |
| `lc-lh-tight` | 1.20 | Compressed runs. |

For pairing rules, the italic-accent pattern, and the "bold inline emphasis" body convention — see `references/03-typography.md`.

## Spacing (4-base scale)

| Token | Value |
|---|---|
| `lc-space-xs` | 4px |
| `lc-space-sm` | 8px |
| `lc-space-md` | 16px |
| `lc-space-lg` | 24px |
| `lc-space-xl` | 32px |
| `lc-space-2xl` | 48px |
| `lc-space-3xl` | 64px |
| `lc-space-4xl` | 96px |
| `lc-space-5xl` | 128px |

Use named tokens — never raw px in design specs. The names compound across the team.

## Radii

| Token | Value | Use |
|---|---|---|
| `lc-radius-none` | 0 | Default. The system prefers crisp corners. |
| `lc-radius-sm` | 4px | Mild rounding — rare. |
| `lc-radius-md` | 8px | Soft cards — rare. |
| `lc-radius-pill` | 9999px | Pill badges — year, CTA, the LC mark badge. |

## Rules (horizontal lines)

| Token | Value | Use |
|---|---|---|
| `lc-rule-hairline` | 1px | TOC dot leaders, footer dividers. |
| `lc-rule-regular` | 1.5px | Stat-block separators. |
| `lc-rule-bold` | 3px | Section divider rules. |

## Motion

| Token | Value | Use |
|---|---|---|
| `lc-dur-fast` | 150ms | Micro-interactions (hover, tap). |
| `lc-dur-base` | 240ms | Default UI transitions. |
| `lc-dur-slow` | 400ms | Reveals, bigger state changes. |
| `lc-dur-ambient` | 800ms | Slow drifts in hero motion. |
| `lc-ease-standard` | `cubic-bezier(0.2, 0, 0, 1)` | Default. |
| `lc-ease-emphasis` | `cubic-bezier(0.3, 0, 0, 1)` | Punchier — for the pink hits. |
| `lc-ease-linear` | `cubic-bezier(0, 0, 1, 1)` | Continuous loops. |

## Surface dimensions

When generating a deliverable, use **exactly** these dimensions. Approximations break the system.

### Social

| Surface | Dimensions | Notes |
|---|---|---|
| IG feed (4:5 portrait) | 1080×1350 | Default for "Sundays at Love" recaps. |
| IG story | 1080×1920 | 9:16. Top 250px and bottom 250px = Instagram UI safe zone. |
| IG square / carousel slide | 1080×1080 | |
| IG reel cover | 1080×1920 | Design 1080×1350 safe area. |
| YT thumbnail | 1280×720 | 16:9. |
| YT channel art | 2560×1440 | Safe area 1546×423. |
| FB cover | 1640×856 | |
| GMB post | 1200×900 | 4:3. |

### Web (lovechurch.org)

| Surface | Dimensions |
|---|---|
| Hero (desktop, 2x retina) | 2880×1620 |
| Hero (mobile) | 750×1334 |
| Card | 1200×900 |

### Email (MailChimp)

| Surface | Dimensions | Notes |
|---|---|---|
| Hero (desktop) | 1200×600 | |
| Hero (mobile) | 600×600 | MailChimp mobile column width. |
| Body block | 1200×N | Full-bleed body, height variable. |

### App (Subsplash)

| Surface | Dimensions | Notes |
|---|---|---|
| Feature card | 1242×500 | App home hero. |
| Square card | 1080×1080 | |

## How to use this index

When the user asks "what's our X?":
1. Find the closest token in this file.
2. Quote the **token name**, the **value**, and the **use context** in that order.
3. Cite the deep-dive reference if the user might want more.

Example:

> Q: What's our body font?
> A: `lc-font-display` — Neue Haas Grotesk Display, Roman 400 at `lc-fs-body` (18px), leading `lc-lh-body` (1.45). It's the workhorse — Apple Garamond italic only enters as the accent word in headlines or as a pull-quote treatment. See `references/03-typography.md` for the full pairing logic.

The token names are how the team gets faster. Every time you cite a name, the system gets a little more durable.
