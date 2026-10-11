# logo-reveal-reel: user manual

An agent skill for planning and producing short vertical **"phone films the laptop" logo-animation reels**. The logo is built in After Effects on screen, cut on the beat into brand mockups, and the reel loops.

The skill is a style *grammar* taken from studying a motion-design reel format. It does not copy anyone's logos or videos, and it refuses real trademarks and characters.

## What's inside

```
logo-reveal-reel/
├── SKILL.md              # the skill: format, design rules, music brief, workflow, QA, guardrails
├── README.md             # this manual
└── scripts/
    └── beatsheet.py      # BPM -> timed, beat-locked shot list
```

## Install

| Where | How |
|---|---|
| **Claude (app / Cowork)** | Settings → Capabilities → Skills → upload the zipped `logo-reveal-reel` folder, or save it from a skill proposal card. |
| **Claude Code** | Copy the folder to `~/.claude/skills/logo-reveal-reel/` for all projects, or `.claude/skills/logo-reveal-reel/` for one repo. |
| **Claude API / Agent SDK** | Upload it as a custom skill (Skills API) and attach it to the container. |
| **Other agents** | Feed `SKILL.md` as a system or reference prompt, and expose `scripts/beatsheet.py` as a tool. |

## Use

Ask in plain language. The skill triggers on logo reveal or logo animation reel requests:

> "Make a logo reveal reel for **NOVA**, a fintech startup, hero colour electric blue, energetic, ~120 BPM."

The agent will then:

1. Confirm the brief: name, sector, adjective, hero colour, BPM or mood. It fills any gaps and tells you what it assumed.
2. Propose **2–3 logo concepts** (primitive → idea → motion) and **wait for your approval**.
3. Deliver:
   - A beat sheet
   - After Effects build notes for each shot
   - A mockup list
   - A music brief
   - A caption and hashtags
   - Optionally, an HTML timing preview
4. Run the QA checklist:
   - Every cut is on a beat.
   - The lockup is held for at least ½ bar.
   - The loop is seamless.
   - The logo is legible at phone size.
   - Only one hero colour is used.
   - No real trademarks appear.

### Beat sheet script

```bash
python3 scripts/beatsheet.py --bpm 120 --brand NOVA                # reveal + 4 mockups (default)
python3 scripts/beatsheet.py --bpm 120 --brand NOVA --mockups 5
python3 scripts/beatsheet.py --bpm 90  --brand NOVA --mode oneshot # single continuous take
```

It needs Python 3 and nothing else. Output is a markdown table with time, beat, shot, on-screen action and camera note. At 120 BPM, reveal mode gives a 15 s reel.

## Producing the reel (you)

1. Build the animation in After Effects following the build notes. Time the Form/Flash moment to the music's drop.
2. Play it back at full speed (RAM preview or a pre-render) on a laptop in a dim, warm room.
3. Film it with your phone:
   - 30 fps, 4K if possible.
   - Lock exposure on the screen at about −1 EV.
   - Hold the phone 15–30° off-axis, with a slow push-in.
   - Shoot 2–3 takes.
4. Cut the mockups on the beat. Post at 9:16, 6–21 s.
5. **Music:** use Instagram's in-app library or a licensed or royalty-free track. Never use audio ripped from other posts.

## Rules (built in)

- Use only original brands, or your own brand.
- No real company logos, film or TV titles, or characters.
- Don't copy the reference creator's marks, or present the work as theirs.

## Notes

The tempo and timing numbers came from automated audio and scene-cut analysis of ~36 reels. Treat them as typical ranges, not exact values.
