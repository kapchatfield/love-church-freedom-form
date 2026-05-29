---
name: sermon-content-kit
description: Transform a sermon video, audio file, or transcript into a full multi-platform content kit for Love Church — YouTube (titles/thumbnails/description/chapters/pinned comment), Instagram (three carousels + short-form clips + quote graphics), X, LinkedIn (teaching pastor voice), blog recap, email newsletter, podcast show notes, community/discipleship discussion guide, SEO keywords and a hook bank. Use this skill whenever a sermon or teaching is the source and the user wants to "repurpose" it, "turn it into content," "make social posts from this sermon," needs "YouTube chapters from a message," asks for a "content kit," "preach kit," "sermon social," or uploads a sermon video/audio. Trigger this even when the user doesn't say "skill" or doesn't name every platform — if the source is a sermon and the ask is multi-platform output, this is the right tool. Baked in with Love Church brand voice, 5S Life language, and lovechurch.org CTAs by default, with per-run overrides supported for guest speakers or partner content.
---

# Sermon Content Kit

Turn one sermon into a full multi-platform content package. One input (video / audio / transcript) → one master markdown file formatted for WordPress P2 that covers every platform Love Church publishes to.

## Why this skill exists

Love Church's creative team publishes a sermon to roughly ten surfaces every week (YouTube long-form, Shorts, three IG carousels, reels, quote graphics, X, LinkedIn from the teaching pastor, a blog recap, an email, a podcast episode, a discipleship question for groups, SEO). Doing this by hand is a full day of work. Doing it badly — rushed captions, generic hooks, "leveraging" and "unpacking" verbiage — makes the sermon land worse than it preached. This skill captures the repeatable parts of that workflow so each run is fast and on-brand, and leaves the creative judgment (thumbnails, edit cuts, image selection) where it belongs: with the humans.

## When to use this skill

Use it whenever a sermon is the source and the output is multi-platform. A few shapes this takes:

- User uploads a sermon video (.mp4, .mov) and asks for content, social, or YouTube metadata.
- User uploads sermon audio (.mp3, .wav, .m4a).
- User pastes a transcript or sermon outline and asks for the same.
- User says "repurpose this message," "make a content kit," "turn Sunday into posts," "preach kit," "sermon social."
- User asks for any *one* of the deliverables (e.g. "just the YouTube description") — run the skill, do the analysis, and output that one section. Do not skip the full structural pass; good micro-copy depends on understanding the full message.

If the user is asking you to *evaluate* a worship set or spoken word — not repurpose a teaching — that's a different skill (`worship-leader-eval`). Sermon content kit is for the teaching pastor's message.

## Workflow

### 1. Interview the user (use the AskUserQuestion tool)

Before analyzing anything, confirm four things. These are the inputs most likely to make or break the output, and asking up front is far cheaper than redoing a carousel at the end.

1. **Speaker and title/series.** "Who is the teaching pastor? What's the sermon title and series if known?" If the user says "infer from the video," note that the title may not appear on-screen and they'll need to confirm at the end.
2. **Analysis depth.** Full pass with real timestamps (recommended) vs. light thematic pass vs. work from a pasted summary. Full pass requires the video; the others are faster and work from text.
3. **CTAs and links.** Default is `lovechurch.org` plus `@lovechurchomaha` on IG/X/TikTok and "search Love Church on Apple/Spotify" for the podcast. Ask if they want to include service times, a "next steps" page, or a specific campaign URL.
4. **Output format.** Default is a single WordPress P2-ready markdown file. Offer: single .md (recommended), one master .docx, separate files per platform, or plain markdown.

Skip this interview only if the current conversation already contains clear answers to all four — e.g., the user said "same setup as last week" or provided all of it in the initial prompt. When in doubt, ask; a 30-second question saves a 20-minute re-roll.

### 2. Transcribe (only if source is video or audio)

If the input is a video file, run the bundled transcription script. It extracts mono 16 kHz PCM audio with ffmpeg and runs faster-whisper locally. For a 20-minute sermon this takes roughly two minutes on CPU.

```bash
python scripts/transcribe.py <path-to-video-or-audio> <output-dir>
```

Outputs (in `<output-dir>`):
- `transcript.txt` — human-readable transcript with `[MM:SS]` timestamps at the start of every segment. Use this for grep, quote extraction, and copy/paste.
- `transcript.json` — structured segments with start/end seconds, for precise chapter markers and clip windows.

If the input is already a transcript (pasted text, a .txt, or a .docx), skip transcription entirely and work from that. If the input is an audio file, pass it to the same script — it handles both.

