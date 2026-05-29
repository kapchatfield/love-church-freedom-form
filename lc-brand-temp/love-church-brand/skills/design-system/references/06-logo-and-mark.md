# 06 — Logo & mark

The Love Church mark is **the L© badge** — a circular form with the letter "L" at center and the orbital text *EXPERIENCE GOD'S BEST FOR YOUR LIFE* wrapped around it, with a small upward arrow. The mark works two ways: as a **standalone badge** AND as an **inline typographic glyph** that substitutes for the letter "L" in the word it precedes (e.g., "L© Online," "L© Stories," "L© India").

Both uses are in the system. Both are distinct. Don't confuse them.

## The badge

The full standalone mark. Circular composition, ~1:1 aspect.

**Anatomy:**
- **Outer orbital ring** — the wordmark "EXPERIENCE GOD'S BEST FOR YOUR LIFE" set in caps, tracked tight, wrapping clockwise from the upper left.
- **Center letter** — capital "L" set in Neue Haas Grotesk Display Black.
- **Arrow** — small upward arrow tucked next to or above the L, indicating ascent / aspiration.
- **Outline** — a single circular stroke at `lc-rule-regular`.

**Color variants:**
- **`lc-ink` on `lc-cream`** — primary lockup. The default everywhere body text is dark.
- **`lc-cream` on `lc-pink-loud`** — appears in pink pill components (the year badge on the Annual cover).
- **`lc-cream` on dark photo** — hero treatments where the badge sits over photography.
- **`lc-pink-loud` on `lc-cream`** — used in the Reading Guide title block. Loud and editorial.

The mark is **always** monochrome. Never multi-color. The orbital text and the L are always the same color in any given lockup.

**Sizing minimums:**

| Surface | Minimum diameter |
|---|---|
| Print | 0.5 inch (~36px at 72dpi) |
| Web | 32px |
| Social (overlay) | 60px |
| Page footer (Annual) | 28px |

Below the minimum, the orbital text becomes unreadable. Use the inline glyph instead at smaller scales.

**Clear space:**

Reserve clear space equal to **half the badge diameter** on all four sides. No type, no rule, no photo edge inside that space. The badge needs air to read as the brand mark.

## The inline glyph

When "L©" appears inside a typographic phrase — "L© Online," "L© Stories," "L© India" — the © character substitutes for the orbital ring. Visually it reads as "L with a small circle next to it." It functions as the L sound + the brand mark in one glyph.

This is a unique pattern — most brands keep their mark separate from typography. Love Church integrates the two, and it's part of what makes the system distinctive.

**Where it appears:**

- **L© Online** — the digital arm of the church
- **L© Stories** — short-form testimonial content
- **L© India** — the international outreach
- **L© Worship** — when worship-team content needs the inline brand mark
- Any "L-word" sub-brand where the inline glyph reinforces the parent identity

**Treatment:**
- The "L" is set in the same typeface and weight as the surrounding word (Neue Haas Grotesk Display, Black for display caps; Bold for caption caps).
- The "©" is the standard copyright symbol from the same typeface — no custom glyph needed at most sizes.
- At display scale, the `©` sits at ~70% of the cap height, vertically centered.
- Tracking between "L" and "©" is tight (-30 / -0.030em) so they read as a single mark, not two characters.

**When NOT to use the inline glyph:**

- General body text. "L© Online" appears in headlines and section titles, not in the middle of a paragraph about the online ministry.
- Sub-brands without the church's explicit naming convention. Don't invent "L© Coffee" or "L© Volunteers" without alignment.
- When the surrounding type isn't Neue Haas Grotesk Display. The glyph belongs to the system's typeface.

## Lockups

A "lockup" is a fixed combination of the mark plus other elements. The system has three.

### Lockup 1: Pill badge with year

Appears on the Annual cover. The wordmark "LOVE CHURCH" sits centered in a `lc-pink-loud` pill, with the L© badge tucked into the left end of the pill and the year ("2023" / "2026") right-aligned at the right end.

```
[L©][              LOVE CHURCH              ][ 2026 ]
└────────────────────── lc-pink-loud pill ──────────────────────┘
```

- Pill background: `lc-pink-loud`
- All type: `lc-cream`
- L© badge: cream-on-pink lockup
- Pill height ~`lc-space-3xl` (64px) at hero scale, scaling down to `lc-space-2xl` (48px) at section scale

### Lockup 2: Mark + page indicator (footer)

The Annual page footer. L© badge in the bottom-outer corner with page number (e.g., "5/16") inset on the inner side.

```
[ LOVECHURCH.ORG | 2026 | LOVE CHURCH OMAHA | 5/16 ][L©]
```

- Mark size ~28px
- All footer type at `lc-fs-micro`, `lc-fw-bold`, `lc-tracking-caption`

### Lockup 3: Standalone hero badge

Centered on a hero card or end card of a video. The badge alone, ~25–35% of the canvas width, on `lc-cream` or `lc-ink`.

Use as the closing card on motion pieces, the avatar on social profiles (the IG profile picture is exactly this lockup), and the hero badge on Plan Your Visit confirmations.

## What NOT to do

1. **Don't recolor the mark.** No purple L©, no gold L©. The brand has its color logic — pink, cream, ink. That's it.
2. **Don't rotate or skew.** The orbital text reads clockwise from the upper left. Flipping or rotating it makes it illegible.
3. **Don't separate the L from the orbital ring** at badge scale. The two together are the mark.
4. **Don't use the badge inline with body text.** That's what the inline glyph (`L©`) is for. The badge is for hero placements.
5. **Don't combine the mark with another sub-brand mark** in a single lockup unless explicitly approved. The L© is the parent.
6. **Don't re-typeset the orbital text.** It's a fixed wordmark at this point — the kerning, the arrow, the alignment are part of the mark's identity. Use the official asset.

## Asset paths

The official badge file lives in the workspace fonts/brand asset folder. When generating a deliverable, the spec should point to the asset path, not embed an attempted recreation.

- **Master asset**: (to be confirmed with Adam — flag for assets/templates/ if not present)
- **Inline glyph spec**: any keyboard-typed "L©" set in `lc-font-display` at the surrounding weight, with `-0.030em` tracking between L and ©.

## Pre-flight check

When the L© appears in a deliverable:

- Is it the badge or the inline glyph? They serve different jobs.
- Is the color lockup one of the four approved: ink/cream, cream/pink, cream/photo, pink/cream?
- At this size, is the orbital text readable? If not, switch to the inline glyph.
- Is there at least half-diameter clear space around the badge?
- Did I use the official asset, not a recreation?
