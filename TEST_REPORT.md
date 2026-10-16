# Midnight Dungeon v0.5.2 — Test Report

日期：2026-10-16（Asia/Taipei）。環境：**Playwright headless Chromium 行動裝置模擬**，不是實體 iPhone Safari。

## 結果
- Node.js JavaScript 語法檢查：PASS。
- 引擎回歸：**1,114 項斷言 PASS**、2,000 張地圖種子無無效地圖、存檔或重播差異。
- 30 層連續推進、守衛與聖物三選一、精英行為與寶箱；360 次掉寶樣本（gold 189、soul 109、relic 62）：PASS。
- 13 項純視覺衍生事件斷言、不變更引擎狀態：PASS。
- v0.5.2 專項：320/375/390/430px × 正常／減少動態效果，\`#combatFeed .fx-float\` 全部在 \`#arena\` 下方，\`#fxLayer .fx-float\` 永遠為 0：PASS。
- 暴擊＋精英擊殺＋金幣同回合同時顯示，不遮擋角色、怪物與血條；光圈仍存在；自動清理：PASS。
- 試播按鈕不修改存檔／回合；v0.5.1 轉 v0.5.2 保留樓層、HP、XP、金幣、永久魂晶與聖物，舊 key 原封保留：PASS。
- 已跑 320/375/390/430px 橫向溢出檢查，觀察到 JavaScript page errors：0。

## 重新測試
- \`python test_regression.py\`
- \`python test_visual_fx.py\`
- \`python test_combat_readability.py\`（GitHub 精簡 smoke；ZIP 中附完整版）
- 完整 ZIP 另含 \`test_hit_visibility.py\`、Playwright 螢幕截圖。

## 尚未完成
實體 iPhone Safari 的顯示、動態設定、長期儲存政策與真實網址端到端測試。沒有對極深樓層的效能做壓測。
