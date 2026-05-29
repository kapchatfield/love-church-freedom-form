# 12 — Components: Email (MailChimp)

Specs for the all-church weekly email and any Love Church transactional or campaign email sent through MailChimp. Email is the most-read surface in the brand week-to-week — it earns careful design.

For the email content recipe (Celebrate · Connect · Invite rhythm), use the `weekly-email-newsletter` skill. This file specs the **visual**.

## Container

- Max width: **600px** (MailChimp default mobile-first)
- Background: `lc-cream` (the canvas)
- Body padding: `lc-space-lg` (24px) inside content blocks
- Block separation: `lc-space-xl` (32px) between blocks

## Header block

**Dimensions:** 600×120
**Layout:**
- Background: `lc-cream`
- L© badge centered, 80px
- Tagline below at `lc-fs-caption` `lc-fw-bold` `lc-tracking-caption` `lc-pink-loud`: "EXPERIENCE GOD'S BEST FOR YOUR LIFE"
- Hairline rule below tagline (`lc-rule-hairline` `lc-rule` color)

## Hero block

**Dimensions:** 1200×600 source (renders at 600×300 in column)
**Layout:**
- Full-bleed photo OR pink fill
- Headline overlay at center or bottom-anchored
- Optional CTA pill embedded

**Type:**
- Headline: `lc-fs-headline-1` (56px) in `lc-fw-black`, italic-accent rule applies
- Subhead: `lc-fs-title` (28px) in `lc-fw-medium`
- CTA pill: `lc-pink-loud` fill / `lc-cream` text or vice-versa depending on background

## Body content block

**Dimensions:** 600×N (height variable)
**Layout:**
- Background: `lc-cream`
- Padding: `lc-space-lg` all sides
- Section label at top: `lc-fs-caption` `lc-fw-bold` `lc-tracking-caption` `lc-pink-loud`
- Section headline: `lc-fs-headline-2` (40px) `lc-fw-black`
- Body: `lc-fs-body-tight` (16px) `lc-fw-roman` `lc-lh-body`
- Inline emphasis: `lc-fw-medium` (NOT bold)
- Pull quote: `lc-font-accent` italic at `lc-fs-lead` (22px) in `lc-pink-loud`

## Three-up block

A common pattern: three side-by-side cards with image, headline, CTA.

**Layout (desktop):**
- 3 columns, each 180px wide with `lc-space-md` (16px) gutter
- Each card: photo top (180×135 4:3), title `lc-fs-caption` `lc-fw-bold`, body 2-line `lc-fs-micro`, CTA "Read more ›"

**Layout (mobile):**
- Stack vertically, full 552px width per card

## CTA block

**Dimensions:** 600×200
**Layout:**
- Background: `lc-pink-loud` (default) or `lc-ink`
- Heroic CTA copy at `lc-fs-headline-2` in `lc-fw-black`, `lc-fg-inverse`
- Italic-accent rule applies
- Pill button below: `lc-cream` fill / `lc-ink` text

## Footer block

**Dimensions:** 600×280
**Layout:**
- Background: `lc-ink`
- Padding: `lc-space-2xl` (48px) vertical, `lc-space-lg` horizontal
- L© badge top-center 60px
- Tagline below: "Love Church · 20120 Blue Sage Pkwy, Omaha, NE 68130 · 402.305.7717"
- Social row: @lovechurchomaha · YouTube · App
- Unsubscribe link at `lc-fs-micro` `lc-cream` 60% opacity

## Email-safe color overrides

Some email clients render hex inconsistently. The system tokens include email-safe fallbacks:

| Token | Email-safe |
|---|---|
| `lc-pink-loud` | `#F0238D` (verified in Gmail, Apple Mail, Outlook 365) |
| `lc-cream` | `#EEE4D3` |
| `lc-ink` | `#151515` |

If a client (Outlook desktop) breaks gradients or rounded buttons, fall back to:
- Solid color buttons (no gradient)
- Square buttons with `lc-radius-md` (8px) instead of pill
- Image-replaced headlines for hero where custom font support is critical

## Type rendering note

Email clients vary wildly in font support. Web fonts work on most modern clients but **not** Outlook desktop. The fallback chain in `lc-font-display` handles this — Inter > Helvetica Neue > Arial — all of which preserve a similar editorial feel without breaking layout.

For body text, use system fallbacks. For display headlines on hero blocks, **embed as image** for guaranteed rendering on Outlook + older clients. Image headlines should be retina (2× the rendered size) and saved as PNG with alt text.

## Worked example

**Request:** "Build me a MailChimp hero block for this weekend's announcement of Plan Your Visit."

**Response:**

```
Surface:    MailChimp hero — 1200×600 source @ 600×300 render
Background: full-bleed photo — documentary candid worship moment, B&W halftone treatment
Overlay:    40% black gradient from bottom for type contrast
Headline:   "Plan Your Visit"
            • Type: image-rendered as PNG (Outlook safety)
            • At 2x: lc-font-display, lc-fw-black, lc-fs-headline-1 (56px → 112px @2x)
            • Color: lc-cream
            • Italic accent on "Visit": lc-font-accent italic
            • Tracking: lc-tracking-display-default
            • Position: bottom-center, 64px above bottom edge
Subhead:    "SUNDAY 9A + 11A · IN-PERSON OR ONLINE"
            • Type: live HTML, lc-font-display fallback chain
            • Size: lc-fs-caption (14px) lc-fw-bold lc-tracking-caption
            • Color: lc-cream
            • Position: 16px below headline
CTA pill:   "GET STARTED"
            • Background: lc-pink-loud
            • Text: lc-cream lc-fs-body lc-fw-bold lc-tracking-caption
            • Padding: 16/32 (lc-space-md / lc-space-xl)
            • Radius: lc-radius-pill (or lc-radius-md fallback for Outlook)
            • Position: centered, 24px below subhead
File name:  email-hero_plan-your-visit_2026-05-10.png
Export:     PNG, sRGB, 1200×600 (2x for retina would be 2400×1200)
```
