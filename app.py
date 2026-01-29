from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API Key (Render se aayegi)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({
        "result": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

