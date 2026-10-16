# 深夜地牢 — PROJECT_STATE

## 基準
- 2026-10-16：v0.4.0（精英狩獵），Chromium 手機模擬回歸通過，待 iPhone Safari 實機驗收。
- Repo: https://github.com/hzw0813/midnight-dungeon
- Game: https://hzw0813.github.io/midnight-dungeon/
- 只靠 ChatGPT 聊天室開發，不使用 Codex/Work；以 GitHub main 的單檔 index.html 為主要來源，每版單獨聚焦一項系統，保留 Git 歷史可回退。

## 現有遊戲
- 無限樓層，XP/金幣／鍛造、每層祝福三選一、每三層聖物三選一、每五層 Boss、死亡／撤退後魂晶永久天賦。
- v0.3 六件聖物：echo/greed/blood/storm/thorns/ember。
- v0.4 精英：每個 floor>=2 且偶數、不逢 5 的樓層有一隻 elite。brute 蓄力後重擊（離開可閃）、guard 第一擊減免最多 2、hunter 遠距離能走兩格。HP/傷害強化，擊殺額外獲得 3 XP。
- 精英死亡時一定在所在格掉 `loot.type='cache'`，當下由 seeded RNG 固定獎項。gold 52%（8＋2×樓層金幣＋1 藥水）、soul 30%（永久 2 魂晶＋1 藥水）、relic 18%（額外聖物三選一）。玩家移動至寶箱才能領取；relic 寶箱使用 `status='relic'`、`relicSource='elite'`。
- UI：精英框與屬性提示、寶箱造型、特殊戰鬥訊息。
- 存檔 key：`midnight-dungeon-v0.4`；優先從 v0.3 migrateV3，然後兼容 v0.2/v0.1，不刪舊存檔。seed+actions 可在相同版本確定重播，新版本舊 action 序列不保證相同。

## QA 與限制
- 本地完整回歸 1,114 項引擎斷言，包含 2,000 地圖種子、30 樓層、360 個精英寶箱掉落驗證、三種精英行為、各寶箱效果、存檔遷移；390px 手機 UI/存檔，320/375/390/430 無水平 overflow，無 Chromium JS pageerror。GitHub test_regression.py 為簡短煙霧測試；完整腳本在 ZIP。
- HTTP localhost 模擬導覽在執行環境因管理限制遭封鎖；真實網站 Safari 實測未完成。高樓層數值上限和真人遊戲平衡亦未驗證。
- 不提供付費抽卡、倒數逼迫或每日簽到。

## 下一步
1. 請使用者在 iPhone Safari 驗收到第 2 層：精英提示、可閃重擊、打倒後寶箱、重載存檔。
2. Bug 先修；若順利，v0.5 只加傷害浮字／擊殺與稀有掉落動效，提高戰鬥即時反饋，不一次重寫全部系統。
3. 後續擴充匯出存檔、精英平衡、超深層數值壓力檢查。

## 續作提示
「讀取 GitHub hzw0813/midnight-dungeon 的最新 main 與 PROJECT_STATE.md，先看 v0.4 的 Safari 驗收回饋。照單版單核心功能的流程實作、回歸測試、部署、再驗收。」
