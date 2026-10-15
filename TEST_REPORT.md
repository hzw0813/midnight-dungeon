# v0.1.0 Test Report

Date: 2026-10-16 (Taipei)

## Automated verification
- Browser: headless Chromium with 390×844 mobile emulation, touch enabled.
- Runtime JavaScript exceptions: **0**.
- Seeds checked: **1,500**.
- Invalid initial game states: **0**.
- Unreachable exit / loot / enemies: **0**.
- Same seed, same 20 operations, divergent state: **0**.
- Artificial floor transition / end-game checks: **30 passed**.
- Death / potion heal / wall no-turn checks: **10 each passed**.
- Tap controls, swipe navigation, debug export, restart: **passed**.

## Limitations
- Tests do not prove all maps can be won by every player strategy; dying is expected game behavior.
- Emulator runs Chromium, **not** physical iPhone Safari.
- Persistent `localStorage` across a real HTTP/HTTPS origin remains untested in the restricted test container.
- Public hosting/GitHub Pages is not configured in this package.