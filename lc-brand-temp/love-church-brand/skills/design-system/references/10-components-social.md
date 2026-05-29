# 10 — Components: Social

Specs for every social surface in scope: Instagram (feed, story, carousel, reel cover), Facebook (post, cover), YouTube (thumbnail, channel art), Google My Business (post). Each component lists exact dimensions, layout, type, color, image direction, and a worked example.

For the foundational tokens, load `01-tokens.md` and `02-color.md` first.

## Instagram

### IG feed — single image (4:5 portrait)

**Dimensions:** 1080×1350px
**Surface token:** `surface.social.igFeed`
**Use:** Daily/weekly feed posts that aren't carousels — sermon clips, recap photos, quote cards, event announcements.

**Layout grid:**
- Outer margin: 80px on all sides
- Title block (when type-driven): top third, max 70% width
- Page indicator / brand mark: bottom-right, 60px diameter L© badge

**Variants:**

**a) Photo with caption overlay** — documentary candid photo full-bleed, optional gradient overlay (40% black from bottom) for type contrast. Headline in `lc-cream`, `lc-fs-headline-2` (40px), `lc-fw-black`. Use the italic-accent rule when emotional.

**b) Quote card on cream** — `lc-cream` background, headline + attribution stacked. Headline at `lc-fs-headline-1` (56px) in `lc-ink`, italic accent on the resonant word. Inset photo of the speaker bottom-right at 360×360px. L© badge bottom-left at 60px.

**c) Stat card on pink** — `lc-pink-loud` background, single big number at `lc-fs-display-1` in `lc-cream`, label below at `lc-fs-micro` `lc-fw-bold` `lc-tracking-caption`.

### IG story (9:16)

**Dimensions:** 1080×1920px
**Surface token:** `surface.social.igStory`
**Use:** Time-sensitive announcements, sermon teasers, behind-the-scenes, repost amplification.

**Safe area:**
- Top 250px: Instagram UI (profile, story progress) — atmosphere only
- Bottom 250px: Instagram UI (reply, react) — atmosphere only
- Critical content: 1080×1420 centered band

**Layout grid:**
- Outer margin: 80px L/R within safe band
- Headline anchored at top of safe band; CTA pill anchored 250px above bottom of safe band

**Variants:**

**a) Plan Your Visit / event story** — `lc-pink-loud` full-bleed background, "PLAN YOUR / VISIT" stacked at `lc-fs-display-1` in `lc-cream`, italic-accent on emotional word. CTA pill at bottom: cream background, ink text, "JOIN US SUNDAY 9A + 11A".

**b) Teaser story** — full-bleed photo (B&W halftone), short headline at top in `lc-cream`, L© badge bottom-center as the closer.

**c) Repost amplification** — original post inset at center on cream, with caption banner above ("FROM @AUTHOR") and CTA pill below.

### IG carousel slide (1:1 square)

**Dimensions:** 1080×1080px each slide (3–10 slides)
**Surface token:** `surface.social.igSquare`
**Use:** Sundays at Love recaps, Bible-teaching mini-series, event walkthroughs, multi-point announcements.

**Layout consistency** is essential. Every slide in a carousel uses the same grid, same footer, same indicator.

**Standard slide structure:**
- Top label: 32px tall, `lc-cream` on `lc-pink-loud` ribbon, "SUNDAYS AT LOVE • 5/3/26" in caption caps
- Content area: 80px margin all sides
- Bottom indicator: page count "01/05" at `lc-fs-micro` left + L© badge 40px right

**Slide types within a carousel:**

| Slide # | Purpose | Treatment |
|---|---|---|
| 1 (cover) | Hook | Photo or stat — strong visual, headline italic-accent |
| 2–4 (body) | Content | Single point per slide, type-led |
| Last (CTA) | Close | Pink fill, `lc-cream` CTA copy + pill, "@lovechurchomaha" handle |

### IG reel cover

**Dimensions:** 1080×1920 with safe area at 1080×1350
**Use:** Cover image visible in IG grid before reel autoplays.

Spec mirrors IG story but **all critical content must fit within the central 1080×1350 area** so it reads on the 4:5 grid crop.

## Facebook

### FB feed post

**Dimensions:** Use IG feed asset 1080×1350 — it scales appropriately on FB.

### FB cover photo

**Dimensions:** 1640×856
**Surface token:** `surface.social.fbCover`
**Use:** Page cover. Updates ~1×/quarter or per major series/season.

**Layout:**
- Subject in central 1200×600 (FB crops differently on mobile vs desktop)
- Type minimum at `lc-fs-headline-1` so it reads on mobile
- Don't put critical info in the bottom 200px (FB UI overlap)

**Default treatment:** B&W halftone photo of worship moment + heroic display headline in `lc-cream` + L© badge.

## YouTube

### YT thumbnail

