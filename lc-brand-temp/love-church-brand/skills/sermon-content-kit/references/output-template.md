# Output Template — WordPress P2-Ready Master File

The master markdown file follows this exact structure. Populate every section. Every run. The team splits this document across multiple owners and an empty section is worse than one that's slightly thin.

File name convention: `<Message-Title-Kebab-Case>_Content-Kit_P2.md`
Save to the workspace folder so the user gets a `computer://` link.

---

## Header

```
# <Message Title> — Full Content Kit

**Message:** <title>
**Teaching Pastor:** <name, role>
**Series:** <series name / book>
**Primary text:** <scripture ref>
**Runtime:** <MM:SS>
**Formatted for:** WordPress P2 — paste section-by-section into posts, or publish the full kit as one long post and use section anchors.
```

## YOUTUBE

1. **SEO Title — 3 variations.** One curiosity+keyword, one tension+clarity, one benefit-led. Include "| Love Church" or speaker's name where natural.
2. **Thumbnail Copy — 5 options.** 4–6 words per option. High-contrast, bold sans-serif, paired with tight crops of the preacher. Note when a quote from the sermon is also thumbnail copy.
3. **SEO Description.** Hook (2–3 sentences of tension), summary of what's inside, `lovechurch.org` CTA, socials, a keyword line at the bottom (`**Keywords:** ...`) that's natural-language not stuffed.
4. **Chapters / Timestamps.** 8–14 chapters in a code block, anchored to `transcript.txt`. Every chapter starts at the real segment. Title each chapter in the preacher's language, not a generic summary.
5. **Pinned Comment.** Ask a question the audience can actually answer (not "what did you think?"). Offer prayer for commenters using 🙏.

## INSTAGRAM

6. **Carousel #1 — Core Message.** 8–10 slides. Slide 1 is tension; slides 2–3 are the thesis; middle slides are the structural points one-by-one; final slide is the CTA. Include a caption paragraph.
7. **Carousel #2 — Emotional / Relatable.** 7–9 slides. Softer tone, less typography, more "you" language. Opens with the felt question the preacher asked. Caption invites a quiet response (save, share, 🙏).
8. **Carousel #3 — Practical Application.** 6–8 slides. Journal-style. One question or one action per slide. Ends with a screenshot-and-save CTA.
9. **Short-Form Clips — 5–10 clips.** Each clip gets: a hook (first 2 seconds spoken), caption (mobile-optimized, short lines), on-screen text line (ALL CAPS, typography only), and **source timestamp range** from the transcript. Aim for 30–75 seconds per clip.
10. **Quote Graphics — 5–8 lines.** Verbatim from the sermon. Short enough to fit a 1080x1080 with room to breathe (15 words or fewer ideally). Attribution line: `<Speaker> | Love Church | <Message Title>`.

## X (TWITTER)

11. **Post #1 — Punchy insight.** Line breaks between thought-beats. One quote or insight. Under 280 chars.
12. **Post #2 — Contrarian / thought-provoking.** Opens with a contrast or challenge. Ends with a soft pointer to the full message (lovechurch.org).

## LINKEDIN (TEACHING PASTOR)

13. **Post #1 — Leadership insight.** 3–5 short paragraphs. Pulls one sermon idea into a leadership lens. No scripture citation required; the pastor's credibility comes from the quality of the insight.
14. **Post #2 — Personal reflection.** First-person. Based on a specific story the preacher told from stage. Ends with a small invitation, not a pitch.

Both posts close with a light tie to Sunday ("preached on this Sunday at Love Church — happy to share the full message if useful").

## BLOG / WEBSITE

15. **Message Recap Blog (600–900 words).** Opens with the thesis as a blunt declarative. Walks through the structure the preacher actually used. Includes 3–5 full quotes (in blockquote formatting). Ends with "so what do you do this week?" — 2–3 concrete questions. CTA to watch the full message.

## EMAIL

16. **Newsletter.** Two subject-line options, one preview text line, body of ~200 words. Short paragraphs. One P.S. line that invites a reply for prayer.

## PODCAST

17. **Podcast Episode Package.**
    - Episode title (mirrors YouTube title but stripped of YouTube-ish verbiage)
    - Short description (160 chars for app display)
    - Long description (3–4 paragraphs)
    - Show notes with the same timestamps as YouTube chapters
    - List of scriptures referenced (bullets)
    - Connect block (web, socials, subscribe line)

## COMMUNITY / DISCIPLESHIP

18. **Community Post.** Either a poll with 3 options tied to the structural points, or an open question that invites honest reflection. Keep the prompt concise (2–4 sentences).
19. **Discussion Guide — 5–7 questions.** Formatted for small groups / D-groups / Rooted-style groups. 45–60 minute arc: one opener, 1–2 Word questions (read the primary text together), 3 principle questions (one per structural point), one "walk it out" question, one prayer move.

## SEO / STRATEGY

20. **Keywords & Tags — 10–15.** Numbered list. Include speaker name, church name, city, sermon-specific phrases, and one or two broad Christian-search terms. Plus a comma-separated `YouTube tags` line ready to paste.
21. **Hook Bank — 10 hooks.** For future short-form and carousel reuse. Should be transferable — usable for other sermons in the same vein, not just this one.

## APPENDIX — NOTES FOR THE CREATIVE TEAM

- Speaker name and role.
- Preferred phrases to weave in where natural (pull from `brand-voice.md` culture phrases).
- Language to avoid (pull the short list from `brand-voice.md`).
- CTAs (web, socials, podcast).
- Timestamp provenance (note if pulled from the full video vs. approximated from a summary).

---

## Formatting notes

- Use `## SECTION` for each top-level platform and `###` for numbered deliverables.
- Use fenced code blocks only for chapters and YouTube tag strings. Everything else should be prose / bullets that paste cleanly into WordPress.
- Blockquote (`> ...`) sermon quotes in the blog, email, and Insta captions where the quote is doing the work. Don't blockquote within slide bullets.
- Link URLs as plain text (`lovechurch.org`) — no markdown link syntax. P2 auto-links plain URLs.
- Never use HTML or tables. P2 renders both inconsistently.
