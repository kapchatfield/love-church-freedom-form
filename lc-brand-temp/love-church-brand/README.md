# Love Church Brand Plugin

Everything the Love Church staff needs to write, design, and ship on-brand content — bundled into one Cowork plugin.

## What's inside

**10 skills:**

1. **brand-voice-enforcement** — Auto-applies the LC voice (faith-forward, all-in, warm-and-invitational) to any content the team writes. Reads the embedded 22-page brand-voice-guidelines.md before producing copy.
2. **love-church-context** — Always-on church context. Loads the mission, 5S Life, leadership team, ministry names, vocabulary, and contact info so every piece of work is grounded.
3. **sermon-content-kit** — One sermon → YouTube + Instagram + X + LinkedIn + blog + email + podcast + group discussion. Bundled from Adam's existing skill.
4. **ig-sundays-recap** — Generates the highest-engagement Instagram bucket (Sundays-at-Love recaps) — caption + carousel + photo direction.
5. **gmb-weekly-post** — Weekly Google My Business post: headline + body + CTA + image direction. Built for Jordan Johnson's GMB cadence.
6. **weekly-email-newsletter** — All-church weekly email in the Celebrate · Connect · Invite rhythm.
7. **creative-brief-generator** — Matches the LC creative-brief template + tier system (Tier 1/2/3) used in the Notion Creative Briefs hub.
8. **creative-director** — Vignelli-discipline review of any creative work (slides, social, motion, key art). Bundled.
9. **worship-leader-eval** — Worship-leader video evaluation in the Bob Kauflin (Worship Matters) framework. Bundled.
10. **kids-rev-comms** — Family-facing copy for Love Kidz (birth–5th) and REV (6th–12th).

**5 slash commands** (one-shot shortcuts):

- `/lc-post` — IG/social post from a topic.
- `/lc-email` — Weekly email newsletter.
- `/lc-brief` — Creative brief.
- `/lc-recap` — Sunday recap kit.
- `/lc-review` — Run an on-brand check on a draft.

## Installation

1. Drag the `love-church-brand.plugin` file into Cowork.
2. Press Accept.
3. Make sure your account is connected to the church's shared tools (Notion, Monday.com, Slack, Gmail, Google Calendar, Google Drive).

That's it.

## How to use

The skills auto-trigger when you ask for the relevant work — you don't need to invoke them explicitly. Examples:

- "Write a weekly email about Mother's Day." → triggers `weekly-email-newsletter` + `brand-voice-enforcement`.
- "Make a Sunday recap kit from this sermon video." → triggers `sermon-content-kit`.
- "Review this slide for me." → triggers `creative-director`.
- "Draft a GMB post for next Thursday." → triggers `gmb-weekly-post`.
- "Write a parent text from REV." → triggers `kids-rev-comms`.

Or use the slash commands when you want a one-shot result without explanation.

## Connectors

This plugin assumes the team has these connected. Skills won't fail without them, but they make the work much faster:

| Tool | What it's used for |
|---|---|
| Notion | Creative Briefs hub, DB · Events, knowledge base |
| Monday.com | Action plans, content calendars |
| Slack | Team comms, draft sharing |
| Gmail | Sending campaigns, capturing replies |
| Google Calendar | Service rhythm, event scheduling |
| Google Drive | Asset storage, photo libraries |

## Brand voice

The full 22-page Love Church Brand Voice Guidelines are embedded at `skills/brand-voice-enforcement/references/brand-voice-guidelines.md`. That file is the source of truth for all content the plugin produces.

## Maintenance

When you update the brand-voice guidelines, update the file at `skills/brand-voice-enforcement/references/brand-voice-guidelines.md`, bump the version in `.claude-plugin/plugin.json`, and rebuild the `.plugin` zip.

To rebuild:

```bash
cd /path/to/love-church-brand && zip -r /tmp/love-church-brand.plugin . -x "*.DS_Store"
```

## Credits

Built by Adam Deidel for Love Church (Omaha, NE).
Voice and design discipline drawn from the Love Church Brand Voice Guidelines, the Core Style Brand Guide, the Love Leadership Playbook, and the @lovechurchomaha Instagram audit.

*Voice is constant. Tone flexes by context. When in doubt: Celebrate. Connect. Invite.*
