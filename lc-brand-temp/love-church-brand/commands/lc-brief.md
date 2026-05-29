---
description: Generate a Love Church creative brief in the Tier 1/2/3 format.
---

The user is asking for a creative brief. Invoke:

1. `love-church-context` for org facts and current naming.
2. `brand-voice-enforcement` for any working copy lines that go in the brief.
3. `creative-brief-generator` for the 8-component structure and tier system.

Confirm:

- Title and tier (1, 2, or 3) — infer if scope is obvious, but confirm.
- Date(s) it serves.
- Owner (default: Adam Deidel or Rachel Hawley).
- Stakeholder (preaching pastor for series, Tera Reelfs for outreach, etc.).
- Source material (sermon outline, prior brief, build from scratch).
- Any Notion event row to backlink.

Deliver the brief as ready-to-paste markdown with the LC 8-component structure:
1. Objective
2. Audience
3. Message
4. Deliverables (table)
5. Look & Feel
6. Mandatories
7. Timeline (backwards-planned)
8. Owner & Stakeholder

Add tier-specific sections:
- Tier 1: stop after the 8.
- Tier 2: add Campaign Beats.
- Tier 3: add Concept Rationale + Series Titles + Through-line.

If Notion is connected and the user wants the brief published there, after producing the markdown also create a Notion page in the Creative Briefs hub via the Notion MCP and backlink the matching event row in DB · Events.

File name convention for the markdown delivery: `BRIEF — [Project Name] [Date].md`
