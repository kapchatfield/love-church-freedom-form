# 02 — Color

The Love Church palette is a **two-load system**: the neutral core does the work; the loud accent does the emphasis. Most layouts are 90% neutral, 10% pink. When that ratio flips — as it does on stat pages and section openers — it flips fully and intentionally. There is no in-between.

## The neutral core

These five values carry the brand. If a layout uses only these, it is on-system.

### `lc-ink` — `#151515`

Near-black. Slightly warm. The default type color on cream surfaces and the default rule color. **Never** pure `#000000` — pure black reads colder than the system wants.

Use for:
- Body and display type on cream surfaces
- Horizontal rules
- Footer page numbers
- Default ink on any neutral page

Don't use for:
- Type on a pink-loud background (use `lc-cream` instead — pink + black is a combo we avoid because it's harsher than the system's voice)
- Drop shadows (the system doesn't use shadows; depth comes from layout, not blur)

### `lc-cream` — `#EEE4D3`

Primary cream. Slightly warm, slightly yellow. The default page background across nearly every neutral surface — the Annual interior, story pages, the Reading Guide, IG feed posts that aren't using a pink fill, lovechurch.org body.

Use for:
- Default page background
- Type color **on** a pink-loud or ink background
- Photo overlays at low opacity for warmth wash

### `lc-paper` — `#F3F1E5`

Off-white paper. Slightly cooler and lighter than cream. Use when you need cream's warmth but a touch more brightness — e.g., long-form body copy, the editorial story page where the photo and the type need maximum contrast.

The Annual story pages (MEET ALYSSA, etc.) use this. The Reading Guide's primary background is closer to cream.

### `lc-taupe` — `#B5A090`

Warm taupe. The bridge between ink and cream — sits between the neutral and the photo treatments. Used as a full-bleed background for the Annual TOC, secondary panels, and quieter announcement layouts.

Use for:
- TOC backgrounds
- Quieter section backgrounds when pink would be too loud
- Caption blocks under photos
- Muted panels in mixed layouts

### `lc-taupe-deep` — `#A39584`

A heavier taupe variant. The Annual TOC actually sits closer to this value. Use when taupe needs more weight — when the page has a lot of cream around it and the taupe block needs to anchor.

## The loud accent

### `lc-pink-loud` — `#F0238D`

The hot magenta-pink that defines Love Church visually. This is the brand's loudest lever. Used sparingly but boldly.

**Where it appears:**
- Year/CTA pills (e.g., the "LOVE CHURCH 2023" pill on the Annual cover; the "2026 READING GUIDE" pill on the Reading Guide)
- Section opener fills (ENCOUNTERS page in the Annual is a full pink bleed)
- Stat-page backgrounds (the L© Online stat block)
- Lead paragraph color on neutral pages (the editorial intro paragraph that sets up the story)
- Pull-quote color on neutral pages
- Big number color when stats sit on cream (LOVE OUT LOUD page)

**The rule:** when pink shows up, it's because something needs to land. If you can't name the thing it's emphasizing, the pink shouldn't be there.

**Pink load — how to think about it:**
- **Cream-loaded layout (default):** pink is <15% of the canvas. A pill, a lead paragraph, a single stat number.
- **Pink-loaded layout (stat page / section opener):** pink is 80–100% of the canvas. The page IS pink, with cream type living on top.
- **Hybrid (split layout):** half the page is pink, half is photo or cream. The L© Online page does this. The Love Out Loud page does it within stat blocks.

There is no 30%, 50%, 70% pink page. Pink either dominates or accents — pick one.

### `lc-pink-soft` — `#F49DC3`

Soft pink. Used for IG story highlight covers (the "Worship" highlight) and secondary tints where the loud pink would overpower. Treat as a lighter cousin, not a default.

## The expanded palette (category / event)

Used **only** for:
- IG story highlight cover backgrounds (one per category — orange, yellow, blue, green)
- Multi-color event graphics (REV Rally — youth-focused, energetic, vibrant)
- Slide system accents that aren't on this skill's surface list (out of scope here)

| Token | Hex | Bucket on IG |
|---|---|---|
| `lc-orange` | `#E27440` | Messages |
| `lc-pink-soft` | `#F49DC3` | Worship |
| `lc-yellow` | `#D9C44A` | Sundays |
| `lc-blue` | `#557EA1` | Photos |
| `lc-green` | `#5E7A56` | Self-Fed |
| `lc-gold` | `#C9A24A` | (Slide accent) |

If you reach for one of these as a default UI color, you've drifted. They're for category coding only.

## Semantic mappings (the layer everything else uses)

When you generate code, components, or specs, use the **semantic** token names. They abstract over the raw values so we can shift palette without breaking every downstream use.

```
lc-bg              → lc-cream         /* default surface */
lc-bg-inverse      → lc-ink           /* dark mode / hero */
lc-bg-emphasis     → lc-pink-loud     /* section opener / stat */
lc-fg              → lc-ink           /* type on cream */
lc-fg-inverse      → lc-cream         /* type on ink or pink-loud */
lc-fg-emphasis     → lc-pink-loud     /* lead paragraph, pull quote, hero stat */
lc-rule            → lc-ink           /* rule lines */
```

## Pair rules (what works together)

These pairings are on-system. Anything else, ask first.

| Background | Foreground type | Use |
|---|---|---|
| `lc-cream` | `lc-ink` | Default editorial body. The 90% case. |
| `lc-cream` | `lc-pink-loud` | Lead paragraphs, pull quotes, stat numbers, section labels. |
| `lc-pink-loud` | `lc-cream` | Section openers, stat pages, year pills. |
| `lc-ink` | `lc-cream` | Hero photo treatments with cream caps overlaid. |
| `lc-taupe` | `lc-cream` | TOC, quieter panels. |
| Photo (B&W halftone) | `lc-cream` | Cover, hero treatments. Use a dark gradient overlay if needed for contrast. |
| Photo (full color, candid) | (no text overlay default) | Editorial spreads — let the photo do the work. |

**Anti-pairings** — don't do these without explicit override:
- `lc-pink-loud` background + `lc-ink` type — too harsh; reads more "warning sticker" than editorial. Use cream type on pink instead.
- `lc-taupe` background + `lc-pink-loud` type — both are warm; pink loses its loudness against taupe.
- Two expanded palette colors as foreground+background — chaos. Pick one expanded color as a fill, use cream type.

## Accessibility notes

Contrast pass/fail at common pairings (against WCAG AA — 4.5:1 normal text, 3:1 large text):

| Pair | Ratio | AA normal | AA large |
|---|---|---|---|
| `lc-ink` on `lc-cream` | ~14.6:1 | ✅ | ✅ |
| `lc-cream` on `lc-pink-loud` | ~3.6:1 | ❌ | ✅ |
| `lc-cream` on `lc-ink` | ~14.6:1 | ✅ | ✅ |
| `lc-pink-loud` on `lc-cream` | ~3.6:1 | ❌ | ✅ |
| `lc-ink` on `lc-taupe` | ~6.0:1 | ✅ | ✅ |

**Implication:** when pink and cream meet (year pill, section opener), keep the type at `lc-fs-title` (28px) or larger. Pink-on-cream lead paragraphs at body size technically fail AA — that's a known editorial trade-off the brand has made. Don't use that pairing for *legal* or *fine-print* type. For body that anyone needs to read carefully, use `lc-ink` on `lc-cream`.

## Where to validate

If you're not sure a color is on-system:
1. Check this file. If it's not here, it's not in the system.
2. Check `assets/tokens.json` (the canonical source).
3. Check the Annual Report PDF in the workspace — every visual treatment in the system shows up there.
4. If still unsure, ask Adam. Don't guess hex codes.

## Open questions / known gaps

- **Brand pink exact value.** `#F0238D` is observed from the Annual and Reading Guide. The Pantone equivalent (likely Pantone 213 C or Rhodamine Red C) hasn't been locked in this file. Add when confirmed.
- **Soft pink token** is observed from the IG Worship story-highlight cover but isn't documented in the Core Style PDF. Treat as provisional.
- **Expanded palette hex codes** are eyeballed from IG covers — confirm against the Sunday Slides Brand Reference when re-uploaded.
