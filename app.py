from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

PPLX_API_KEY = os.getenv("PPLX_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"

@app.route("/")
def home():
    return "Perplexity Chatbot is LIVE 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("msg")

    headers = {
        "Authorization": f"Bearer {PPLX_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar-small-chat",
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
