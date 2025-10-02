from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("API"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

app = Flask(__name__)

def get_bot_response(user_input: str) -> str:
    user_input = (user_input or "").strip()

    # 若以 /smiles 開頭 => 僅回 SMILES，沒有廢話
    if user_input.lower().startswith("/smiles "):
        topic = user_input[8:].strip()
        prompt = (
            "你是一個化學 SMILES 產生器。"
            "只輸出一行有效 SMILES，不要加任何說明、標點或前綴。"
            "例如苯請直接輸出 c1ccccc1。\n"
            f"題目：{topic}"
        )
    else:
        # 一般模式
        prompt = f"請用簡短且專業的態度，討論 {user_input}。"

    try:
        resp = model.generate_content(prompt)
        text = getattr(resp, "text", str(resp)).strip()
        if text.startswith("```"):
            text = text.strip("`").split("\n", 1)[-1].strip()
            if text.endswith("```"):
                text = text.rsplit("```", 1)[0].strip()
        return text
    except Exception as e:
        return f"Error generating response: {e}"

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