**Dimensions:** 1280×720 (16:9)
**Surface token:** `surface.social.ytThumb`
**Use:** Sermon uploads, music videos, sermon clips, podcast episodes.

**Layout grid:**
- Subject in left 60% of frame
- Title block right or overlaid on bottom-third gradient
- L© badge bottom-right, 80px

**Type spec:**
- Title at `lc-fs-headline-1` (56px) in `lc-fw-black`, `lc-cream` on photo
- Sub-label (series name, episode #) at `lc-fs-caption`, tracked, in `lc-pink-loud` for series-pop
- Italic-accent on the emotional word in the title (e.g., "When God Feels *Distant*")

**Variants:**

**a) Sermon thumbnail** — pastor mid-message photo, title overlaid right or bottom, series label in pink top-left.

**b) Worship video thumbnail** — wider shot of band/leader, song title centered or left, "L© WORSHIP" label.

**c) L© Stories thumbnail** — subject's headshot on white seamless or in-context, "L© STORIES" label top-left in pink, name at `lc-fs-headline-2`.

### YT channel art

**Dimensions:** 2560×1440 (safe area 1546×423 visible on all devices)
**Use:** Channel header. Updates ~1–2×/year.

**Layout:**
- All critical content in 1546×423 center safe area
- Wordmark/headline center-aligned
- Subhead with service times or signature phrase

**Default:** B&W halftone worship hero + "EXPERIENCE GOD'S BEST FOR YOUR LIFE" in `lc-cream` `lc-fs-headline-1` + L© badge centered or right-anchored.

## Google My Business (GMB)

### GMB post

**Dimensions:** 1200×900 (4:3)
**Surface token:** `surface.social.gmbPost`
**Use:** Weekly Thursday post per Jordan Johnson's cadence (see `gmb-weekly-post` skill for content recipe).

**Layout grid:**
- Outer margin: 80px all sides
- Title block top half
- Photo or fill bottom half
- CTA copy as part of the post body, not embedded in graphic

**Type spec:**
- Headline at `lc-fs-headline-2` (40px) in `lc-fw-black`
- Subhead at `lc-fs-body` (18px) `lc-fw-medium`
- Day/time labels at `lc-fs-caption`, tracked, in `lc-pink-loud`

**Variants:**

**a) "Sundays at Love" GMB** — split layout: cream type block left + worship photo right. Headline "JOIN US SUNDAY" with italic accent on "SUNDAY".

**b) Event GMB** — full-bleed pink background, big event name in cream display, time/location underneath.

**c) Sermon highlight GMB** — B&W halftone photo of the message moment, title overlay, "WATCH NOW" CTA pill at bottom.

## Cross-platform export checklist

When generating any social asset, the spec returned to the user MUST include:

1. **Exact dimensions** (1080×1350, not "around 1080")
2. **File format** (JPG quality 85 for photo-led, PNG for type-led)
3. **Color profile** (sRGB for screen)
4. **File name** (see `14-spec-and-handoff.md`)
5. **Image direction** (mode, subject, lighting, crop)
6. **Type spec** (typeface, weight, size, tracking, case, color, italic-accent)
7. **Component callouts** (which slot is the headline, the CTA, the indicator)
8. **Token names** (cite, don't just give values)

## Worked example

**Request:** "Make me an IG story for Plan Your Visit this Sunday."

**Response:**

```
Surface:    IG story (surface.social.igStory) — 1080×1920px
Background: lc-pink-loud (#F0238D), full bleed
Headline:   "PLAN YOUR / VISIT" stacked
            • Type: lc-font-display, lc-fw-black, lc-fs-display-1 (96px)
            • Color: lc-cream
            • Tracking: lc-tracking-display-tight (-0.030em)
            • Leading: lc-lh-display-tight (0.92)
            • Italic accent: none (this is a directive, not emotional)
            • Position: top of safe band, 80px L margin
Subhead:    "SUNDAY 9:00A + 11:00A"
            • Type: lc-font-display, lc-fw-bold, lc-fs-title (28px)
            • Color: lc-cream
            • Tracking: lc-tracking-caption (+0.060em)
            • Position: 64px below headline
Address:    "20120 Blue Sage Pkwy"
            • Type: lc-fs-body (18px), lc-fw-roman
            • Color: lc-cream at 80% opacity
            • Position: 32px below subhead
CTA pill:   "WATCH ONLINE 5P"
            • Background: lc-cream
            • Text: lc-ink at lc-fs-caption, lc-fw-bold, lc-tracking-caption
            • Padding: lc-space-md vertical / lc-space-xl horizontal
            • Position: 320px above bottom of canvas (250px safe + 70px breath)
L© badge:   60px diameter, cream-on-pink lockup, bottom-right
File name:  ig-story_plan-your-visit_2026-05-10.png
Export:     PNG, sRGB, 1080×1920px exactly
```

This is the standard output shape — it should be self-contained enough that any V/I Team member can build it without asking follow-ups.
