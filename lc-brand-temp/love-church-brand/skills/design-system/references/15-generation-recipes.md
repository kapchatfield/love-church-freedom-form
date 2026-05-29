# 15 — Generation recipes

The fastest path from "make me X" to a complete spec. Each recipe takes a common request, names the matching component, fills the tokens, and returns the spec. Use these as starting points — modify based on the specific message and audience.

For each recipe, the structure is:

```
Trigger phrases — what the user might say
Surface       — which component file to load
Tokens        — primary tokens used
Spec          — the canonical assembly
Variation     — how to flex if context differs
```

## Recipe 01 — Plan Your Visit IG story

**Trigger phrases:** "IG story for Plan Your Visit," "Sunday invite story," "first-time guest story"
**Surface:** `references/10-components-social.md` → IG story
**Tokens:** `lc-pink-loud`, `lc-cream`, `lc-fs-display-1`, `lc-fw-black`, `lc-fs-title`, `lc-fs-caption`

**Spec:**

- 1080×1920, full-bleed `lc-pink-loud`
- "PLAN YOUR / VISIT" stacked top of safe band, `lc-cream`, `lc-fs-display-1`, `lc-fw-black`, `lc-tracking-display-tight`, `lc-lh-display-tight`
- Subhead "SUNDAY 9:00A + 11:00A" `lc-cream` `lc-fs-title` `lc-fw-bold` `lc-tracking-caption`, 64px below
- Address 1 line `lc-fs-body` `lc-cream` 80% opacity, 32px below subhead
- Cream pill CTA "WATCH ONLINE 5P" 320px above bottom edge
- L© badge bottom-right 60px (cream-on-pink lockup)

**Variation:** if it's an outdoor / launch event, swap pink for a documentary candid photo with 40% bottom gradient overlay; everything else identical.

## Recipe 02 — Sundays at Love IG carousel

**Trigger phrases:** "Sunday recap," "this week's IG post," "Sundays at Love carousel," "weekly recap"
**Surface:** `references/10-components-social.md` → IG carousel slide
**Tokens:** see recipe — multi-slide; tokens vary per slide
**Notes:** This pairs with the `ig-sundays-recap` skill for content; this recipe specs the visual.

**Spec (5-slide template):**

- **Slide 1 (cover):** 1080×1080, full-bleed photo (documentary candid worship moment), 40% bottom gradient. Headline `lc-cream` `lc-fs-headline-1` italic-accent on emotional word. Top ribbon `lc-pink-loud` 32px tall with "SUNDAYS AT LOVE • [DATE]" `lc-cream` `lc-fs-caption` tracked.
- **Slide 2–4 (body):** 1080×1080 `lc-cream` background. Each slide: section label tiny pink caps, headline `lc-fs-headline-2` `lc-fw-black`, body `lc-fs-body` `lc-fw-roman` with inline `lc-fw-medium` emphasis on key phrases. Optional inset photo bottom-half.
- **Slide 5 (CTA close):** full-bleed `lc-pink-loud`. Cream caps headline ("EXPERIENCE GOD'S BEST FOR YOUR LIFE"). Cream pill CTA: "PLAN YOUR VISIT". L© badge bottom-center 80px.
- **Footer (every slide):** "01/05" page indicator `lc-fs-micro` left, L© badge 40px right, in matching color depending on background.

## Recipe 03 — YouTube sermon thumbnail

**Trigger phrases:** "YouTube thumbnail," "sermon video thumbnail," "thumbnail for [pastor]'s message"
**Surface:** `references/10-components-social.md` → YT thumbnail
**Tokens:** `lc-cream`, `lc-pink-loud`, `lc-ink`, `lc-fs-headline-1`, `lc-fw-black`

**Spec:**

- 1280×720, photo of the pastor mid-message in left 60% of frame
- Photo treatment: documentary candid color (warm cast, natural light), slight darkening on right third for type contrast
- Series label top-left corner: "[SERIES NAME] · WK [N]" `lc-fs-caption` `lc-fw-bold` `lc-tracking-caption` in `lc-pink-loud`
- Title overlaid right or bottom: `lc-fs-headline-1` `lc-fw-black` `lc-cream`, italic-accent on the emotional/pivot word
- L© badge bottom-right 60px

**Variation A — Worship video:** wider band/leader shot, song title centered, "L© WORSHIP" pink label.
**Variation B — L© Stories:** subject on white seamless or in-context, "L© STORIES" top-left in pink, name at `lc-fs-headline-2`.
**Variation C — Highlight clip:** B&W halftone of moment, "1-MINUTE CLIP" pink label, single-line clip title.

## Recipe 04 — MailChimp weekly newsletter hero

**Trigger phrases:** "weekly email hero," "MailChimp hero," "all-church email banner"
**Surface:** `references/12-components-email.md` → hero block
**Pairs with:** `weekly-email-newsletter` skill (content)

**Spec:**

- 1200×600 source rendered at 600×300 column width
- Background: full-bleed photo (documentary candid) with 40% bottom gradient OR full `lc-pink-loud`
- Headline rendered as PNG (Outlook safety): "[Weekly theme]" with italic-accent rule, `lc-fs-headline-1` at 2x = ~112px source, `lc-cream`
- Subhead live HTML: 1-line context, `lc-fs-caption` `lc-fw-bold` tracked caps `lc-cream`
- CTA pill: `lc-pink-loud` fill (or `lc-cream` if hero is pink) with cream/ink text "READ MORE" or specific weekly CTA
- File: PNG, sRGB, 1200×600 (retina would be 2400×1200)

