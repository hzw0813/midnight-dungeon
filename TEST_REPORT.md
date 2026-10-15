# v0.2.0 Regression Report

Date: 2026-10-16 (Asia/Taipei)
Test platform: Headless Chromium, 390×844 mobile emulation, Playwright. This is **not** a real iPhone Safari test.

## Passed
- 2,000 seeded games: valid save states, reachable exits and entity placements, deterministic replay.
- 16 floor transitions / 16 distinct three-choice rewards.
- Floor 5, 10, 15 bosses must be defeated before portal can be used.
- XP/level-up, deaths and one-time coin conversion, permanent talent effects across runs, shop costs, v0.1 save migration.
- Mobile touch directional controls, map swipe, shop, rewards, camp, persisted state simulation.
- JavaScript page errors: 0.
- Mobile widths 375, 390, 430 tested for horizontal overflow.

## Unverified
- Real Safari behavior, actual phone localStorage policy, live site loading in iPhone, long-term difficulty and extreme-depth endurance.
- Full local test script and mobile screenshots are also archived in `midnight_dungeon_v0.2.zip`.
