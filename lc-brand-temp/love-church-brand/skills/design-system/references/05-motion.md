# 05 — Motion

Most of the Love Church visual system is static. When motion appears — an IG reel cover, a website hero animation, a sermon teaser — it should feel like the static system in time, not like a different brand suddenly turning on.

## Principles

1. **Type does the moving.** Photos hold; type slides in or scales up. The brand's voice is typographic, so the motion language extends from typography.
2. **Restraint over flourish.** No bouncing, no spinning, no parallax for parallax's sake. A clean cut, a slow fade, a quick reveal — that's the vocabulary.
3. **The pink hits late.** When pink enters a motion piece, it's the punchline — the year pill landing into place, the CTA appearing. Letting it sit on screen for two beats makes it land harder than animating it forever.
4. **Sound is treated separately.** This skill doesn't spec audio. But the motion language assumes the music has already done emotional work — the visual stays gridded and disciplined.

## Duration tokens

| Token | Value | Use |
|---|---|---|
| `lc-dur-fast` | 150ms | Hover, tap, micro-state changes. |
| `lc-dur-base` | 240ms | Default UI transitions — page navs, button presses, accordion. |
| `lc-dur-slow` | 400ms | Bigger reveals — modals, hero copy entrance. |
| `lc-dur-ambient` | 800ms | Slow drifts on hero motion graphics — text crawls, background pans. |

Anything over 800ms is asking the audience to wait. Use sparingly and only on hero pieces where they've chosen to dwell.

## Easing tokens

| Token | Value | Use |
|---|---|---|
| `lc-ease-standard` | `cubic-bezier(0.2, 0, 0, 1)` | Default for all UI motion. |
| `lc-ease-emphasis` | `cubic-bezier(0.3, 0, 0, 1)` | Punchier — for the pink hits, the stat-number reveal. |
| `lc-ease-linear` | `cubic-bezier(0, 0, 1, 1)` | Continuous loops — text crawls, looping background. |

No bouncy / overshoot eases. The brand isn't playful in that way.

## Motion vocabulary

A short list of moves the system endorses. Anything outside this list, ask first.

- **Cut** — the default. Hard transition between two static states. Use for sermon teaser cuts, social reels.
- **Fade** — `lc-dur-base` opacity transition. Use between photos in a hero cycle.
- **Slide-and-snap** — type slides in `lc-dur-slow` with `lc-ease-emphasis`, lands on grid, holds. Use for headline reveals.
- **Scale-and-hold** — display headline starts at 110% scale and settles to 100% over `lc-dur-slow`. Use sparingly, for hero moments.
- **Crawl** — `lc-dur-ambient` linear horizontal pan of a band of type or a photo. Use for ambient backgrounds.
- **Pop** — a small accent element (year pill, CTA pill) appears with a quick scale `lc-dur-fast` and `lc-ease-emphasis`. Use for the pink punchline.

## Sermon teaser pattern

When motion is generated for a sermon teaser:

1. **Hero shot, 1–2 seconds** — full-color or B&W documentary photo of the moment. Held still.
2. **Title card** — cream paper, headline in display caps slides in from below (slide-and-snap), italic-accent word lands a beat after the rest with a soft fade.
3. **Pink punctuation** — series number pill or year pill pops into the corner.
4. **CTA card, 1.5 seconds** — short directive ("WATCH ONLINE 5P SUNDAY"), centered, holds.
5. **Cut to logo card** — L© badge centered on cream, holds.

Total duration: ~6–8 seconds. Anything longer needs justification.

## What's out of scope (for now)

- Pacing for full sermon recap reels — defer to the V/I Team's after-effects templates.
- Lyric and worship motion — tracked separately; out of this skill.
- Lower thirds / broadcast graphics — a future addition; not yet in the system.

If a request comes in for any of these, deliver what you can with the duration/easing/vocabulary tokens above and flag the gap to Adam.
