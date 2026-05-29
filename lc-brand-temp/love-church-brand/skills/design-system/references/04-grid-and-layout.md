# 04 — Grid & layout

Love Church layouts are gridded, hierarchical, and unafraid of large blocks. The system uses generous margin, strict alignment, and rules (literal horizontal lines) instead of boxes. When in doubt, lean editorial: more breathing room, fewer dividers, stronger hierarchy.

## The grids

### Print / page (Annual Report, Reading Guide)

- **Letter portrait, 8.5×11"** — the Annual canvas.
- **Margin:** 0.5" outer, 0.6" top, 0.6" bottom. Page numbers sit in the bottom-outer corner with the L© badge.
- **Columns:** 2-column for body story pages (MEET ALYSSA pattern). 3-column or 6-column for stat pages and TOC.
- **Baseline grid:** 14pt baseline. Body sets at 11/14 (size/leading). Display sits on the same baseline grid, snapped.
- **Vertical rhythm:** stat blocks separated by `lc-rule-regular` rules with one baseline of clearance above and below.

### Reading Guide (landscape)

- **Letter landscape, 11×8.5"** — the Reading Guide canvas.
- **6-column data grid** for the months, with a **3-column title block** on the right.
- The right title block is fixed — display headline + L badge + accent button stack.
- Footer rule full-width at base of page with three-column footer (org url / year / city).

### Web (lovechurch.org)

- **12-column max-width 1280px container** with 24px gutters.
- **Hero:** full-bleed at desktop, snapping to 12-col container for content.
- **Section padding:** `lc-space-4xl` (96px) top and bottom on desktop, `lc-space-2xl` (48px) on mobile.
- Body content sits at max-width 720–800px for long-form readability.

### Email (MailChimp)

- **Single-column 600px wide on mobile.** Multi-column blocks stack on mobile by default.
- **Padding:** `lc-space-lg` (24px) inside content blocks; `lc-space-xl` (32px) between blocks.
- **Hero image:** full-bleed within the column. No outer padding above the hero.

### Social (IG / FB / GMB / YT)

Each surface has its own grid baked into its dimension token (see `01-tokens.md` and `10-components-social.md`). Common rules:

- **IG safe area:** keep all critical content within the central 80% of the canvas. Top 250px and bottom 250px of an IG story are the platform's UI overlap zone — use them for atmosphere, not for the headline.
- **YT thumbnail safe area:** keep the headline in the left 65% of the frame; the right side often gets covered by the duration timestamp on hover.
- **Carousel slide consistency:** every carousel slide uses the same grid — title position, footer position, page indicator. The carousel reads as a designed object only when the underlying grid is honored.

## Page numbers and footers

The Annual page footer is a system worth copying for any multi-page deliverable:

```
[LOVECHURCH.ORG]    [2026]    [LOVE CHURCH OMAHA]    [page X/Y]    [L© badge]
```

- All caps, `lc-fs-micro`, `lc-fw-bold`, `lc-tracking-caption`.
- A `lc-rule-hairline` runs above the footer text, full bleed.
- The L© badge anchors the outer corner — same orbital mark as the brand mark, scaled to ~28px.

## Section openers

A section opener is its own page in print; it's its own block on web. The pattern:

1. **Loud color fill** — `lc-pink-loud` background, full bleed.
2. **Heroic display headline** — `lc-fs-display-1` or `display-2`, `lc-fw-black`, `lc-fg-inverse` (cream-on-pink). All caps. Tight tracking.
3. **Sub-section labels and stats** stack below in cream, separated by hairline rules.

The opener earns its loudness by being **brief**. A one-word section title (ENCOUNTERS) plus the data. No body copy on a section opener — that goes on the following page.

## Modular spreads

A "modular spread" is a single page that mixes multiple block types — stat blocks, photos, headlines. The Love Out Loud page is the canonical example.

The rule: every block on a modular spread sits on the same grid. If you have a stat block (left) and a photo (right), they share the column boundary, the top edge, AND the bottom edge. No floating, no random padding.

When you generate a modular spread:
- Pick the grid (3-col or 6-col).
- Place each block as a multiple of grid cells (1×1, 2×1, 1×2, etc.).
- Use rules between blocks of the same type; use color fields between blocks of different types.

## Whitespace

The system defaults to generous whitespace. The editorial discipline is *withholding* — the urge to fill empty space is the urge to weaken hierarchy.

Heuristics:
- Section openers should have at minimum `lc-space-3xl` (64px) of clearance between the headline and the first sub-element.
- Body columns should never come within `lc-space-lg` (24px) of an image edge.
- Page margins are never violated by display type. The headline can be huge; it cannot bleed off the edge unless the layout is explicitly full-bleed.

## When the grid breaks (and how)

Some pieces intentionally break the grid for emphasis. The Annual cover headline (ANNUAL/REPORT) is so large that the letterforms touch the edges of the page. That's the breaking point — when type is the photograph.

Rules for grid-breaking:
- It's **always type**, not a photo or a graphic.
- It's **always at the largest scale** in the document.
- It's **always intentional and rare** — once per piece, not throughout.
