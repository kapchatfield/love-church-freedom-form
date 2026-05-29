---
name: weekly-email-newsletter
description: Write the all-church weekly email newsletter for Love Church. Triggers when the user asks for "the weekly email," "all-church email," "newsletter," "Friday email," "MailChimp send," or any standing congregational email. Follows the Celebrate · Connect · Invite rhythm baked into the Love Church voice guidelines. Output is ready to paste into the email platform, with subject line, preheader, body, CTAs, and image direction.
---

# Weekly All-Church Email

The weekly email lands in member inboxes. It's the most direct surface to the church family. Make it warm, useful, and Sunday-prep — not a marketing blast.

## When to trigger

- "Weekly email."
- "All-church email."
- "Friday email." (or whatever day the church sends)
- "Email blast about [topic]."
- "Newsletter for this week."

## What you need

1. **Send date and audience.** All-church or a segment? When does it go out?
2. **What's preached this Sunday?** Title, series, takeaway in one line. Speaker if not Pastor Mike or Pastor Todd.
3. **What's happening this week?** 1–3 events, sign-ups, or moments to highlight. Don't list everything — pick the 1–3 that actually matter.
4. **Big celebration?** Baptisms, big offering moment, milestone, transition update.
5. **Sermon series art or hero photo?** Image direction or filename.

If the user says "same as last week's structure," default to the structure below.

## Output structure — Celebrate · Connect · Invite

### Subject line (≤50 characters)

Italic-accent headline pattern works well even in subject lines:

- "There's More *to Life*"
- "This Sunday at Love"
- "*Real People. Real Life.*"

Avoid emoji in subjects. Avoid "Don't miss." Avoid SHOUTING.

### Preheader (≤90 characters)

The line that appears next to the subject in inbox previews. Use it to set the takeaway:

- "Pastor Mike on Joshua 3 — and a story you'll want to hear."
- "Sunday + how to be part of what's coming."

### Body — 4 sections, in order

**1. Hero / opening (Celebrate)**
A 2–3 sentence open. Lead with what God did this week, or what's true. Plain language. No "We're so excited to announce." Real voice.

**2. This Sunday (Invite)**
Short paragraph: who's preaching, the message title, the one-line takeaway, service times (9:00A + 11:00A in person, 5:00P online). Pair Plan Your Visit + Watch Online buttons or links.

**3. This Week / Connect (Connect)**
1–3 items max, with one-line descriptions and a single link each. Items can include:
- A group sign-up window
- A serve team need
- A ministry event (Love Out Loud, Agape, Valor, Marriage, Love Kidz, REV, 180 Omaha)
- A class or training
- An outreach opportunity

If you have more than 3 items, *don't list them all*. Pick the top 3. Long lists kill click-through.

**4. Closing**
One short closing thought from the lead pastor's voice or a verse for the week. Sign off:

- "Love,"
- "Pastor Mike & Jerica O'Connell" (or the appropriate signer)

### CTAs

Default pair: **Plan Your Visit** + **Watch Online** in the Sunday section.

Other CTAs as needed: **Sign Up**, **Give**, **Read More**, **RSVP**.

Use no more than 4 CTAs total in the email. Each CTA in its own line/button — not a list.

### Footer

- Address: 20120 Blue Sage Pkwy, Omaha, NE 68130
- Phone: 402.305.7717
- Web: lovechurch.org
- Social: @lovechurchomaha
- Unsubscribe link (let the email platform inject this).

## Voice rules

This skill runs alongside `brand-voice-enforcement`. Voice is constant. Tone for the weekly email is:

- **Formality:** Medium
- **Energy:** Medium (steady, warm)
- **Technical depth:** Low–Medium
- **Key principle:** Celebrate · Connect · Invite. In that order.

## Common failure modes

- **Announcement-y opening.** "We have lots of exciting things happening this week!" Fix: lead with a story, a celebration, or a verse.
- **Listing every event.** Kills CTR. Fix: pick the top 3.
- **No call to action in the Sunday section.** Fix: always Plan Your Visit + Watch Online.
- **"Service" instead of "Encounter" or just "Sunday."** Fix: use the LC vocabulary.
- **Missing signer.** Members read the email in the lead pastor's voice. Sign it.
- **Generic "have a blessed week" close.** Off-voice. Fix: a specific scripture, a sentence with weight, or just "Love, Pastor Mike."

## Delivery

Hand off in this format so the email-team can paste straight into the platform:

```
SUBJECT: [≤50 chars]
PREHEADER: [≤90 chars]

---

BODY:

[Section 1: Hero / Celebrate]
[copy]

[Section 2: This Sunday / Invite]
[copy]
[CTA: Plan Your Visit] [CTA: Watch Online]

[Section 3: This Week / Connect]
1. [item + 1-line description + CTA]
2. [item + 1-line description + CTA]
3. [item + 1-line description + CTA]

[Section 4: Closing]
[copy]

[Signer: Pastor [Name]]

---

IMAGE: [direction or filename for hero image]

NOTES: [anything for the email team]
```

If the user wants a Saturday "Sunday prep" version (lighter, just the message + invite), keep sections 1, 2, and 4 only.
