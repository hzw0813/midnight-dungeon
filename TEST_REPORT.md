# Midnight Dungeon v0.5.1 — Visual Feedback Regression

Date: 2026-10-16, Asia/Taipei

## Automated test results
- JavaScript syntax checked with Node.js: PASS.
- Playwright headless Chromium `test_regression.py`: 1,114 engine assertions PASS; 2,000 seeded maps valid and deterministic, 30 floors, 10 relic offers, 360 elite cache results (189 gold / 109 soul / 62 relic), legacy save compatibility; widths 320/375/390/430 pass; JS page errors 0.
- `test_visual_fx.py`: 13 pure-FX assertions plus UI tests PASS; crit floating text, healing, kill, loot, relics, animation cleanup and v0.4 migration unchanged.
- `test_hit_visibility.py` (in downloadable ZIP): normal hit activates `impact-hit` map highlight and damage number; test button displays teal hit and gold crit, preserves save and turn; in reduced-motion mode static damage text remains visible; FX nodes disappear after timeout; migration from v0.5 save preserves floor, coins, shards, relics and old backup.
- Headless Chromium screenshots and full test scripts are in ZIP.

## Not yet verified
- Actual iPhone Safari screen output, accessibility settings on user's device, network-deployed page behavior on Safari, and performance at extreme depth.
- This is a map-local tinted pulse, not an entire-device screen flash.
