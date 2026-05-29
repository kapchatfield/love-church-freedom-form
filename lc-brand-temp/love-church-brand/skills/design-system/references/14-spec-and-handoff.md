# 14 — Spec & handoff

When a deliverable is ready to leave this skill and enter production — the V/I Team builds the asset, a contractor designs the page, a dev implements the email — the spec needs to be **self-contained**. No follow-up questions. No "what color is the headline again?" This file documents the handoff format that makes that possible.

## The handoff packet

Every spec returned to the user (in generate or handoff mode) includes these eight blocks, in this order. Don't omit. Don't rearrange.

```
1. WHAT THIS IS
   One-sentence purpose.

2. SURFACE
   Surface token + exact dimensions + format.

3. TOKENS USED
   Bulleted list of every token referenced, with values inline.

4. LAYOUT
   Grid, safe areas, anchor points, padding values.

5. TYPE SPEC
   Per text element: typeface, weight, size, tracking, leading, color, case, italic-accent.

6. IMAGE SPEC
   Mode (documentary / B&W halftone / studio / fill), subject, lighting, crop, overlay if any.

7. EXPORT
   File format, color profile, exact resolution, retina spec if applicable.

8. ASSET PATHS
   File name, source location, output location.
```

## File naming

Every deliverable file uses this pattern:

```
[surface-slug]_[content-slug]_[YYYY-MM-DD].[ext]
```

**surface-slug** — kebab-case identifier of the surface:

| Surface | Slug |
|---|---|
| IG feed | `ig-feed` |
| IG story | `ig-story` |
| IG carousel slide | `ig-carousel` |
| IG reel cover | `ig-reel-cover` |
| YT thumbnail | `yt-thumb` |
| YT channel art | `yt-channel-art` |
| FB cover | `fb-cover` |
| GMB post | `gmb-post` |
| Web hero | `web-hero` |
| Web card | `web-card` |
| Email hero | `email-hero` |
| Email body | `email-body` |
| Email footer | `email-footer` |
| App feature | `app-feature` |
| App thumbnail | `app-thumb` |

**content-slug** — kebab-case identifier of what the asset is about:

- Specific event: `plan-your-visit`, `rev-rally`, `commission-sunday`
- Recurring content: `sundays-at-love-recap`, `weekly-newsletter`, `bible-in-2-years-day-142`
- Series: `more-to-life`, `agape`

**YYYY-MM-DD** — ship date of the asset.

**Examples:**

```
ig-story_plan-your-visit_2026-05-10.png
yt-thumb_more-to-life-week-3_2026-05-15.jpg
email-hero_weekly-newsletter_2026-05-08.png
gmb-post_sundays-at-love_2026-05-07.jpg
```

For a carousel, append the slide number:

```
ig-carousel_sundays-at-love-recap_2026-05-04_01.png
ig-carousel_sundays-at-love-recap_2026-05-04_02.png
ig-carousel_sundays-at-love-recap_2026-05-04_03.png
```

## Asset directory structure

When working in the `LC Notion` workspace folder, organize delivered assets:

```
LC Notion/
├── Brand/
│   ├── design-system/        ← this skill's source files
│   ├── tokens/               ← copies of tokens.json / tokens.css for reference
│   └── source-files/         ← Master InDesign / Figma / Photoshop files
└── Deliverables/
    └── 2026/
        └── 05/
            ├── ig-story_plan-your-visit_2026-05-10.png
            ├── ig-story_plan-your-visit_2026-05-10.psd
            └── email-hero_weekly-newsletter_2026-05-08.png
```

## Color profile

| Use | Profile |
|---|---|
| Screen (web, social, app, email) | sRGB |
| Print (Annual Report, Reading Guide, posters) | CMYK with Adobe RGB working space, US Web Coated SWOP v2 |
| Photo source files | Adobe RGB or ProPhoto |

## Export presets

| Surface | Format | Quality | Color | Compression |
|---|---|---|---|---|
| Photo-led JPG (IG feed, FB, GMB) | JPG | 85 | sRGB | Optimized baseline |
| Type-led / quote cards | PNG-24 | — | sRGB | Standard |
| Reels cover, video thumbnail | JPG | 90 | sRGB | Progressive |
| Email hero (rendered) | PNG-24 retina (2x) | — | sRGB | Standard |
| Web hero | WebP (primary) + JPG (fallback) | 80 / 85 | sRGB | — |
| Print | PDF/X-1a | — | CMYK | — |

## Token JSON for downstream consumption

The `assets/tokens.json` file is the canonical machine-readable copy. When handing off to a developer or design-tool integration:

- For **web**, the dev imports `tokens.css` directly and uses CSS variables.
- For **Figma**, plugin "Tokens Studio" can ingest the W3C-format JSON.
- For **MailChimp**, the CSS variables go in custom CSS, but inline styles are still safer for body emails.
- For **Subsplash app theming**, only the `lc-pink-loud` accent transfers — Subsplash exposes a single accent.

## Versioning

The system as currently shipped is **v1.0.0**. Future updates follow semver:

- **Patch** (1.0.1): typo fixes, better examples, corrections that don't change values.
- **Minor** (1.1.0): new tokens, new components, additions that don't break existing usage.
- **Major** (2.0.0): renamed tokens, removed components, value changes that break existing deliverables.

When the system updates, bump `assets/tokens.json` `$metadata.version` AND add a CHANGELOG entry to `references/01-tokens.md`.

## Pre-flight handoff check

Before sending a spec packet to a designer or dev:

- All eight blocks present?
- File name follows the convention?
- Color profile specified?
- Export resolution exact (including retina if applicable)?
- Token names cited (not just raw values)?
- Image direction is enough that someone *not in this conversation* could shoot/select a photo from it?
