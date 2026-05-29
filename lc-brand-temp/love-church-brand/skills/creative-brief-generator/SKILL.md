---
name: creative-brief-generator
description: Generate a Love Church creative brief in the Tier 1/2/3 format used in the Notion Creative Briefs hub. Triggers when the user asks for "a creative brief," "brief for [event/series/sermon]," "tier 1 brief," "tier 2 brief," "tier 3 brief," "make a brief," or "creative brief template." Produces a ready-to-publish brief with all 8 LC components (objective, audience, message, deliverables, look/feel, mandatories, timeline, owner). Drop it in Notion, share it with the V/I Team, hand off to the designers.
---

# Love Church Creative Brief Generator

Creative briefs are the unlock for the V/I Team. A great brief makes the design fast and the revisions rare. A bad brief makes everyone redo the work twice.

## When to trigger

- "Make a brief for [event/series/Sunday]."
- "Tier 2 brief for Mother's Day."
- "Creative brief for the next sermon series."
- "Draft a brief I can drop into Notion."

## Tier system

Love Church briefs run on a 3-tier system based on scope and effort:

- **Tier 1** — Single-piece briefs. One IG post, one slide, one event card. Light brief, 1 page.
- **Tier 2** — Campaign briefs. A multi-piece event push (e.g., Mother's Day weekend) with several deliverables across channels. Medium brief, 1–2 pages.
- **Tier 3** — Series-level briefs. A sermon series, a vision moment, a season (e.g., Easter, Christmas, a transition). Full brief, 2–3 pages with concept exploration.

If the user doesn't specify the tier, infer from scope and confirm before producing.

## What you need

Before generating, confirm:

1. **Title and tier.** "Mother's Day 2026 — Tier 2."
2. **Date(s) it serves.** Sunday it lands or campaign window.
3. **Owner.** Who's responsible for shipping the deliverables. Default: Adam or Rachel Hawley.
4. **Stakeholder.** Who's the primary voice/audience contact (e.g., the preaching pastor for series, Tera Reelfs for outreach, Casey Reale for next steps).
5. **Source material.** Sermon outline, event description, prior brief to follow, or "build from scratch."

If the user has a Notion event row to link to, capture the URL — the brief should backlink to it.

## Output structure — the LC 8-component brief

Every brief, regardless of tier, hits all 8 components. Tier just controls depth.

### 1. Objective
What does this need to do? In one sentence.

- *Tier 1 example:* "Drive RSVPs for the May 17 Marriage Date Night."
- *Tier 3 example:* "Cast vision for the 5S Life across a 6-week sermon series and convert 200 new self-feeders to the daily reading plan."

### 2. Audience
Who is this for? Be specific. Not "the church" — who within the church or city.

- "First-time guests with a school-age kid."
- "Long-time members in the 5S Surrendered tier looking for a Surrounded next step."
- "Omaha women 25–45 not currently attending church."

### 3. Message
The single takeaway in one sentence. If the audience remembers nothing else, what's the line?

- "There's a seat for you Sunday."
- "Real People, Real Life — and we mean it."
- "The 5S Life isn't a checklist. It's a way of walking with Jesus."

### 4. Deliverables
A complete list of every piece of creative needed. For each, name the format, dimensions, and channel.

| # | Deliverable | Format | Channel | Owner |
|---|---|---|---|---|
| 1 | IG carousel | 1080×1350, 5 slides | @lovechurchomaha | Creative |
| 2 | Sunday lobby slide | 1920×1080 | LED wall | Production |
| 3 | Email hero | 1200×600 | All-church email | Comms |
| 4 | GMB post | Headline + body + image | Google Business | Jordan |
| 5 | Web banner | 1920×600 | lovechurch.org/events | Web |

### 5. Look & Feel
The visual brief. Reference the LC brand palette (near-black, cream, taupe, off-white) and type system (Neue Haas Display + Apple Garamond italic accent). Note any series-specific palette, photography style, or motion direction. Drop reference links if useful.

For Tier 3 briefs, include 2–3 mood-board references and a sentence of concept rationale.

### 6. Mandatories
Things the work must include or avoid:

- LC logo / "L" badge mark
- "Plan Your Visit" + "Watch Online" CTA pair (for guest-facing pieces)
- Service times: 9A + 11A
- Address line for printed pieces
- Any sermon scripture (cited NKJV by default)
- Translation of insider terms on first use

And the don'ts:
- No stock photos
- No trendy display fonts
- No emoji-stuffed copy
- No "service" — use "Encounter"
- No "Pastor [First Name]" for women in formal leadership

### 7. Timeline
Backwards-planned from the launch date. Include drafts, reviews, final, and ship.

```
Mon DD — Brief approved (today)
Wed DD — Round 1 drafts due
Fri DD — Round 1 review with [stakeholder]
Mon DD — Round 2 final
Wed DD — All assets handed off to channels
Sun DD — Live
```

### 8. Owner & Stakeholder
Name names. Brief is owned by [X]. Stakeholder approval comes from [Y]. Designer/copywriter is [Z]. Use Notion mentions if the brief is going to Notion.

## Tier-specific additions

### Tier 1 (single-piece)
Stop after the 8 components. Don't add concept exploration — it's a single piece.

### Tier 2 (campaign)
After the 8 components, add a **Campaign Beats** section listing the rollout sequence (announcement → deeper push → final reminder → recap).

### Tier 3 (series)
After the 8 components, add:
- **Concept rationale:** 2–3 paragraphs on the *why* behind the visual direction.
- **Series titles + episode breakdown:** Each Sunday's title and one-line takeaway.
- **Through-line:** What ties every piece together (a verse, a phrase, a visual motif).

## Voice rules

This skill runs alongside `brand-voice-enforcement` and `love-church-context`. The brief itself should be in clean, direct prose — not church-marketing-speak. Write briefs like you'd write a memo: short sentences, no hedging, every line earns its place.

## Common failure modes

- **Vague objective.** "Promote Mother's Day." Fix: name the conversion ("Drive 50 first-time-guest visits").
- **Audience = 'everyone'.** Off-brand. Fix: pick a single primary audience.
- **No deliverables list.** Designer can't ship without it. Fix: enumerate every asset.
- **Copy/voice missing.** Brief should include the working headline + body lines for designers. Fix: write them in.
- **No timeline.** Brief becomes wishful. Fix: backwards-plan.
- **Missing owner.** Briefs without owners die. Fix: name names.

## Delivery

Hand off as a clean markdown file ready to paste into Notion. File name convention:

```
BRIEF — [Project Name] [Date].md
```

If the user has a Notion link to the matching event row, include it at the top of the brief and add a TODO to backlink the brief from the event.

If they want a Notion-ready output (with toggle blocks, callouts, etc.), produce two outputs: the markdown version and a Notion-block version using the Notion MCP — but only if the team has Notion connected.
