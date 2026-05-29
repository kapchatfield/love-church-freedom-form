# 03 — Typography

Type carries the Love Church brand. Color is bold; photo is documentary; layout is gridded. But it is the **type** that gives every piece its voice. Two typefaces do the entire system. Get the pairing right and the rest of the brand falls into place behind it.

## The pairing

**`lc-font-display`** — Neue Haas Grotesk Display
The workhorse. Display headlines, body, captions, labels. All weights from Light through Black. Tight tracking on caps (the Core Style spec is `-20`, deepening to `-30` at heroic display sizes).

**`lc-font-accent`** — Apple Garamond
The emotional accent. Italic only. Used for *one* word in a headline, for pull quotes, and for the rare moment you want a piece to pause and breathe. Roman / regular Garamond does **not** appear in the system — only the italic.

**Why two typefaces, not three:**
The system is editorial. The contrast between a heroic black sans-serif and a delicate italic serif IS the voice. Adding a third typeface (a script, a slab, a different sans) makes the system look like decoration. Hold the line.

## The italic-accent rule (signature pattern)

Love Church headlines on the public web follow a recurring pattern: **all-caps Neue Haas display + one italicized accent word in Apple Garamond.** The accent word is the emotional payload — the line *breathes* on it.

Examples pulled live from lovechurch.org:

> There's More **<em>To Life</em>**
> Real People, **<em>Real Life</em>**
> Engaging Encounters **<em>for all Ages</em>**
> Simple Teaching **<em>through the Bible</em>**
> Ever feel like **<em>there should be more?</em>**
> The gameplan is **<em>simple.</em>**
> Ready to **<em>Experience More?</em>**

When to use the italic-accent rule:
- Web heroes, IG carousel covers, sermon teaser graphics, email subject blocks — anywhere the headline carries emotional weight.
- The italic word is usually the *promise* or the *invitation* in the line. Pick the word the audience needs to feel.

When NOT to use the italic-accent rule:
- Section openers in stat-heavy contexts (ENCOUNTERS, LOVE OUT LOUD) — these stay all-caps Neue Haas, no italic. The information is the emotion.
- Short labels and microcopy — too much weight for a small phrase.
- Anywhere the italic would force a line break that breaks the layout.

**Implementation:**

```html
<h1 class="lc-display-2">
  Real People,
  <span class="lc-accent-italic">Real Life.</span>
</h1>
```

The italic span doesn't need its own size — it inherits from the headline. It does need to retain its serif character; don't substitute a sans italic. If Apple Garamond is unavailable, EB Garamond (Google Fonts) is the closest free fallback.

## The body emphasis pattern

In long-form editorial body — the More To Life Story pages in the Annual, blog posts on lovechurch.org, MailChimp body — certain phrases are inline-bolded for emphasis. This is a deliberate device that gives the text a "scan path" for skim readers.

From the Annual (MEET ALYSSA story page):

> Alyssa spent most of her life **knowing about Jesus—but not truly knowing Him**. Growing up in an unstable home, she carried **anxiety, sadness, and fear** from an early age...

The bolded phrases are the *emotional and narrative beats*. A reader skimming the bolded fragments alone gets the whole story arc. This is the body's parallel to the italic-accent rule in display: where display whispers with italic, body shouts with bold.

Use `lc-fw-medium` (500) — not `lc-fw-bold` (700). The 500 weight punches without screaming. Bold (700) should be reserved for subheads.

## Type scale and use

| Token | Size | Surface examples |
|---|---|---|
| `lc-fs-display-1` (96px) | Annual cover, large-format posters | Cover headlines — ANNUAL REPORT, ENCOUNTERS, LOVE OUT LOUD |
| `lc-fs-display-2` (72px) | Section openers, IG carousel cover at full bleed | Stat-page section labels, large IG quote cards |
| `lc-fs-headline-1` (56px) | IG feed cover, web hero | Series art titles, web hero headline |
| `lc-fs-headline-2` (40px) | Story page headline | "MEET ALYSSA," "MEET MATT" — name reveals |
| `lc-fs-title` (28px) | Sub-section, IG quote line | Pull quotes in their own block |
| `lc-fs-lead` (22px) | Lead paragraph (in pink), pull quote | The first paragraph of an editorial story |
| `lc-fs-body` (18px) | Default body | Long-form reading |
| `lc-fs-body-tight` (16px) | Two-column editorial, email | Annual interior body, MailChimp |
| `lc-fs-caption` (14px) | Section labels, footer | "MORE TO LIFE STORY" labels |
| `lc-fs-micro` (12px) | Stat block labels, page numbers | "LOVES TOTAL," "5/16" |

Don't invent in-between sizes. If 56px is too big and 40px is too small, the layout is asking for adjustment, not a new size.

## Tracking (letter-spacing)

