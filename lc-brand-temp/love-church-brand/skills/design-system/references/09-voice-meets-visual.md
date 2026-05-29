# 09 — Voice meets visual

This is where the design system intersects the brand-voice system. Type doesn't just *display* the words — it *interprets* them. The same headline set two different ways means two different things. This file documents the interpretation rules so visual choices reinforce voice, not fight it.

For the underlying voice doctrine, see `skills/brand-voice-enforcement/SKILL.md`. This file is about typography and layout in service of voice.

## The italic-accent rule (most important)

Headlines on the public-facing surfaces of Love Church follow a recurring pattern: **all-caps Neue Haas display + one italicized accent word in Apple Garamond.** The italic word is the line's emotional payload — the place where the brand stops shouting and breathes.

This is the brand's *most distinctive typographic device*. It runs on the website, in the Annual, in the welcome video. Get this right and the brand is recognizable in two seconds.

### How to pick the accent word

The accent word is **the promise**, **the invitation**, or **the emotional payload** of the line. Walk through these tests in order:

1. **Which word do you want the reader to feel?** Italicize that.
2. **Which word does the line pivot on?** ("Real People, *Real Life.*" — pivots on "Real Life" being the resonance.)
3. **Which word, if removed, would make the line lose its meaning?** Italicize that.

Examples from the live site (already validated):

| Headline | Accent | Why |
|---|---|---|
| There's More *To Life* | "To Life" | The promise. |
| Real People, *Real Life* | "Real Life" | The pivot. |
| The gameplan is *simple.* | "simple." | The relief. |
| Ready to *Experience More?* | "Experience More?" | The invitation. |
| Ever feel like *there should be more?* | "there should be more?" | The unspoken longing. |

### Treatment

- Italic word in `lc-font-accent` (Apple Garamond, italic, regular weight)
- Inherits the size of the surrounding headline — don't shrink it
- Inline, no break unless the layout demands it
- Color matches the surrounding line (don't pink the italic; let the italic do the work)
- Tracking: 0 (don't tighten the italic — the serif breathes)

### When NOT to use it

- Stat-page section openers (ENCOUNTERS, LOVE OUT LOUD) — the data is the emotion; no italic needed
- Microcopy and labels — too small to register
- Headlines under ~24px — the contrast collapses
- Serial headlines where every line uses an italic — overuse weakens the device

## CTA microcopy + button pairings

CTAs in the LC system are pill-shaped, short, directive. The button shape is from `lc-radius-pill`. The copy comes from the brand-voice system.

### Approved CTA copy

These are the brand's go-to calls. Use them verbatim where they fit.

| Copy | Use | Button color |
|---|---|---|
| Plan Your Visit | First-time guest CTA. The dominant surface CTA. | `lc-pink-loud` fill + `lc-cream` text |
| Watch Online | Online encounter CTA. | `lc-pink-loud` fill + `lc-cream` text |
| Get In The Game | Serve-team / volunteer CTA. | `lc-pink-loud` fill + `lc-cream` text |
| Experience More | Generic next-step CTA. | `lc-pink-loud` fill + `lc-cream` text |
| Connect with Us | Contact CTA. | `lc-cream` border + `lc-ink` text (secondary) |
| Find a Group | Groups CTA. | `lc-pink-loud` fill + `lc-cream` text |
| Give | Giving CTA. | `lc-pink-loud` fill + `lc-cream` text |

**Rule:** the dominant CTA on a piece is filled pink. Secondary CTAs are outline / text-only. Never two filled-pink CTAs in the same piece — pink is the lever, not the default.

### CTA button spec

```
Background: lc-pink-loud
Text:       lc-cream
Type:       lc-font-display, lc-fw-bold
Size:       lc-fs-caption (14px) for inline UI; lc-fs-body (18px) for hero CTA
Tracking:   lc-tracking-caption (+0.060em)
Case:       UPPERCASE
Padding:    lc-space-md (16px) vertical / lc-space-xl (32px) horizontal
Radius:     lc-radius-pill
```

The pill shape and the tight tracked caps are the LC button signature. Standard rounded-rectangle buttons fall out of system.

## The "Bold inline phrase" body pattern

In long-form body, certain phrases get inline weight (`lc-fw-medium`) for emphasis. This creates a "skim path" — a reader scanning the bolded fragments alone gets the narrative arc.

How to choose what to bold:

- The **emotional beats** ("knowing about Jesus—but not truly knowing Him")
- The **named feelings or experiences** ("anxiety, sadness, and fear")
- The **turning points** ("She began praying and asking God to lead her")
- The **resonant phrases** ("a freedom she once believed she'd never experience")

Don't bold:
- Generic verbs and connectors
- Dates, names, places (unless they're the turning point)
- More than ~4 phrases per paragraph (the skim path should breathe)

Use weight 500 (`lc-fw-medium`), never 700 (`lc-fw-bold`). Bold is for subheads.

## Pink lead paragraph

Editorial story pages in the Annual use a `lc-pink-loud` lead paragraph at `lc-fs-lead` (22px) before transitioning into `lc-ink` body. The pink lead does three things at once:

1. Visual anchor — the eye lands on it first
2. Emotional cue — pink signals "the moment that mattered"
3. Reading rhythm — the color shift between lead and body breaks up the column

Use this pattern when:
- An editorial story page needs a lead
- A web feature has a narrative structure
- An email has a single most-important paragraph

Don't use when:
- The whole piece is short (under ~150 words). The pink lead works because it contrasts with body that follows.
- Multiple paragraphs deserve emphasis equally — pink lead is for THE paragraph that matters most.

## "L©" inline glyph (cross-reference)

The L© inline glyph (substituting for the letter "L" in "L© Online," "L© Stories") is a voice-meets-visual pattern as much as a logo pattern. Whenever a sub-brand name starts with L and is part of the LC family, the inline glyph reinforces parent-brand DNA without adding a separate mark.

See `references/06-logo-and-mark.md` for the full mark spec.

## Voice/visual mismatches to watch for

| Voice direction | Visual answer |
|---|---|
| Warm, invitational | Documentary photo + cream surface + italic-accent headline |
| Bold, ALL IN | Heroic display caps in `lc-fw-black`, tight tracking, on `lc-pink-loud` or `lc-ink` |
| Celebratory | Color photo + pink lead paragraph + stat-style numbers |
| Mission-obsessed | Numbers heroic, type spare, layout gridded |
| Pastoral, reflective | B&W halftone photo + Apple Garamond italic in pull quotes |
| Quick directive (CTA) | Pink pill button + tracked-out caps copy |

When you receive copy from the voice system or a draft, ask: which of these directions is it? Then pick the visual answer.

## The "two seconds" test

A piece is on-system if: a member of the team can identify it as Love Church in two seconds, even with no logo visible. The italic-accent headline, the pink + cream, the Neue Haas Black, the documentary photo — those are the markers. If none of them are present, the piece may not be on-system.

Run that test on every deliverable.