## Recipe 05 — Google My Business weekly post

**Trigger phrases:** "GMB post," "Google Business post," "Thursday GMB"
**Surface:** `references/10-components-social.md` → GMB post
**Pairs with:** `gmb-weekly-post` skill (content)

**Spec:**

- 1200×900, split layout: cream type block left + worship documentary photo right
- Headline left: "JOIN US *SUNDAY*" italic-accent, `lc-fs-headline-2` `lc-fw-black` `lc-ink`
- Day/time line: "9:00A + 11:00A · IN-PERSON OR ONLINE" `lc-fs-body` `lc-fw-medium`
- Location line: "20120 BLUE SAGE PKWY, OMAHA" `lc-fs-caption` `lc-fw-bold` `lc-tracking-caption` `lc-pink-loud`
- L© badge bottom-left of type block, 60px
- Photo right: documentary candid worship moment, 4:3 crop

## Recipe 06 — Sermon series art (single key art)

**Trigger phrases:** "sermon series art," "key art for [series]," "series cover"

> Note: sermon series art was scoped OUT of this skill's surfaces. If the request comes in, route to the V/I Team's series-art skill (TBD) OR generate a directional reference using the system tokens, with a flag that this is **directional only** and the official series art will live elsewhere.

**Directional spec when forced:**

- 2880×1620 (web hero) or 1080×1350 (IG feed cover)
- B&W halftone hero photo of a person, place, or moment that visually anchors the theme
- Series title in `lc-fs-display-1` `lc-fw-black` `lc-cream`, italic-accent if title carries emotion
- "A [N]-WEEK SERIES" label below in `lc-fs-caption` `lc-fw-bold` `lc-tracking-caption` `lc-pink-loud`
- L© badge bottom-right 80px

## Recipe 07 — Web hero block

**Trigger phrases:** "web hero," "homepage hero," "lovechurch.org hero"
**Surface:** `references/11-components-web.md` → hero

**Spec:**

- Desktop 2880×1620 source
- Full-bleed photo with 40% bottom gradient, OR cream type-only with L© badge anchor
- Headline `lc-fs-display-2` desktop / 48px mobile, italic-accent rule applies
- Subhead `lc-fs-lead` `lc-fw-roman` max-width 480px
- Pink pill CTA "PLAN YOUR VISIT" or context-specific
- Padding `lc-space-5xl` top, `lc-space-3xl` bottom desktop
- Mobile stack: headline scales down, padding `lc-space-3xl` / `lc-space-xl`

## Recipe 08 — Plan Your Visit web module

**Trigger phrases:** "Plan Your Visit module," "first-time guest section," "homepage CTA block"
**Surface:** `references/11-components-web.md` → Plan Your Visit module

**Spec:**

- Full-bleed `lc-pink-loud`
- Headline "Plan Your *Visit*" italic-accent, `lc-fs-display-2` `lc-fw-black` `lc-cream`
- Service times in column right: "SUNDAY / 9:00A + 11:00A" stacked, `lc-fs-title` `lc-fw-bold` `lc-cream`
- Address inline below times
- Pill CTA "GET STARTED" — `lc-cream` fill, `lc-ink` text
- Optional small map or photo aside

## Recipe 09 — Quote card (IG feed)

**Trigger phrases:** "quote card," "pull quote graphic," "quote from [pastor]"
**Surface:** `references/10-components-social.md` → IG feed → quote card variant

**Spec:**

- 1080×1350
- Background: `lc-cream`
- Quote at center: `lc-font-display` mixed case at `lc-fs-headline-1` `lc-fw-roman` (lighter than display headlines — this is a quote, not a slogan), italic-accent rule on the resonant phrase
- Attribution below quote: small caps `lc-fs-caption` `lc-fw-bold` `lc-tracking-caption` `lc-pink-loud` — "—PASTOR MIKE / SUNDAY 5/3"
- Inset photo bottom-right of speaker, 360×360, soft drop position
- L© badge bottom-left 60px

## Recipe 10 — Stat-page section opener (Annual / longform)

**Trigger phrases:** "stat page," "Annual section opener," "data graphic page"
**Surface:** `references/04-grid-and-layout.md` → section openers

**Spec:**

- Full-bleed `lc-pink-loud`
- Section title `lc-fs-display-1` `lc-fw-black` `lc-cream` top of page (e.g., "ENCOUNTERS")
- Stat blocks in 3-column grid: each with hairline rule above, sub-section label, then 3 stats horizontally separated by hairline rules
- Each stat: huge number `lc-fs-display-2` `lc-fw-black` cream + tiny label `lc-fs-micro` `lc-fw-bold` `lc-tracking-caption` cream
- Page footer (multi-page): page number / L© badge in cream

## How to use these recipes

When a request comes in:

1. **Find the closest recipe** by trigger phrase.
2. **Take the recipe spec** as the starting point.
3. **Customize** based on the specific message and audience — accent word in the headline, color choice if photo or fill, etc.
4. **Return the spec** in the 8-block handoff format from `references/14-spec-and-handoff.md`.
5. **Cite the recipe number** so future requests can reference it ("This is Recipe 01 with a photo background instead of pink fill").

If no recipe fits, build from tokens + components and **add the new pattern as Recipe 11+** when it's likely to recur.
