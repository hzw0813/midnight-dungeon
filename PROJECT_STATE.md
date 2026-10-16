# Midnight Dungeon — PROJECT_STATE

## 最新版本與位置
- **v0.5.0 / Impact Edition**（2026-10-16），已完成 Chromium 本地回歸；尚需使用者實體 iPhone Safari 驗收。
- Repository: https://github.com/hzw0813/midnight-dungeon
- Game: https://hzw0813.github.io/midnight-dungeon/
- Single-file source: `main/index.html`。每次使用 ChatGPT 普通聊天室小步迭代，不用 Codex 或 Work。提交前須測試，使用 Git commit 可回退。

## 當前玩法（v0.1～v0.4）
- 無盡地牢、seed + actions 決定性重播、XP / 升級 / 金幣 / 鍛造 / 藥水。
- 每層祝福三選一；第 1、4、7、10… 層聖物三選一。六個聖物：echo、greed、blood、storm、thorns、ember。每五層 Boss 封印出口。
- 偶數且非 Boss 樓層有精英 brute / guard / hunter。精英必掉寶箱，類型 gold 52% / soul 30% / relic 18%。
- 退回營地或死亡後能把魂晶用於永久 talents（might、life、wealth）。

## v0.5 新增（純視覺）
- 新增 `#fxLayer` DOM 動效層，`pointer-events:none`、`aria-hidden=true`，不影響 Canvas 點擊或滑動。
- `beforeVisual(s)`、`visualEvents(before,after,cmd)` 只讀遊戲狀態，不消耗 RNG、不存入本機資料，`useAction()` 在每輪 UI 操作後產生暫時顯示。
- 傷害、暴擊、擊殺、精英、Boss、金幣、魂晶、回血、受傷、升級、開箱、聖物與過層回饋；短暫閃光、modal 進場動畫及傳說聖物掃光。
- 動效會自動移除、最多 40 DOM 節點；尊重 `prefers-reduced-motion`。未變動戰鬥引擎數值。
- 存檔使用 `midnight-dungeon-v0.5`，優先從 v0.4 遷移，然後支援 v0.3、v0.2、v0.1；保留所有舊 key。

## QA 與限制
- 本地 Chromium：2,000 seeds、1,114 引擎斷言、30 層、360 精英掉落案例、13 項純動效斷言、手機 DOM／動畫清理／舊存檔升級；320、375、390、430 寬度無水平 overflow；JS page errors 0。
- 真實 iPhone Safari、長期儲存政策、極深層數值上限與實際動效流暢度尚未驗收。網站 Pages 部署狀態須以 GitHub Actions 為準。

## 下一輪
1. 先收集 Safari 操作／動畫流暢度／存檔回饋；若出現 Bug 先修。
2. v0.6 建議做「存檔匯入匯出」或「成就圖鑑與長期目標」，一次只做一個主要系統。
3. 續作請先讀取此 repo 的最新 main 與 PROJECT_STATE，保留 deterministic replay、舊版存檔及手機操作，完成回歸測試後再部署。
