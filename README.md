# OgChemicalDraw

## 簡介
一個簡單的 Flask 應用程式，使用 Google Generative AI (Gemini) 生成回覆，前端使用 RDKit.js 將 SMILES 或反應式渲染為化學結構圖。

## 功能
- 一般模式：輸入問題，AI 以簡短專業語氣回覆文字。
- SMILES 模式：輸入 `/smiles XXX`，AI 只回傳一行 SMILES，前端自動繪圖而不顯示文字。
- 反應式模式：若 AI 回傳反應 SMILES (如 `C.OO>>O=C=O`)，前端可渲染反應圖。

## 檔案結構
- `app.py`：Flask 伺服器，處理 API 請求並呼叫 Gemini 模型。
- `templates/chat.html`：前端介面，包含聊天室與 RDKit.js 繪圖邏輯。

## 使用方式
1. 安裝需求：
   ```bash
   pip install flask python-dotenv google-generativeai


2. 在專案根目錄建立 `.env`，設定：

   ```
   API=你的_Gemini_API_Key
   ```
3. 啟動伺服器：

   ```bash
   python app.py
   ```
4. 開啟瀏覽器訪問 `http://127.0.0.1:5000`。
