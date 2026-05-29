---
description: Build the full Sunday recap content kit — IG, blog, email blurb, YouTube metadata, and social clips.
---

The user is asking for a Sunday recap kit. This is a multi-platform output, not a single post. Invoke:

1. `love-church-context` for org facts.
2. `brand-voice-enforcement` for voice on every output.
3. `sermon-content-kit` for the full 21-section template (YouTube, IG carousels, X, LinkedIn, blog, email, podcast, group questions, SEO, hook bank).
4. `ig-sundays-recap` if the user only wants the IG Sundays-at-Love piece (high engagement bucket).

Confirm:

- Sermon source (video file, audio, transcript, or "I'll fill you in").
- Speaker (default: current Lead Pastor).
- Series + message title.
- Output format (single .md kit, separate files per platform, or chat output).
- Whether to include the Instagram Sundays-at-Love piece as part of the recap or just the standard sermon-content-kit.

If a sermon video or audio file is provided:
- Run the bundled transcribe.py to produce timestamped transcript.
- Use timestamps for YouTube chapters and short-form clip windows. Never invent timestamps.

Deliver per the sermon-content-kit template — one master markdown file in the workspace folder named `<Message-Title-Kebab-Case>_Content-Kit_P2.md`. Provide a computer:// link.

After delivery, ask if the user wants individual pieces split out (e.g., `youtube.md`, `instagram.md`) or a Notion publish.
