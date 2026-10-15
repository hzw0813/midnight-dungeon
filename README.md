# 深夜地牢 v0.1 — Midnight Dungeon

這是一個可以在手機或電腦瀏覽器玩的回合制地牢小遊戲。全部遊戲寫在 `index.html`，沒有任何外部程式庫、廣告、連線要求或帳號需求。

## 如何玩
- **手機**：點選方向鍵移動、或在地圖上滑動。走向怪物就會攻擊。
- **電腦**：方向鍵或 WASD 移動、H 用藥水、空白鍵等待一回合。
- **目標**：走到發光的圓形傳送門，連續通過三層。
- **紀錄**：點「紀錄」可複製種子、操作序列、當前地圖與最近事件。若有問題，把紀錄貼回 ChatGPT。
- **存檔**：支援的網頁瀏覽器會自動將進度儲存到這個網站的 localStorage（不同網址間不共用）。

## 在 iPhone Safari 上玩
最穩定的方式是將 `index.html` 放在 GitHub Pages 等 HTTPS 靜態網站上，再用 Safari 開啟網站。只把 HTML 存在 iPhone「檔案」App，無法保證預覽時執行 JavaScript。

### 首次用 GitHub Pages 部署
1. 在 GitHub 建立一個**公開**的空 repo，例如 `midnight-dungeon`。公開後，程式碼與遊戲可被任何人檢視。
2. 在 repo 根目錄新增或上傳 `index.html`（可連同 PROJECT_STATE.md）。
3. 到 repo 的 **Settings → Pages → Build and deployment**，設定 **Deploy from a branch**，選擇 `main` 和 `/(root)`，再儲存。
4. 等待 Pages 建立網站後，用 GitHub 頁面提供的網址在 Safari 打開。往後只要更新 `index.html`，同一個網址就會取得新版本（更新後可能需要重新整理頁面）。

**發布狀態（2026-10-16）**：v0.1 遊戲程式已上傳到 [hzw0813/midnight-dungeon](https://github.com/hzw0813/midnight-dungeon) 的 `main`。GitHub Pages 仍待在 Settings → Pages 啟用並確認可連線。

## 維護與版本
每次續作，把**完整最新 ZIP**上傳到新聊天室並輸入「繼續優化」。
詳細版本狀態與測試結果見 `PROJECT_STATE.md`。