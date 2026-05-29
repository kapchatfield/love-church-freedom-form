---
description: Generate an Instagram or social post for Love Church from a topic or sermon takeaway.
---

The user is asking for an on-brand Love Church social post. Invoke the relevant skills to produce it correctly:

1. Load `love-church-context` for org facts, leadership, vocabulary, channels.
2. Load `brand-voice-enforcement` and read the embedded brand-voice-guidelines.md.
3. If the post is a Sunday recap, invoke `ig-sundays-recap` and follow that workflow exactly.
4. For all other social posts (sermon teaser, testimony, ministry highlight, event push, announcement), use the LC voice and the recurring patterns:
   - Italic-accent headline pattern when the medium supports it.
   - Lead with person, story, or moment — never "We're so excited to announce."
   - One CTA per post (default: Plan Your Visit + Watch Online for guest-facing).
   - 1–2 hashtags max (`#lovechurchomaha` + one contextual).
   - No emoji-stuffed copy. No stock photo direction.

Ask the user for:
- The topic/takeaway/event being promoted.
- Which channel (IG feed, IG Story, IG Reel, X, LinkedIn).
- Any photo or video assets ready, or whether you should produce direction.

Deliver:
- Caption (copy-pasteable).
- Hashtag line.
- Photo/visual direction if assets aren't picked yet.
- One-line note on optimal post time/window if the user wants it.

If the request is for multiple posts (a campaign), produce them in series and number them.
