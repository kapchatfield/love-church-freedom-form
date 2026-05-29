# 11 — Components: Web (lovechurch.org)

Specs for the lovechurch.org components — hero, cards, CTA blocks, navigation, footer, Plan Your Visit module. The web is where the italic-accent headline rule does its heaviest work; the homepage shows it on rotation.

## Hero

**Dimensions:**
- Desktop: 2880×1620 source (rendered at max-width 1280 with full-bleed background)
- Mobile: 750×1334 source

**Layout:**
- Full-bleed photo or color background
- Content container max-width 1280px, centered
- Headline anchored to bottom-third of container (gives photo room above)
- Padding: `lc-space-5xl` (128px) top, `lc-space-3xl` (64px) bottom on desktop; `lc-space-3xl` top, `lc-space-xl` bottom on mobile

**Type:**
- Headline: `lc-display-2` (72px desktop / 48px mobile), italic-accent rule applies
- Subhead: `lc-fs-lead` (22px), `lc-fw-roman`, max-width 480px
- CTA: pill button with `lc-pink-loud` fill, cream text, `lc-fs-body` `lc-fw-bold` caps tracked

**Background variants:**

**a) Photo hero** — documentary candid photo, gradient overlay 40% black from bottom for type contrast.

**b) Cream hero** — type-only on `lc-cream`, with the L© badge as the visual anchor right-side. Used for transitional moments (between series, off-season).

**c) Pink hero** — full-bleed `lc-pink-loud`, cream type, used for major announcements or campaign launches. Use sparingly.

## Section block

A repeating page section: a labeled module with a headline, body, optional photo, and CTA.

**Layout:**
- Padding: `lc-space-4xl` (96px) vertical on desktop, `lc-space-2xl` (48px) on mobile
- Container max-width 1280px
- Two-column at desktop (text left 7/12, photo right 5/12) — stack on mobile
- Section label above headline at `lc-fs-caption`, tracked, in `lc-pink-loud`
- Headline at `lc-fs-headline-1` (56px desktop / 36px mobile), italic-accent
- Body at `lc-fs-body` (18px), `lc-lh-body`, max-width 600px
- CTA: pill button, secondary outline style if subordinate to a hero CTA above

## Card

A small information unit: an event, a sermon, a group, a story.

**Dimensions:** 1200×900 reference (4:3) at full size; scales down for grids.

**Layout:**
- Photo at top: 4:3 documentary candid
- Body container with `lc-space-lg` (24px) padding
- Title at `lc-fs-title` (28px) `lc-fw-bold`
- Meta line at `lc-fs-caption` `lc-fw-medium` in `lc-pink-loud`
- Description at `lc-fs-body-tight` (16px), max 3 lines truncated with ellipsis
- Optional CTA "Read More ›" at `lc-fs-caption` `lc-fw-bold`

## Plan Your Visit module

The most-used CTA block on lovechurch.org. Shows up on the homepage, in the menu, and on the dedicated /plan-your-visit page.

**Default treatment:**
- Full-bleed `lc-pink-loud` background
- Heroic headline: "Plan Your *Visit*" — italic accent rule
- Service times in `lc-cream` `lc-fs-title` next to address
- Pill CTA in `lc-cream` fill / `lc-ink` text: "GET STARTED"
- Optional small map or photo to the side

## Navigation

**Desktop (top nav):**
- Background: `lc-cream` (or transparent on hero)
- Height: 80px
- Logo (L© badge) left at 48px diameter
- Nav links right: `lc-fs-caption` `lc-fw-bold` tracked caps, `lc-ink` color
- Active state: `lc-pink-loud` underline (1.5px) with `lc-space-sm` (8px) offset
- Primary CTA pill: "Plan Your Visit" right-anchored, `lc-pink-loud` fill

**Mobile (hamburger menu):**
- Background: `lc-cream`
- Height: 64px
- Logo left at 40px
- Hamburger icon right at 24px stroke 2px
- Drawer opens full-screen with `lc-pink-loud` background and cream nav links at `lc-fs-headline-2`

## Footer

**Layout:**
- Background: `lc-ink`
- Type: `lc-cream`
- Padding: `lc-space-3xl` (64px) vertical
- Three-column desktop: brand left / nav middle / contact right; stacked mobile
- L© badge top-left, 80px
- "Experience God's best for your life." tagline below badge at `lc-fs-body` italic
- Nav links at `lc-fs-caption` `lc-fw-bold` tracked caps
- Social handles inline as @lovechurchomaha · YouTube · Subsplash
- Copyright/address at `lc-fs-micro` at the bottom

## Form fields

When forms appear on lovechurch.org or via Typeform integration:

- Field background: `lc-paper`
- Field border: 1px `lc-taupe`
- Field text: `lc-ink` at `lc-fs-body`
- Label: `lc-fs-caption` `lc-fw-bold` `lc-tracking-caption` `lc-pink-loud`
- Submit: pill button, pink fill, cream caps copy

## Responsive breakpoints

| Breakpoint | Width | Container |
|---|---|---|
| Mobile | 320–767px | 100% with `lc-space-lg` padding |
| Tablet | 768–1023px | 720px |
| Desktop | 1024–1439px | 960px |
| Wide | 1440px+ | 1280px |

Type scales down at mobile per the desktop/mobile size pairs noted on each component.

## Pre-flight check

Before delivering a web component spec:

- Are dimensions tied to surface tokens (not invented)?
- Did I cite the breakpoint behavior?
- Did I use the italic-accent rule on emotional headlines?
- Is the dominant CTA on this surface a single pink-pill (not two)?
- Did I include both desktop AND mobile specs?
