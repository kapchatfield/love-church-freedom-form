---
name: kids-rev-comms
description: Write parent-facing and student-facing comms for Love Kidz (birth–5th grade) and REV (6th–12th grade) — weekly recap emails, parent texts, sign-up copy, event invites, volunteer recruitment, big-day comms (kids dedications, REV camp, etc.). Triggers on "Love Kidz email," "REV parent text," "kids ministry comms," "student ministry update," "REV invite," "kids volunteer ask," or any family-facing copy for the next-gen ministries. Output respects the LC voice and the specific tone of parent/student audiences.
---

# Love Kidz & REV Comms

Family ministry comms have a different audience than the all-church email — parents are scanning during carpool, students are reading on TikTok-attention spans. Adjust accordingly.

## When to trigger

- "Write a Love Kidz weekly recap."
- "REV parent text for this week."
- "Volunteer ask for the kids team."
- "Sign-up copy for REV camp."
- "Kids dedication invite."
- "Big REV night announcement."

If the user doesn't say which ministry, ask. Love Kidz and REV have different vocabularies and different audiences.

## Audience profiles

### Love Kidz (birth–5th grade) → parents
- Reading on a phone between work, school pickup, and dinner.
- Wants the *one thing they need to know* in the first sentence.
- Trusts Love Kidz leaders enormously — earn it back every week.
- Loves photos of their kid. *Always include or hint at photos when relevant.*

### REV (6th–12th grade) → split audience
- **Parents** want safety, schedule, transportation, and what their kid is being taught.
- **Students** want their friends, fun, real questions getting answered, and not being talked down to.

For a REV piece, ask whether the primary audience is parents or students — different formats, different voices.

## Voice for each audience

### Parent voice (Love Kidz + REV parents)
- **Formality:** Medium-low. Friendly. Real.
- **Energy:** Medium. Calm > hype.
- **Technical depth:** Low. Schedule, location, what to bring.
- **Key principle:** Reduce parent decision load. Give them what they need to say yes.

### Student voice (REV students)
- **Formality:** Low.
- **Energy:** Medium-high. Conversational.
- **Technical depth:** Low.
- **Key principle:** Sound like a person, not a brochure. Don't try too hard. Don't talk down.

## Output structures by piece

### Love Kidz weekly recap email
1. **Subject line** — "Love Kidz this Sunday" or "What we taught your kid this week"
2. **Open (1–2 lines)** — What was taught + the question to ask at dinner.
3. **Bible point + verse** — One verse, one sentence. NKJV by default; NIV/NLT if it's for a younger audience and readability matters.
4. **Conversation starter for the family** — "This week, ask your kid…"
5. **Heads-up** — Anything coming up (kids dedication, special week, costume Sunday, sign-up).
6. **CTA** — Plan your visit / sign up / volunteer.
7. **Sign-off** — Love Kidz Director or "The Love Kidz Team."

### REV parent update
1. **Subject** — "REV this week" / "Heads-up for REV parents"
2. **What we're teaching** — One sentence.
3. **What's happening** — Schedule, location, anything different from a normal week.
4. **What to expect** — Especially for trips, retreats, big nights.
5. **What to ask your student** — One conversation starter.
6. **Sign-off** — Pastor Ben Norvig (Next Gen) or REV team.

### REV student message (text/IG/Story)
1. **Hook** — One short line. Question, image, or imperative.
2. **The thing** — Where, when, who's invited.
3. **The why** — One reason to come (not five).
4. **CTA** — Show up, RSVP, bring a friend.

Examples:
- *"Tomorrow night. Pizza. Real questions. Bring someone. 6:30 at the church."*
- *"You don't have to have it figured out to come. We'd just love to have you. Wednesday 6:30."*

### Volunteer recruitment (for either ministry)
1. **The need** — Specific. "We need 4 more Love Kidz leaders for the 11A Encounter."
2. **The why** — One sentence on impact.
3. **What it looks like** — Time commitment, training, support.
4. **The ask** — Specific next step. Reply, sign up at lovechurch.org/teams, talk to [name].

## Voice rules

This skill runs alongside `brand-voice-enforcement` and `love-church-context`. Specific to next-gen ministries:

- **Use "Love Kidz" — note the z.** Not "Love Kids," not "kids ministry."
- **Use "REV" — all caps, no period.** Not "Rev" or "rev."
- **Pastor Ben Norvig** is Next Gen Pastor. He oversees REV.
- **Translate any insider terms** for first-time-guest parents (e.g., "Sundays at 9A and 11A — REV (our 6th–12th grade ministry) meets in the youth room.")

## Common failure modes

- **Wall-of-text email.** Parents bounce. Fix: 5–7 short blocks, lots of whitespace.
- **"Kids" instead of "Love Kidz."** Off-brand. Fix: use the proper name.
- **Trying-too-hard student copy.** "Hey fam, what's up, this Wednesday is gonna be 🔥🔥." Cringe. Fix: write like you'd text a teenager.
- **Burying the schedule/location.** Lead with the practical info — that's what parents are scanning for.
- **No sign-off person.** Family ministries trade on trust. Sign your name.

## Delivery

For email or weekly recap, deliver as ready-to-paste markdown with subject + preheader + body + CTAs.

For texts or short-form student comms, deliver as plain copy with a one-line note on the channel ("Send via Subsplash app push" / "Post to REV IG Story" / "Text via the REV blast list").

For volunteer recruitment, deliver in two flavors: an email version (longer) and a Slack/text version (short).
