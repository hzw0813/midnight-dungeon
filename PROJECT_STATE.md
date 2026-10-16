# Midnight Dungeon — PROJECT_STATE

## 最新版
- **v0.5.1 / Impact Visibility Fix**，2026-10-16，Chromium 自動測試通過；iPhone Safari 真機待驗收。
- Repo: https://github.com/hzw0813/midnight-dungeon
- Game: https://hzw0813.github.io/midnight-dungeon/
- 主程式 `index.html` 單檔 HTML5，純 ChatGPT 一般聊天室小步迭代，完成後以 Git 提交並確認 Pages。
- **此版觸發原因：** 使用者在 iPhone 回報「攻擊完全沒看到整個螢幕有閃特效」。實際 v0.5 並沒有全螢幕閃光；普通攻擊只顯示小浮字，暴擊才稍微亮。Reduce Motion 時原程式則直接跳過全部特效。

## v0.5.1 變更
- 所有正常造成敵方傷害的攻擊可觸發 `impact-hit`；地圖周圍短暫綠光、亮邊與命中光圈。暴擊則以更顯眼的金色亮光與傷害字區分。無刺眼的全螢幕白閃。
- `fxTestBtn` 會依序展示普通命中／暴擊效果，用於 iPhone 驗收，不呼叫 `applyAction`，不消耗 RNG/回合/存檔。
- `prefers-reduced-motion` 模式不再直接丟棄傷害提示，而是短暫顯示靜態浮字，定時清除。一般動畫也有 timer fallback。
- 版本 `VERSION='0.5.1'`、新 key `midnight-dungeon-v0.5.1`；優先 `migrateV5` 遷移 v0.5.0，不更改遊戲狀態其餘欄位；保留 v0.4/v0.3/v0.2/v0.1 遷移及舊 key。

## 既有遊戲與保護約束
- 無盡爬塔、戰鬥/XP/升級/金幣/鍛造/祝福、六聖物流派、每五層 Boss、偶數非 Boss 樓層精英及稀有寶箱、魂晶永久天賦，全部沿用。
- 程式保持 seed+actions 確定性重播；本版只動視覺與存檔版本遷移，不改戰鬥或掉寶機率。
- 版本驅動：先測試→原子更新 GitHub→檢查 Pages→手機驗收。先修 BUG，再擴充下一個系統。

## 測試與限制
- Playwright Chromium：原有 1,114 引擎斷言、2000 seeds、30 層、360 組精英掉落、13 項動效純函式斷言；320/375/390/430 手機版面均通過。
- v0.5.1 專項：試播效果、實際普通命中、減少動態效果靜態字、特效清理、試播不寫入存檔、v0.5.0 保存進度遷移通過。
- 真實 iPhone Safari 顯示、網站端儲存、長期性能尚未完成驗收。不要聲稱真機已測試。

## 下一步
1. 讓使用者 iPhone 開啟正式網站，確認是 V0.5.1，點「試播打擊特效」，收集綠光／金光／減少動態效果的體感。
2. 若仍沒有亮光，詢問是否只看見靜態字（Reduce Motion）、有沒有看到 V0.5.1，必要時請截圖。
3. 後續才開始 v0.6 存檔匯出／匯入功能。

下一次聊天：先讀 GitHub 最新 main 的 index.html、PROJECT_STATE.md 和測試紀錄，以本次 v0.5.1 真機回饋為第一優先。
