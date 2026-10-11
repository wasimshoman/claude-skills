---
name: logo-reveal-reel
description: Plan and produce short vertical "phone films the laptop" logo-animation reels — an After Effects logo build shown on screen, beat-cut into brand mockups, looping. Use for logo reveal reels, logo animation concepts, motion-design social posts.
---

# Logo Reveal Reel

A format distilled from analysis of ~36 unique motion-design reels (41 files, 6 duplicates). It's a design *grammar*. Never recreate the source creator's specific logos, or any real brand or character.

## 1. The format at a glance

- **Delivery:** 9:16 vertical, 720×1280 or 1080×1920, 30 fps, **6–21 s** (median ≈ 17 s). It loops.
- **The shot:** a phone, handheld or propped, films a laptop or monitor running After Effects. The camera sits 15–30° off-axis, usually low and looking slightly up. The room shows at the edges: warm ceiling lights, a desk, keyboard RGB. The AE timeline and panels stay partly visible, as proof that "this is real work". The animation fills about 50–70% of the frame.
- **Light:** dim, warm room; the screen is the brightest object. Dark comps glow, and white or brand-colour flashes light the room.
- **No voice-over, no captions on screen.** The caption carries one hook line plus hashtags (#aftereffects #logo #motiongraphics #logoanimation).

## 2. Two structures

**A. Reveal + mockups (≈70% of posts).** These have 3–15 hard cuts, all landing on the beat (median offset from the nearest beat is 0.1–0.2 s).
1. **Seed (1 bar):** one primitive on a dark comp: a dot, a line, a rectangle or a ring.
2. **Construct (1 bar):** construction geometry such as guide lines, circles and grid sweeps. The mark is "drawn" by its own geometry.
3. **Form (1 bar):** the primitive morphs or snaps into the mark with an overshoot ease (ease-out with about 5–10% bounce). Optional effects: glitch or pixel-scatter, a 3D extrude, a light sweep.
4. **Lockup (1 bar):** the wordmark builds letter by letter, or slides out from behind the mark.
5. **Flash (½ bar):** the background swaps from dark to white or to the brand colour, cut on the downbeat.
6. **Mockups (½ bar each, 3–5 of them):** a social profile on a phone over a brand-colour field, a cap or tee, a business card or wallet, a poster with a large headline, an app-icon grid, a watch face, or a 3D sphere or badge. Keep the mark in roughly the same screen position from cut to cut.
7. **Loop:** end on the seed primitive so the restart is seamless.

**B. One-shot build (≈30%).** There are no cuts: a single continuous construction (letter-by-letter title reveals, particle or light assemblies, signature write-ons). It suits cinematic or ambient music and slower tempos.

Run `python3 scripts/beatsheet.py` (source in the Appendix; write it to disk if absent): `python3 scripts/beatsheet.py --bpm <bpm> --brand <NAME> [--mode reveal|oneshot] [--mockups N]` to get a timed shot list.

## 3. Mark & motion design rules

- Each mark comes from **one primitive plus one idea**: a letterform (A, X, M, V) built from 2–3 geometric strokes, or a pictogram.
- The palette is **one hero colour plus black and white**: electric blue, magenta, signal red, teal-green or emerald. On dark comps the hero colour may glow.
- Typography is a geometric or grotesk sans, bold, wide-tracked for the wordmark. A mono or stencil face is fine for tech brands.
- **Motion vocabulary:** stroke draw-on (trim paths), mask wipes, scale-from-0 with overshoot, rotation snaps of 90°/180°, a split into parts that reassemble, pixel or glitch dissolve, extrude/3D turn, light sweep across the face, and a colour-fill flood behind it.
- Hold the finished lockup for at least ½ bar before cutting. Viewers need a readable frame.

## 4. Music

Measured across the set:

- **Tempo:** a dominant cluster at **117–123 BPM**, with 108–112 for calmer pieces and 144–172 for cinematic or one-shot builds. The 59 BPM tracks are ambient pads.
- **Character:**
  - Reveal reels use bright, punchy electronic or house-pop with a clear kick and a pronounced riser into the drop. Percussive energy is often higher than harmonic, and spectral centroid runs 2.6–3.6 kHz.
  - One-shot builds use dark, cinematic tension with sub-hits and whooshes, lower brightness (0.7–2 kHz) and sparse percussion.
- **Sync:** time the Form/Flash moment to the **drop or the first big downbeat**, cut every mockup on a beat, and add one SFX "hit" (whoosh, impact or glitch tick) on the mark resolve.
- **Licensing:** use Instagram's music library (it's licensed for in-app posting) or royalty-free or licensed tracks (Artlist, Epidemic, Musicbed and similar). Don't reuse audio ripped from other creators.