On first use the faster-whisper `small` model downloads (~460 MB). This is a one-time cost per environment. If you need speed over accuracy, change `small` to `tiny` in the script; if you need accuracy over speed, change it to `base` or `medium`.

### 3. Structure the sermon

Before generating anything, build a short internal map of the message. Read `references/structuring.md` for the checklist. The short version: identify the thesis, the scripture(s), the central illustration(s), the explicit/implicit main points, the key quotes with timestamps, and the altar call or closing move. Do not skip this. Every downstream deliverable — chapters, clips, quote graphics, discussion questions — is better when it's built from a clear structural map than when it's patched together from keyword search.

### 4. Apply brand voice

Read `references/brand-voice.md` once before writing. It's the Love Church voice guide — culture phrases to weave in naturally, language to avoid, tone notes, and CTA conventions. If the user has given per-run overrides (different speaker's voice, a guest church, a campaign-specific CTA), apply those on top of the defaults.

### 5. Generate the full kit

Follow the structure in `references/output-template.md`. This is the canonical 21-section template and should be the backbone of every run. Populate every section. Do not drop sections that feel redundant — the client's team splits this doc across multiple owners (video editor, social manager, email copywriter, small-groups pastor), and empty sections are worse than slightly-overlapping ones.

A few cross-cutting rules that matter more than the template itself:

- **Quote fidelity.** Every pull-quote, carousel slide, and short-form hook should be a real line from the sermon (verbatim or light cleanup). Invented quotes erode the preacher's trust in the kit and can misrepresent their message. Cite timestamps next to short-form clips so the editor knows where to cut.
- **Timestamps are load-bearing.** YouTube chapters and short-form clip windows must be anchored to the actual video. Never make them up. If the user chose "light pass" or "summary only," say explicitly in the chapter section that timestamps are approximate.
- **Tension openers.** Every hook — on YouTube titles, IG carousel slide 1, X posts, email subject lines — should open with tension or a felt question, not a statement of topic. Match the energy of the preacher's own opening. Read the hook bank in `references/brand-voice.md` for the pattern.
- **Two audiences, one voice.** Every piece should read naturally to both a committed Christian and someone exploring faith. If a line only works for insiders (requires jargon, church-world references), either cut it or rewrite it so both audiences can enter.
- **CTAs are invitations.** Never pressure. "You belong before you believe" is the posture. "Come forward right now if…" is the preacher's line; the social version is softer: "If this landed, here's where to go next."

### 6. Assemble and deliver

Write the full kit to a single markdown file in the user's workspace folder (`/sessions/<session>/mnt/<workspace>/`). File name convention: `<Message-Title-Kebab-Case>_Content-Kit_P2.md`. After writing, give the user a `computer://` link and a two-to-three paragraph summary of what's inside. Do not re-explain the sermon back to them — they preached it.

If the user asked for docx, separate files, or any other format, adapt the delivery step but keep the content identical. For .docx output, invoke the `docx` skill to format. For separate files, split the master doc along the top-level headings and name each file after its platform (`youtube.md`, `instagram.md`, etc.).

## Guardrails and common failure modes

- **Don't hallucinate scripture.** Only cite verses the preacher explicitly referenced, plus clear cross-references that are in the immediate text (e.g., "Judges 3:1-2" is explicit; "Zechariah 4:6" counts if they quoted it). If unsure, omit rather than invent.
- **Don't summarize the altar call as a CTA.** The in-room call to come forward is different from a social CTA. Translate the *invitation* (who this is for, what's being offered) into something watchable for someone at home.
- **Don't use emoji spam.** One emoji per social caption, max, unless the user requests more. Never in long-form (blog, email body, LinkedIn).
- **Don't use "unpack," "leverage," "intentionality," "dive in," "at the end of the day."** This list lives in `references/brand-voice.md`. It's there because it matters.
- **Don't over-format the P2 markdown.** Headings and bullets are fine. Avoid HTML, tables, and heavy nesting — WordPress P2 renders them inconsistently.

## What the user actually sees at the end

A single link to a file that their team can split up and ship by Monday. Not a victory lap in the chat. The file does the talking.

## Reference files

- `references/brand-voice.md` — Love Church voice guide. Read once before writing.
- `references/output-template.md` — The 21-section master template every run fills out.
- `references/structuring.md` — Short checklist for mapping the sermon before generation.
- `scripts/transcribe.py` — ffmpeg + faster-whisper transcription. Handles .mp4, .mov, .mp3, .wav, .m4a.
