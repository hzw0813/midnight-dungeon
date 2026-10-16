# v0.4.0 Test Report — 2026-10-16

## Local automated suite passed
- Headless Playwright Chromium；**1,114 engine assertions**, 2,000 seeded game maps/replay/validation, 30-floor progression and relic choices.
- 50 floors checked for elite cadence: 20 elite floors, all three variants seen. Verified guard first-hit mitigation, brute windup, heavy strike and dodge cancel, hunter double movement.
- 360 independently seeded elite kill/drop checks: gold 189, soul 109, relic 62; identical seed reproduces chest prizes and game state. All 3 reward types collect correctly, with reload/relic choice checks.
- v0.1/v0.2/v0.3 save migration and original storage key preservation. Touch, choice modals, debug export, 320/375/390/430px without horizontal overflow; JS page exceptions: 0.
- A real-origin localhost page navigation check was attempted but blocked by environment policy (ERR_BLOCKED_BY_ADMINISTRATOR). No iPhone Safari verification yet.

## Reproduce
The repository `test_regression.py` provides the smaller smoke test (Python Playwright + /usr/bin/chromium). The full local test suite and screenshots are bundled in `midnight_dungeon_v0.4.zip`.

## Remaining risks
Real iPhone Safari performance/touch/storage, actual end-to-end GitHub Pages browser load, very deep floors and difficulty balance.
