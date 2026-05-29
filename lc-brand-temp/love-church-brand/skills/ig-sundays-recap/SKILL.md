---
name: ig-sundays-recap
description: Generate the weekly "Sundays at Love" Instagram recap — caption, carousel slide copy, photo direction, and CTA. This is the highest-engagement IG bucket for @lovechurchomaha (~189 avg likes per IG content audit). Triggers when the user asks for a "Sunday recap," "this week's IG post," "Sundays at Love," "weekly recap," "post for Monday," or any IG carousel/feed content reflecting on the prior Sunday. Output is ready to hand to the social team for posting.
---

# Sundays at Love — Instagram Recap

The weekly Sunday recap is Love Church's highest-engagement Instagram bucket. Treat it like a hero piece, not a leftover.

## When to trigger

- "Make me a Sunday recap post."
- "IG carousel from this Sunday."
- "Caption for Monday's recap."
- "Post for the weekly recap."
- "Sundays at Love post."

If the user says "social post" without context, ask whether it's the Sunday recap or a different bucket (announcements, sermon teaser, testimony, ministry highlight) — different buckets, different formulas.

## What you need from the user

Before generating, confirm:

1. **What Sunday is this for?** Date.
2. **What was preached?** Title, series, one-line takeaway. Speaker if not Pastor Mike or Pastor Todd.
3. **Photos available?** Real photos from Sunday — not stock. If photos aren't picked yet, you can produce direction (what to look for, what NOT to use).
4. **Special moments?** Baptisms, salvations, first-time guest, kids dedication, milestone — anything to celebrate beyond the regular flow.
5. **Format preference?** Single feed photo + caption, or 5–8 slide carousel.

If the user provides a sermon or service recording, run the analysis to extract the takeaway yourself and confirm it.

## Output structure

### 1. Caption

8–12 lines. Structure:

- **Line 1:** Identity line or a celebration line. Examples:
  - "Sundays at Love."
  - "This is what we mean by Real People, Real Life."
  - "Worship. Word. Witness. Sunday at Love Church."
- **Lines 2–6:** The body — 2–3 short sentences naming what God did, what was preached, who showed up. Plain language. No hype.
- **Line 7–8:** Italic-accent line if the medium supports italics (use *asterisk italics* — Instagram preserves them on web, social schedulers may flatten):
  - *"Real People. Real Life."*
- **Closing:** One CTA. Default: *"Plan your visit → link in bio."* For testimony-heavy weeks: *"Watch the message → link in bio."*
- **Hashtags:** 1–2 max. `#lovechurchomaha` plus one contextual tag if it actually fits (`#omaha`, `#easter`, `#baptisms`). Skip generic religious hashtag stacks.

### 2. Carousel slides (if applicable)

5–8 slides. Lead with people, end with invitation.

- **Slide 1 (cover):** Strong photo of the room or a person. Headline overlay: short, italic-accent pattern. *"Sundays at Love"* or *"This Sunday."*
- **Slides 2–4:** Photos with one-line captions in Neue Haas Display. Specific moments — worship, kids, baptisms, the preaching.
- **Slide 5 (mid-point):** A pull quote from the sermon in serif italic (Apple Garamond). Cite scripture if the line was a verse. Default NKJV; allow NIV/NLT if readability matters.
- **Slides 6–7:** More photos with captions. Family, friends, the people behind the room.
- **Final slide:** *"There's a seat for you."* + Plan Your Visit + service times + handle. Keep it spare.

### 3. Photo direction (if photos aren't picked)

Tell the social team what to look for:

- **Yes:** Wide room shots with hands raised. Close-ups of real congregants — not just leadership. Kids dedications, baptisms, hugs after service. The lobby. Coffee. Conversation.
- **No:** Posed shots with the same five people. Empty stage shots. Behind-the-scenes-of-the-band only. Stock or AI-generated photos. Anything overly polished.

### 4. CTA stack

Always include the dual pair if the post is guest-facing:

- **Plan Your Visit:** lovechurch.org or "link in bio."
- **Watch Online:** youtube.com/lovechurchomaha.

## Voice rules

This skill should be invoked alongside `brand-voice-enforcement`. The voice attributes apply: faith-forward, bold & all-in, warm & invitational, celebratory, mission-obsessed, authentic & relational, consistently excellent.

Specific to the Sunday recap:

- Lead with the person, not the brand.
- Celebrate what God did. Don't perform what we did.
- One CTA per caption. More than one is noise.
- No hype words ("don't miss," "you have to see this," "🔥🔥").
- "Service" is forbidden — use "Encounter" or just "Sunday."

## Common failure modes

- **Stock photos.** Off-brand. Fix: use real photos from this Sunday. If none exist, hold the post until they do.
- **Five hashtags.** Off-brand. Fix: 1–2 specific tags max.
- **Announcement-y caption.** "We're so excited to share…" Fix: open with what God did or what someone experienced.
- **Sermon outline as caption.** That's a blog. Fix: pick one line and let the rest live in the YouTube/blog assets.
- **Carousel that ends without a CTA.** Final slide must invite next step.

## Delivery

Hand off as:

1. Caption (copy-pasteable).
2. Carousel slide copy (numbered, with slide-by-slide direction for the designer).
3. Photo direction (if applicable).
4. Hashtags (already inside caption — don't list separately).

Drop in `/sessions/<session>/mnt/<workspace>/` as a single .md or paste inline if the user prefers chat delivery.