## 5. Filming checklist

Phone at 30 fps, 4K if possible, exposure locked to the screen (tap and hold, then pull exposure down about −1 EV). Turn off auto-brightness and Night Shift on the laptop. Let the AE preview play at full speed (pre-render, or use RAM preview). Move the camera a little: a slow push-in or a few degrees of drift, never a static tripod look. Shoot 2–3 takes and keep the one where the cuts land cleanly.

## 6. Workflow when asked to make one

1. Get the brand name, sector, one adjective, a hero colour, and a BPM or mood. If any is missing, choose and state it.
2. Propose **2–3 mark concepts** (primitive → idea → motion) in words or rough SVG, and get approval before building.
3. Produce the beat sheet (script), the AE build notes per shot (layers, effects, easing), a mockup list, a music brief (BPM, mood, where the drop lands) and a caption.
4. Optionally render a preview as an animated HTML/SVG page or CSS keyframes so the timing can be checked before AE work.
5. QA before you call it done:
   - Every cut is on a beat.
   - The lockup is held for at least ½ bar.
   - The loop is seamless.
   - The mark is legible at phone size.
   - Only one hero colour is used.
   - No real-world trademark or character appears.

## 7. Guardrails

Only invent original brands, or use the user's own brand with their permission. Don't animate or mock up real company logos, film or TV titles, or characters (the source set included fan concepts of real brands and characters; leave those out). Don't copy the source creator's specific marks, or present output as theirs.

## Appendix: scripts/beatsheet.py

```python
#!/usr/bin/env python3
"""Generate a beat-locked shot list for a 'phone-films-laptop' logo reveal reel.
Usage: beatsheet.py --bpm 120 --brand "NOVA" [--mode reveal|oneshot] [--mockups 4]
Prints a markdown table: time, beat, shot, on-screen action, camera note."""
import argparse
p = argparse.ArgumentParser()
p.add_argument("--bpm", type=float, default=120)
p.add_argument("--brand", default="BRAND")
p.add_argument("--mode", choices=["reveal", "oneshot"], default="reveal")
p.add_argument("--mockups", type=int, default=4)
a = p.parse_args()
beat = 60 / a.bpm
bar = 4 * beat
MOCKS = ["phone profile on brand-colour field", "merch (cap / tee / hoodie chest)",
         "business card or wallet", "poster with big headline", "app icon grid",
         "smartwatch face", "3D badge / sphere"]
rows = []
t = 0.0
def add(bars, shot, action, cam):
    global t
    rows.append((t, t / beat, shot, action, cam)); t += bars * bar
if a.mode == "reveal":
    add(1, "Seed", "single primitive (dot/line/rect) appears on dark comp", "slow push-in, AE timeline visible")
    add(1, "Construct", "construction lines / circles sweep, geometry snaps", "hold; slight handheld drift")
    add(1, "Form", f"primitive morphs into the {a.brand} mark, overshoot ease", "hold")
    add(1, "Lockup", "wordmark builds letter by letter beside mark", "small tilt toward screen")
    add(0.5, "Flash", "colour/background swap (dark->white or brand colour)", "cut ON downbeat")
    for i in range(a.mockups):
        add(0.5, f"Mockup {i+1}", MOCKS[i % len(MOCKS)], "hard cut on beat; mark in same screen position")
    add(1, "Loop", "return to seed primitive so the reel loops seamlessly", "match first frame")
else:
    add(1, "Seed", "primitive on dark comp", "static or very slow push")
    add(2, "Build", "continuous single-take construction, no cuts", "phone handheld at 15-25 deg angle")
    add(1, "Resolve", f"{a.brand} lockup settles, glow/light sweep", "hold 1 bar")
    add(1, "Loop", "dissolve/reverse back to seed", "match first frame")
print(f"BPM {a.bpm:g} | beat {beat:.3f}s | bar {bar:.2f}s | total {t:.1f}s\n")
print("| t (s) | beat | shot | on-screen | camera |\n|---|---|---|---|---|")
for r in rows:
    print(f"| {r[0]:.2f} | {r[1]:.0f} | {r[2]} | {r[3]} | {r[4]} |")
```
