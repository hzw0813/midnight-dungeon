# v0.3.0 Regression Report — 2026-10-16

平台：Headless Chromium / Playwright，手機尺寸 320、375、390、430px，**非實機 Safari**。

## 本地測試：通過
- 2000 隨機地圖 seed：出口可達、物件可達、存檔合法、確定重播，失敗各 0。
- 30 層連續推進：每層祝福可選，層 1、4、7、10、13、16、19、22、25、28 額外聖物三選一。
- 守衛樓層傳送門封印；回聲第三次攻擊、雷鏈傷害、吸血/金幣共鳴、荊棘反擊擊殺、火種每層一次重生通過。
- v0.1/v0.2 內容轉換；舊 v0.2 存檔 key 保留；背包、重載後聖物、debug 紀錄正確。
- 249 引擎斷言；320～430px 不產生水平 overflow；JavaScript pageerror 0。

## 限制
- 本測試環境無法直接對本機伺服器或 GitHub Pages 導覽，因此測試使用 `page.set_content` 和 mock localStorage；尚未驗證實際網路載入或 Safari 儲存。
- 高樓層數值溢位、真人遊玩平衡及真實 iPhone 觸控尚未測試。完整測試腳本、截圖與原始專案保存於 `midnight_dungeon_v0.3.zip`。
