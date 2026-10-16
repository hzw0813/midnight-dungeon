# 深夜地牢 — PROJECT_STATE

## 基準版本
- Version: **v0.3.0 / 聖物覺醒**，2026-10-16。Chromium 自動測試通過，**iPhone Safari 尚待真機驗收**。
- Repository: https://github.com/hzw0813/midnight-dungeon
- Game: https://hzw0813.github.io/midnight-dungeon/
- Entry: `main/index.html`（單檔 HTML+CSS+JS）；版控可回退。開發流程純 ChatGPT 聊天室，不用 Codex、Work。

## 長期遊戲方向
核心為無盡爬塔、短期 XP 金幣與升級、中期流派搭配與聖物、長期魂晶永久天賦。每版聚焦一個系統、可測試/可回退，不使用強迫每日簽到、計時付費獎勵或付費抽卡。

## v0.3 機制
- 新增 `relics` 六項非負整數：`echo`（每三攻追擊）、`greed`（金幣＋貪婪連攜回血）、`blood`（回血＋吸血連攜）、`storm`（暴擊雷鏈＋暴擊祝福連攜）、`thorns`（受擊反傷）、`ember`（每層一次瀕死重生）。
- 物品稀有度 common / rare / legendary（權重 6 / 3 / 1），抽取不重複的三件。通關層數 1,4,7,10... 有聖物選擇；先祝福 `choosing` 後聖物 `relic`。
- 新狀態 `pendingRelics`、`attackCount`、`emberUsedFloor`，可用 `relic:<id>` 選擇；未完成選擇不能繼續普通操作。
- 畫面增加 `#relicBtn` 背包、稀有度高亮卡片與特殊觸發提示。重複取得相同聖物可升級。
- v0.3 存檔 key `midnight-dungeon-v0.3`。`migrateV2` 優先遷移 v0.2，否則嘗試 v0.1；原本 key 不刪除，保留回退可能。

## 自動品質
- 2000 seeded maps + replay/存檔驗證、30 層（10 次聖物機會）、Boss 出口封印、六聖物實際效果、遷移、手機觸控選擇及本機存檔模擬；完整本地回歸 249 項引擎斷言均通過。
- 320/375/390/430px 手機模擬無水平 overflow，JS pageerror 0。*非* iPhone Safari 實機，也非線上站點瀏覽器測試。

## 下一步
1. 收集實際 iPhone Safari 的遊玩、觸控、存檔及聖物選擇回饋。若有 Bug 優先修復。
2. v0.4 建議聚焦「精英怪＋不同掉落」或「傷害浮字／擊殺回饋」，勿一次堆積很多系統。
3. 之後再做完整存檔匯出/匯入、難度曲線與極深樓層壓力測試。JS 安全整數限制意味無盡並不等於數學上的無限。

### 下一次 ChatGPT 聊天提示
「讀取 hzw0813/midnight-dungeon 最新 main 的 index.html、PROJECT_STATE.md、TEST_REPORT.md 與 test_regression.py；沿用小步測試→更新→部署→手機驗收的流程，勿用 Codex/Work。v0.3 有六種聖物和祝福連攜、舊版存檔遷移；先等 Safari 實機回饋。」
