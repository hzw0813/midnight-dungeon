# Midnight Dungeon v0.5.0 — Test Report
Date: 2026-10-16 (Asia/Taipei)

## Passed (Playwright headless Chromium)
- 本地完整引擎回歸：**1,114 引擎斷言**、2,000 種子、0 無法抵達的出口／不合法存檔／重播不一致。
- 30 層連續推進（10 次聖物選擇），精英 50 層節奏與三種技能；360 次 seeded 精英掉落：gold 189、soul 109、relic 62。
- v0.1 / v0.2 / v0.3 / v0.4 存檔轉換。v0.4 舊 key 保留，保有玩家樓層、HP、金幣、魂晶、天賦及聖物等級。
- **13 項動效純函式與相容性斷言**：暴擊傷害、擊殺、開箱、治療、升級、遊戲狀態不被特效修改。
- DOM：手機按鍵能觸發浮字；動畫後會清除；精英聖物獎勵採金色面板；減少動態效果時不生成浮字；debug 報告仍可使用。
- 模擬手機寬度 320/375/390/430px 無水平溢出。觀察到的 JS page exceptions：0。Node 內嵌 JavaScript 語法檢查通過。

## 限制
測試環境限制直接開啟 localhost/外部網頁，因此使用 Chromium 的 `page.set_content`、模擬 localStorage 與觸控事件測試。**尚未完成實體 iPhone Safari 或 GitHub Pages 站點端到端驗收**；不保證每種 iOS 版本效能一致。

完整測試腳本、測試輸出和手機截圖也封裝在 `midnight_dungeon_v0.5.zip`。