Tracking changes more than size at the display level. Get tracking wrong and the whole headline reads sloppy.

| Token | Value | Where |
|---|---|---|
| `lc-tracking-display-tight` | -0.030em | Display-1 caps. The heroic tightening that gives "ANNUAL REPORT" its punch. |
| `lc-tracking-display-default` | -0.020em | Display-2 / headline caps. The Core Style spec value. |
| `lc-tracking-body` | 0 | Default body. |
| `lc-tracking-caption` | +0.060em | All-caps section labels. The editorial open-spacing that makes "MORE TO LIFE STORY" sit right above a 40px headline. |

In InDesign units: `-30`, `-20`, `0`, `+60` (which is what the Core Style PDF uses). Translation: tracking in CSS uses em; in InDesign, divide by 1000.

## Leading (line-height)

| Token | Value | Where |
|---|---|---|
| `lc-lh-display-tight` | 0.92 | Stacked all-caps display where lines should kiss. ANNUAL/REPORT. WE/ARE/SELF-FED. |
| `lc-lh-headline` | 1.05 | Single-line or short stacked headlines. |
| `lc-lh-body` | 1.45 | Body. Generous, reading-friendly. |
| `lc-lh-tight` | 1.20 | Compressed runs — captions, footers. |

The tight 0.92 leading on stacked caps is part of the brand's editorial discipline. Don't soften it.

## Weights — when to use which

| Weight | When |
|---|---|
| `lc-fw-thin` (100) | Reserved. Don't reach for. |
| `lc-fw-light` (300) | Body at very small sizes (10–12px) when 400 looks too heavy. |
| `lc-fw-roman` (400) | Default body. |
| `lc-fw-medium` (500) | **Inline body emphasis only.** This is the "bolded phrase" pattern. |
| `lc-fw-bold` (700) | Subheads, label caps, button text, stat-block labels. |
| `lc-fw-black` (900) | Display headlines. The heroic treatment. The brand's loudest type voice. |

A trap: don't use 700 for display. The brand's display voice is 900 — anything lighter looks under-confident. The Core Style PDF specifies `Bold` for headers and that maps to the **heaviest available bold**, which in the Neue Haas Grotesk family is the Black weight.

## Numbers

Stats are heroic in this system. The huge numbers on the ENCOUNTERS and LOVE OUT LOUD pages are display-2 size (72px) in `lc-fw-black`, with a tiny tracked-out caps label below. The pattern:

```
[BIG NUMBER in lc-fw-black, lc-fs-display-2, line-height: 1]
[Tiny caps label in lc-fw-bold, lc-fs-micro, lc-tracking-caption]
```

For dollar amounts, use the editorial pattern from LOVE OUT LOUD: dollar sign at smaller weight, decimal subscript:

```
$425,760.24
   └ "425,760" at full size
   └ "$" prefix at ~70% size, baseline-aligned
   └ ".24" at ~50% size, baseline-aligned (subscript-like)
```

This is the magazine-stat treatment. It signals "this is data" while keeping the number heroic.

## Captions, labels, and footers

The caption layer is small but everywhere. Get it consistent and the brand reads tight.

- **Section labels** (e.g., "MORE TO LIFE STORY" above a story headline): `lc-caption` with `lc-tracking-caption` and `lc-fw-bold`. All caps. Always.
- **Footer page numbers**: `lc-fs-micro` in `lc-fw-bold`, all caps if they include a label ("5/16" no label).
- **Stat labels under big numbers**: `lc-fs-micro` in `lc-fw-bold`, `lc-tracking-caption`, all caps.
- **Image captions**: `lc-fs-caption` in `lc-fw-roman` (not bold). Reading copy under photos.

## Common mistakes

1. **Using a third typeface.** "Just for this one piece." No. The system is two typefaces. If the design needs a script feel, it doesn't fit this system — this skill isn't the right tool for it.
2. **Mixing italic and roman Garamond.** Only italic appears. Roman Garamond looks like a different typeface in context.
3. **Setting display headlines below 900 weight.** Bold (700) display headlines look hesitant. The brand's voice is the Black weight.
4. **Using bold (700) for inline emphasis in body.** Use medium (500). Bold reads as a subhead.
5. **Forgetting tracking.** A `-20` headline at 56px reads completely different from a `0` headline at 56px. The system specifies tracking; honor it.
6. **Italicizing a whole headline.** The italic is *one word* — the accent. Italicizing the whole line collapses the contrast that makes the system work.

## Pre-flight check

Before delivering any spec that includes type:

- Did I name the typeface, weight, size, and tracking? All four.
- Did I follow the italic-accent rule on emotional headlines, and skip it on stat-page headlines?
- Did I use 500 (medium) for inline body emphasis, not 700 (bold)?
- Did I use the named token (`lc-fs-headline-1`) instead of the raw value (`56px`)? Names compound.
