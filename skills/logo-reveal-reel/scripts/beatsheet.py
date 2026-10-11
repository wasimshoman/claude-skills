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
