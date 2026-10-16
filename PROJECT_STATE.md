# 深夜地牢 — PROJECT_STATE

## 最新版
- 版本：**v0.5.2 Clear Combat**，2026-10-16，Chromium 回歸通過，等待實體 iPhone Safari 驗收。
- GitHub：https://github.com/hzw0813/midnight-dungeon
- 遊戲：https://hzw0813.github.io/midnight-dungeon/
- 標準 ChatGPT 聊天室長期開發，不用 Codex / Work；以 GitHub main 的單檔 \`index.html\` 為準；每輪完成自動測試、單次提交、Pages 部署、手機驗收。

## 使用者回饋
使用者指出「懸浮文字會擋住角色跟怪物」。v0.5.1 的 \`emitEffects()\` 把文字放在地圖上的 \`#fxLayer\`，傷害、擊殺、金幣會同回合疊加遮住單位及血條。

## v0.5.2 改動
- 新增地圖外 \`#combatFeed\`；所有 \`fx-float\` 文字**只**顯示於此。
- \`#fxLayer\` 僅保留命中時透明中心的光圈，不再放置文字。地圖綠光／金光仍保留。
- 戰鬥訊息最多 3 個 chip（小於 360px 時 2 個），約 1.5 秒自動清理；支援減少動態效果時的靜態提示，沒有水平溢出。
- 試播打擊特效不呼叫 \`applyAction()\`，不修改存檔、亂數或回合。
- \`VERSION='0.5.2'\`、\`SAVE_KEY='midnight-dungeon-v0.5.2'\`。新增 \`migrateV51\`；從有效 v0.5.1 進度轉換後保留舊 key。v0.5 至 v0.1 遷移也保留。
- **未修改**遊戲核心規則、敵人 AI、傷害、道具掉落機率及 seed+actions 的確定性。

## 既有系統
無盡樓層、XP 升級、鍛造、每層祝福三選一、六種聖物和共鳴、每五層 Boss、精英與稀有寶箱、魂晶永久天賦。

## 品質
- 2,000 種子，1,114 引擎斷言，30 層成長、360 精英掉落、13 純 FX 斷言 PASS。
- 320/375/390/430px，正常／減少動態效果，文字全部在地圖下方；實際精英暴擊擊殺＋金幣回饋時也無遮擋；0 橫向溢出。
- v0.5.1 → v0.5.2 保留樓層、HP、等級、金幣、魂晶、聖物、永久天賦；舊存檔 key 保留。
- Chromium 頭部模擬測試，**尚未實測 iPhone Safari 或極深樓層**。

## 下一輪
1. 優先請使用者在 Safari 看 V0.5.2，試播及實際攻擊，確認下方戰鬥列不遮擋。
2. 有 Bug 先修。若順利，可規劃 v0.6 存檔匯入／匯出；不要一次引入多個新系統。

## 新對話交接
「讀取 hzw0813/midnight-dungeon 最新 main 的 PROJECT_STATE、index.html 和測試，先處理 v0.5.2 的 Safari 驗收；維持小步修改、回歸測試及 GitHub Pages 部署。」
