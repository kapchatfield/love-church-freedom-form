# 13 — Components: App (Subsplash)

Specs for the Love Church app on Subsplash. The app is the most controlled surface in the system — Subsplash provides the chrome, Love Church provides the content tiles. Spec scope is therefore narrower: feature cards, content thumbnails, and any custom-themed regions.

App live at: subsplash.com/lovechurch/app

## Feature card (home hero)

**Dimensions:** 1242×500 (Subsplash spec)
**Use:** The top hero on the app home — usually the current series or the next big event.

**Layout:**
- Full-bleed photo OR pink fill
- Headline left-anchored, 80px L margin
- Subhead and CTA-style label below

**Type:**
- Headline: `lc-fs-headline-1` (56px) `lc-fw-black`, italic-accent rule applies
- Subhead: `lc-fs-caption` (14px) `lc-fw-bold` `lc-tracking-caption` in `lc-pink-loud`
- Color: cream on photo / pink, ink on cream

**Variants:**

**a) Series feature** — sermon series art (B&W halftone or photo with gradient), title in `lc-cream`, week number label in pink.

**b) Event feature** — `lc-pink-loud` fill, event name in cream, date and CTA copy below.

**c) Watch live** — full-bleed photo with red dot indicator, "WATCH LIVE NOW" label, time stamp.

## Content thumbnail (square card)

**Dimensions:** 1080×1080 (1:1)
**Use:** Sermon thumbnails, podcast episodes, devotionals — the secondary content tiles.

**Layout:**
- 4:3 photo top (1080×810)
- Caption block bottom (1080×270)

**Type:**
- Title at `lc-fs-title` (28px) `lc-fw-bold` in `lc-ink` (on cream caption block)
- Series/category label at `lc-fs-caption` `lc-fw-bold` `lc-tracking-caption` in `lc-pink-loud`
- Date/duration at `lc-fs-micro` in `lc-taupe`

## Reading plan tile

The Bible-in-2-Years reading plan is a recurring app surface.

**Dimensions:** 1080×600 (16:9 banner)
**Layout:**
- Background: `lc-cream`
- Left third: Day number (e.g., "DAY 142") in `lc-fs-display-2` `lc-fw-black` `lc-pink-loud`
- Right two-thirds: Today's reading reference at `lc-fs-headline-2` in `lc-ink`
- Optional verse pull-quote in `lc-font-accent` italic at `lc-fs-lead`

## Notification icon

**Dimensions:** 256×256 (Subsplash app notification icon)
**Treatment:** L© badge centered on `lc-pink-loud` rounded-square (16px corner radius), white outer mask for iOS.

## What's in Subsplash's lane

Many app surfaces are templated by Subsplash itself — list views, player screens, profile screens. The Love Church team doesn't custom-design those. They inherit:
- Subsplash typography defaults
- Subsplash navigation chrome
- Subsplash tab bar

The only custom surfaces under our control are the **feature card**, **content thumbnails**, and **theme accent color** (which Subsplash exposes as a single value).

## Subsplash theme accent

Set the app's accent color to `lc-pink-loud` (`#F0238D`). This drives:
- Active tab indicators
- Link colors
- Like/save state

## Pre-flight check

When generating an app deliverable:

- Is this surface actually under our design control, or is it Subsplash chrome? Don't waste cycles speccing what we can't customize.
- Are dimensions exactly per Subsplash's spec sheet?
- Is the photo aspect right for the surface (1080×500 banner vs 1080×1080 square)?
