# Midnight Dungeon — PROJECT_STATE

> 專案狀態的單一真實來源。開啟新 ChatGPT 聊天時，請同時上傳最新 ZIP，讓助手以此檔與實際程式碼為準繼續開發。

## 版本
- Project: 深夜地牢 / Midnight Dungeon
- Version: v0.1.0
- Date: 2026-10-16 (Asia/Taipei)
- Baseline: `index.html`
- Release state: **候選版本，已通過自動化測試；待使用者 iPhone Safari 驗收**。
- Deployment: 已上傳至 https://github.com/hzw0813/midnight-dungeon 的 `main` 根目錄；GitHub Pages 待啟用並完成網址驗證。

## 目標與原則
1. 僅靠 ChatGPT 聊天室迭代，不使用 Codex / Work。
2. 每回合只做一個主要改善目標，產出新版 ZIP、更新狀態檔與簡短驗收步驟。
3. 永遠保留上一個已由使用者驗收的穩定版本；未驗收的版次標記為 `candidate`。
4. 優先順序：會當機的 Bug → 測試/架構 → 手機操作體驗 → 遊戲平衡 → 新功能。
5. 遊戲核心必須支援 **固定 seed + actions 重播**，否則錯誤難以重現。
6. 不要求使用者必須有電腦。瀏覽器可直接執行單檔 HTML，無外部資源。

## v0.1.0 已完成
- 11×13 地牢地圖；確保角色到傳送門可達。
- 三層關卡，每層會生成障礙、怪物、道具、出口。
- 角色移動、碰撞、近身攻擊、追擊型怪物、受傷死亡、通關。
- 治療藥水、金幣、基本分數。
- iPhone 觸控方向鍵、在地圖上滑動、相鄰格點擊，以及電腦方向鍵/WASD。
- 種子決定的關卡生成與操作序列、回合數與近期事件紀錄。
- 輕量本機儲存（localStorage）；不支援儲存的瀏覽器環境會退化成單次遊玩。
- 重開相同種子／新地圖、測試紀錄複製功能。

## 介面/架構
- `index.html`: 單檔 HTML + CSS + JS；沒有編譯步驟。
- 遊戲核心 `createState(seed)`, `applyAction(state, action)`, `distances(state, x, y)`。
- `window.MidnightDungeonTest`：只為回歸測試暴露固定接口。
- 存檔 key: `midnight-dungeon-v0.1`；版本不相容時不載入舊存檔。
- 動作字串：`up`, `down`, `left`, `right`, `potion`, `wait`。

## 2026-10-16 自動測試結果
- Chromium 390×844 手機視窗，JS 例外：0。
- 1,500 個 seeds 產生合法狀態：全部通過。
- 1,500 個 seeds 地圖出口均可到達、怪物道具均可到達：全部通過。
- 1,500 次同 seed 同指令重播：全部一致。
- 30 次人工到達出口的樓層／通關轉移：通過。
- 10 次死亡、10 次藥水治療、10 次撞牆不耗回合：通過。
- 觸控按鈕、地圖滑動、紀錄面板、重開：通過。
- **未實測**：實體 iPhone Safari、GitHub Pages 上線、手機長時間穩定性和真正真人通關體驗。

## 已知限制
- 沒有正式音效、裝備、技能、Boss、難度選單、完整視障支援。
- 戰鬥僅 1 點基礎傷害，敵人種類單一；數值平衡尚未經真人驗收。
- localStorage 若在聊天內預覽或特殊私密模式不可用，存檔可能無法跨重新載入保存。
- 在 iPhone 的「檔案」App 裡直接預覽 HTML，JavaScript 可能無法正常執行。以 Safari 開啟託管網址驗收較可靠。
- 已建立並寫入 GitHub repository；GitHub Pages 尚待啟用及確認可用，不能假設 Safari 網址目前能開啟。

## 下一步（按優先順序）
1. 收集使用者 iPhone 上對 v0.1.0 的驗收（是否可啟動、是否可操作、是否有 UI 遮擋）。
2. GitHub repo 已建立且為公開。前往 Settings → Pages，使用 Deploy from a branch、`main`、`/(root)` 啟用網站，然後驗證 Safari 可用。
3. 下一版建議：操作回饋（攻擊動畫／玩家受傷提示），先不新增大型系統。

## ChatGPT 新聊天交接指令
「請讀取此 ZIP 內的 index.html、PROJECT_STATE.md 與 test_regression.py。從最新可用版本繼續，只選一項最有價值的改善。先說明改動目標，再實作並執行回歸測試，更新 PROJECT_STATE，產出完整新版 ZIP；不要刪除舊功能，也不要聲稱已在 iPhone Safari 測過。」