# 深夜地牢 — PROJECT_STATE

## 最新版
- 版本：v0.2.0 (candidate)，2026-10-16，尚待 iPhone Safari 真機驗收。
- Repo: https://github.com/hzw0813/midnight-dungeon
- 遊戲: https://hzw0813.github.io/midnight-dungeon/
- 主程式：`index.html` 單檔 HTML5；保留 Git 提交紀錄可回退到 v0.1。
- 目標：只用 ChatGPT 聊天室逐版迭代。每次聚焦一個主要提升，產出 ZIP、測試、更新狀態、推送 Pages，再由使用者驗收。

## 方向：令人滿足但不具掠奪性的成長
短循環（擊殺→ XP → 升級、金幣與鍛造）、中循環（通過每層三選一 Build、每五層守衛）、長循環（死亡/撤退後用魂晶買永久天賦，超越最高樓層）。沒有強迫每日登入、付費抽卡、限時等待。

## v0.2.0 機制
- 地牢不再有三層終點。樓層越高怪物 HP、傷害越高，敵人數量至多 7。第 5/10/15... 層守衛存活時封印傳送門。
- 英雄有 `level`、`xp`：升級 +2 maxHP / 恢復少量 HP，每兩級提高基礎攻擊。打怪有 XP 與金幣。
- 每層突破得魂晶 1，Boss 層額外 +4；進入 `choosing` 狀態，3 選 1 本輪祝福：`blade/heart/vamp/fortune/potion/crit`。
- 戰鬥商店：`shop:attack` 花 `12 + 8×本輪已有鍛造次數` 金幣、`shop:potion` 花 8 金幣。
- 回營地或死亡時，剩餘金幣每 15 枚轉成 1 魂晶，`coinSettled` 防止重複結算。
- 永久天賦 `might/life/wealth` 增加下一輪攻擊+1、初始 HP+3、擊殺金幣+1。費用按天賦等級線性增加。
- 新存檔 key `midnight-dungeon-v0.2`。首次使用會嘗試轉換有效舊 `midnight-dungeon-v0.1` 存檔，保留原始 key。
- `createState(seed,meta?)` 和 `applyAction(state,command)` 保證同一初始狀態 + 指令序列可確定重播。指令包含 `blessing:<id>`、`shop:attack|shop:potion`、`retire`、`talent:<key>`。

## 2026-10-16 品質
- 2,000 組種子驗證地圖、怪物、道具可達；合法存檔和重播；差異數 0。
- 16 層樓層轉換和 3 選 1、Boss 5/10/15 樓層封印、XP 升級、永久天賦、鍛造、金幣單次結算、舊存檔轉換通過。
- Chromium 390×844 手機觸控、滑動、商店、祝福、營地與模擬存檔恢復通過；未捕捉到 JavaScript 例外。
- 真機 Safari 及真人平衡未驗收，不能宣稱已穩定或在極高樓層實測。

## 下一步
1. 收集 iPhone Safari 對 v0.2 的驗收：UI、觸控、頁面重新載入後進度、祝福與永久天賦、Boss 體感。
2. 有 Bug 先修；若無，建議 v0.3 只加入「稀有聖物 / 流派連攜」，別一次大改全部遊戲。
3. 後續再加傷害浮字、精英怪差異、升級特效、可攜式存檔匯入匯出、平衡曲線。
4. 每次修改須先 fetch_file 取得目前 blob SHA，修改後 update_file，再看 GitHub Pages Actions 結果。不要誤改不相關 repo。

## 下一次聊天交接
「讀取 hzw0813/midnight-dungeon 最新 main 的 index.html、PROJECT_STATE.md 及 test_regression.py。沿用版本驅動迭代流程，保留 seed+actions 可重播與手機支援。v0.2 是候選版，先考慮實機回饋。」
