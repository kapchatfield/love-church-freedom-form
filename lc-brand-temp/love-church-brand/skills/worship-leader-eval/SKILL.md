---
name: worship-leader-eval
description: "Evaluate worship leader performances from uploaded video files. Use this skill whenever the user uploads a video of a worship leader, worship set, worship moment, spoken word transition, or any live church performance and wants structured feedback. Also trigger when the user mentions 'worship evaluation', 'worship leader feedback', 'worship review', 'worship leader eval', 'evaluate this worship set', 'Bob Kauflin', or asks for feedback on a worship performance. This skill handles the full pipeline: interviewing the user for context, extracting and analyzing video frames, and generating a polished .docx evaluation document with timestamp-based feedback."
---

# Worship Leader Evaluation Skill

## Overview

This skill produces professional worship leader evaluations from uploaded video files. It follows the Bob Kauflin (Worship Matters) framework and outputs a polished, hand-off-ready .docx document with four structured sections of feedback.

## Workflow

### Step 1: Interview (Always Do This First)

When a video is uploaded, ALWAYS ask these four clarifying questions before analyzing:

1. **Who is the worship leader?** Name and experience level (newer/still growing, mid-level/refining, seasoned/sharpening).
2. **What was the service context?** (Normal Sunday, Easter, special series, etc.)
3. **Room size?** (Rough number — a few hundred vs. a thousand+)
4. **Specific coaching focus?** What area is the director already working on with this leader? (e.g., command, depth, transitions, engagement, confidence, delivery, eye contact, verbal transitions, theological depth, energy management)

The experience level and coaching focus fundamentally change the calibration of the feedback. What's a win for a 2-year leader is a baseline expectation for a seasoned one. Do NOT skip this step.

### Step 2: Video Analysis

Extract frames from the uploaded video at regular intervals to build a visual timeline of the performance. Adapt sampling rate to video length:

- **Under 3 minutes**: Every 10 seconds
- **3–6 minutes**: Every 15 seconds
- **Over 6 minutes**: Every 20 seconds

```bash
mkdir -p /home/claude/eval_frames
ffmpeg -i [VIDEO_PATH] -vf "fps=1/[INTERVAL]" -q:v 2 /home/claude/eval_frames/f_%03d.jpg
```

Review ALL extracted frames to observe:

- **Body orientation** — Is the leader facing the congregation or turned away?
- **Eye contact** — Eyes open and scanning vs. closed?
- **Gestural engagement** — What are the hands doing? Open palm, raised, passive?
- **Facial expression** — Engaged, authentic, performative, disconnected?
- **Team engagement** — Are the vocalists/choir behind them engaged or static?
- **Congregation response** — Hands raised, clapping, standing, passive?
- **Lyrics on screen** — What song is being performed? What section of the song?
- **Moment type** — Is this singing, spoken word, Scripture reading, prayer, transition?
- **Dynamic arc** — Is the energy building, sustaining, or declining across the clip?
- **Props/tools** — Bible in hand, notes, instrument, hands-free?

### Step 3: Determine Moment Type

The evaluation approach changes based on what kind of moment this is:

| Moment Type | Primary Evaluation Lens |
|---|---|
| **Song performance** | Vocal delivery, physical engagement, dynamic leadership, congregation leading |
| **Spoken word / Scripture** | Delivery cadence, body language, eye contact, declarative vs. recitative posture |
| **Transition between songs** | Verbal depth, theological content, pacing, pastoral shepherding |
| **Prayer moment** | Authenticity, pacing, congregational invitation, emotional range |
| **Altar call / response** | Sensitivity, clarity of instruction, pastoral warmth, reading the room |

### Step 4: Generate Evaluation Document

Produce a .docx file using the `docx` skill (read `/mnt/skills/public/docx/SKILL.md` before generating). The document must follow this exact four-section structure:

#### Section 1: WHAT YOU DID WELL
- Specific, timestamp-based encouragement
- Tie observations to exact visual moments from the frames
- For newer leaders: celebrate fundamentals (confidence, posture, song selection)
- For seasoned leaders: highlight elite-level moments (dynamic control, pastoral instinct, team influence)
- Note when the team or congregation visibly responds to the leader's cues

