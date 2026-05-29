# 16 — Do and don't

A pinned list of pass/fail moves the system has learned from. Each entry names the failure, the principle behind it, and the corrected move.

## Color

**❌ Don't:** Use `lc-pink-loud` as a default UI color (button on a quiet card, link color in body).
**✅ Do:** Reserve pink for emphasis — section opener, year/CTA pill, lead paragraph, hero stat. Pink is the lever, not the default.
*Why:* When pink is everywhere, it stops meaning anything. The system depends on cream + ink doing 90% of the visual work so the 10% pink lands.

**❌ Don't:** Set `lc-ink` body text on `lc-pink-loud` background.
**✅ Do:** Use `lc-cream` text on `lc-pink-loud`.
*Why:* Pink + black reads harsh — more "warning sticker" than editorial. Pink + cream is the brand's voice.

**❌ Don't:** Reach for the expanded palette (orange, yellow, blue, green) for default UI surfaces.
**✅ Do:** Use those only for category coding (IG story highlight covers) or vibrant event graphics (REV Rally). For everything else, neutral core + pink.
*Why:* The expanded palette is the brand's "loud event" voice. Using it for buttons or backgrounds drifts the system into generic-multicolor.

## Typography

**❌ Don't:** Italicize the entire headline.
**✅ Do:** Italicize one accent word in Apple Garamond. Leave the rest in Neue Haas all-caps.
*Why:* The contrast between heavy sans and delicate italic IS the device. Italicizing the whole line collapses it.

**❌ Don't:** Set display headlines below 900 weight.
**✅ Do:** Use `lc-fw-black` for any heroic display.
*Why:* Lower weights look hesitant. The brand's display voice is heroic.

**❌ Don't:** Use `lc-fw-bold` (700) for inline body emphasis.
**✅ Do:** Use `lc-fw-medium` (500) for the bolded-phrase pattern in body. Reserve 700 for subheads.
*Why:* 700 in body reads as a separate-line subhead. 500 punches without breaking the paragraph.

**❌ Don't:** Forget to specify tracking when speccing display type.
**✅ Do:** Always cite tracking. `-30` / `-20` / `0` / `+60` are the four values in the system.
*Why:* A 56px headline at tracking 0 reads completely different from the same headline at tracking -20. The system specifies it because it matters.

**❌ Don't:** Introduce a third typeface "just for this one piece."
**✅ Do:** Stick with Neue Haas Grotesk Display + Apple Garamond italic. If a project genuinely needs a different feel, it doesn't fit this system — flag it.

## Logo & mark

**❌ Don't:** Recolor the L© mark (purple, gold, etc.).
**✅ Do:** Use only the four approved color lockups: ink/cream, cream/pink, cream/photo, pink/cream.

**❌ Don't:** Use the badge inline with body text.
**✅ Do:** Use the inline glyph "L©" (typed) for inline use; reserve the orbital badge for hero placements and footer signatures.

**❌ Don't:** Recreate the badge from scratch.
**✅ Do:** Use the official asset. The kerning of the orbital text and the position of the arrow are part of the mark's identity.

## Photography

**❌ Don't:** Use stock photography of generic happy people.
**✅ Do:** Use Love Church people in Love Church spaces. Documentary candid is the default mode.

**❌ Don't:** Apply heavy color filters (Lo-Fi, Mayfair, etc.).
**✅ Do:** Keep color natural with a subtle warm cast.

**❌ Don't:** Use drop shadows on type sitting on a photo.
**✅ Do:** Use a gradient overlay on the photo (40% black from bottom) for type contrast, or move the type.

**❌ Don't:** Crop hands out of worship photography.
**✅ Do:** Show the hands. Raised, clasped, lifted — they're emotionally central to the brand's worship aesthetic.

## Layout

**❌ Don't:** Float elements without aligning them to the grid.
**✅ Do:** Every element on a page sits on the same column grid. Stat block + photo on the same line share the column boundary, the top edge, AND the bottom edge.

**❌ Don't:** Fill every corner of a layout.
**✅ Do:** Withhold. Generous whitespace is a brand signal — the editorial discipline.

**❌ Don't:** Bleed display type off the page edge unintentionally.
**✅ Do:** Bleed only when the type IS the focal subject (Annual cover ANNUAL/REPORT). Once per piece, intentionally.

## Components

**❌ Don't:** Use rounded-rectangle buttons (the standard 8px radius "modern button").
**✅ Do:** Use pill-shaped buttons (`lc-radius-pill`) with tracked-caps copy in `lc-fw-bold`.

**❌ Don't:** Place two filled-pink CTAs on the same piece.
**✅ Do:** One dominant pink CTA + secondary outline/text-only CTAs.

**❌ Don't:** Approximate dimensions ("about 1080 wide").
**✅ Do:** Cite exact pixels (1080×1350) tied to a surface token.

## Voice meets visual

**❌ Don't:** Use the italic-accent rule on stat-heavy section openers.
**✅ Do:** Reserve italic-accent for emotional headlines. Stat openers stay all-caps Neue Haas because the data IS the emotion.

**❌ Don't:** Pink-color the italic accent word.
**✅ Do:** Let the italic accent inherit the surrounding line color. The italic does the work; pink would over-emphasize.

## Process

**❌ Don't:** Quote a hex code without naming the token.
**✅ Do:** "Use `lc-pink-loud` (#F0238D) — the loud accent, reserved for emphasis."

**❌ Don't:** Skip the pre-flight check before sending a spec.
**✅ Do:** Run the checklist in `SKILL.md` § Pre-flight checks. Every time.

## When you're not sure

The "Annual Report test" — would this fit between two pages of the Annual Report? If yes, ship it. If no, you've drifted. Pull back to the system and try again.
