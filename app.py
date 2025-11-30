from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='.', static_url_path='')

API_KEY = os.getenv("PERPLEXITY_API_KEY")

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')   # <-- This loads UI

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("msg", "")

        payload = {
            "model": "sonar-small-chat",
            "messages":[{"role":"user","content":user_input}]
        }

        res = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}","Content-Type":"application/json"},
            json=payload
        )

        return jsonify(res.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