#### Section 2: AREAS TO GROW
- Clear, constructive, tied to exact moments with timestamps
- Calibrate to experience level:
  - **Newer leaders**: Focus on 2-3 foundational areas (eye contact, body orientation, basic verbal transitions)
  - **Seasoned leaders**: Push into nuanced areas (delivery mechanics, gestural congruence, dynamic command, the gap between content quality and physical delivery)
- Always frame as "the next layer" rather than deficiencies
- Address the specific coaching focus the director identified

#### Section 3: SPIRITUAL LEADERSHIP INSIGHT
- Evaluate how well they led people TOWARD worship, not just performed
- Distinguish between worshipping and leading worship (both matter, but they're different skills)
- For Easter/special services: address how well they served guests and first-time visitors
- Identify the leader's strongest spiritual instinct and where their pastoral presence could deepen
- Be theologically grounded but not preachy

#### Section 4: ACTION STEPS FOR NEXT WEEK (2-3 Steps)
- Each step must be **practical** and **measurable**
- Include a specific drill, exercise, or self-evaluation method
- Give the leader something they can do THIS WEEK, not "over time"
- Tie each step back to a specific observation from the video
- Calibrate difficulty to experience level

### Document Formatting Guidelines

- **Header block**: Leader name (large), evaluation label, service context, song/moment identification
- **Context metadata**: Experience level, room size, coaching focus, moment type — displayed in a clean table
- **Section headers**: Color-coded by section (green for strengths, amber for growth, purple for spiritual insight, blue for action steps)
- **Timestamps**: Formatted in accent color with bold weight, followed by observation text
- **Tone**: Written as if FROM the worship director TO the worship leader — warm, pastoral, direct, growth-oriented. Ready to copy/paste and hand directly to the leader.
- **Closing**: Personal sign-off from the director with a final word of encouragement
- **Footer**: Framework attribution (Bob Kauflin / Worship Matters)

### Step 5: Present the Document

After generating the .docx, copy it to `/mnt/user-data/outputs/` and use `present_files` to share it. Provide a brief summary highlighting:
- The moment type (song, spoken word, transition, etc.)
- Top 2-3 wins
- Top 2-3 growth areas
- The core tension or theme of the evaluation

## Voice and Tone Guide

The evaluation should read as if written by Bob Kauflin — author of "Worship Matters" and Director of Sovereign Grace Music. That means:

- **Encouraging but not flattering** — Every compliment is tied to a specific observable moment
- **Direct but not harsh** — Growth areas are framed as "the next layer of your calling"
- **Theologically grounded** — References to the purpose of worship leading (shepherding, not performing)
- **Practically minded** — Every observation leads to something actionable
- **Calibrated to the leader** — A seasoned leader gets sharper, more nuanced feedback than a newer one

Avoid:
- Generic praise ("Great job!")
- Vague criticism ("Work on your stage presence")
- Performance-only language (this is worship leading, not concert performing)
- Spiritual bypassing ("Just let the Spirit lead" without practical application)

## Calibration by Experience Level

| Area | Newer Leader (1-3 yrs) | Mid-Level (3-7 yrs) | Seasoned (7+ yrs) |
|---|---|---|---|
| Eye contact | Introduce 70/30 rule | Refine scanning patterns | 90%+ open during spoken |
| Body orientation | "Face forward" basics | Room coverage rotation | Never lose a section |
| Verbal transitions | Write one line per song | Extemporaneous depth | Theological precision |
| Dynamic command | Follow the band's energy | Shape the energy | Direct the wave |
| Gestural engagement | Basic hand awareness | Intentional gestures | Full-body congruence |
| Team leadership | Awareness of team | Vocal team management | Real-time influence |

## Edge Cases

- **Multiple leaders in the clip**: Ask the director which leader to evaluate. If both, create separate documents.
- **Poor video quality / dark lighting**: Note what you can and cannot assess. Don't fabricate observations.
- **Very short clip (<60 seconds)**: Acknowledge the limited sample. Focus on what's observable and note what a longer clip would reveal.
- **No lyrics visible on screen**: Ask the director what song this is, or note that song identification was not possible from the video.
- **Non-singing moment (spoken word, prayer, Scripture)**: Shift evaluation lens entirely — see Moment Type table above. This is NOT a lesser evaluation; these moments often reveal more about a leader's pastoral depth than singing does.
