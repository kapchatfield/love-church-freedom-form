# 08 — Iconography

The Love Church system uses **type and rules** as its primary information graphics. Icons are rare. When an icon does appear — a play button on a video card, a chevron on a CTA, a hamburger on the mobile nav — it should be invisible: monoline, square-cap, sized to match the type next to it.

## When to reach for an icon (and when not to)

**Use an icon when:**
- The surface is a UI element (web, app, email) and an icon is functionally expected (play, share, menu, search).
- The icon replaces a longer label that would clutter (e.g., a small chevron after "Read more" instead of an em-dash).
- The deliverable is a wayfinding piece (a map legend, a service guide) where icons aid scanning.

**Don't use an icon when:**
- Type would do the job. The brand is editorial — words are usually stronger than little pictures.
- The icon would be decorative (a sparkle next to a headline, a heart next to "Love"). Decoration weakens hierarchy.
- The surface is editorial print or social — those don't need icons; the layout itself is the wayfinding.

## Style spec

When icons are required:

- **Monoline.** Single weight, no fills, no two-tone. The Phosphor "Regular" set, Heroicons "Outline," or Lucide all match this style.
- **Stroke weight: 1.5–2px** at 24px reference size. Scales linearly.
- **Square caps.** Not rounded.
- **No decoration.** No drop shadows, no inner glows, no gradients.
- **Color**: matches the type next to it — `lc-ink`, `lc-cream`, or `lc-pink-loud`. No multi-color icons.

## Sizing

Icons should match the **cap height** of the type next to them, not the line height. The eye reads the icon and the word as a single unit.

| Beside text | Icon size |
|---|---|
| `lc-fs-caption` (14px) | 14px |
| `lc-fs-body` (18px) | 16–18px |
| `lc-fs-title` (28px) | 24px |
| Standalone (CTA button) | 20–24px |
| App tab bar | 24px |

## Common icons in the system

| Use | Icon | Notes |
|---|---|---|
| Play (video card) | Triangle in circle | Outline only. |
| Share | Standard share glyph | Phosphor "share-network" or equivalent. |
| Menu (mobile) | Hamburger | Three lines, square caps. |
| Close | X | Square caps. |
| Right arrow / chevron | Chevron-right | Used after CTAs ("Plan Your Visit ›"). |
| Search | Magnifying glass | Outline only. |
| Location | Pin | Outline only. |
| Calendar | Standard calendar | Outline only. |

## Don't

- Don't fill icons. The system is monoline.
- Don't use emoji as design icons (emoji is fine in copy, not in design — they read as a different visual register).
- Don't introduce a custom illustrated icon set. If a moment needs more than monoline outlines, it needs a different visual answer (a photo, a typographic treatment), not a custom icon.

## What's reserved for a future iteration

- Custom event icons (REV Rally, Christmas Encounters) — currently solved with type + color, not iconography.
- Sermon series-specific glyphs — handled inside the series art skill, out of this skill's scope.

This is the lightest section in the system on purpose. The brand uses fewer icons than most, and that's a feature.
