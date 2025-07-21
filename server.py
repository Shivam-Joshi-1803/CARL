from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import config

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend communication

# OpenAI API Key
openai.api_key = config.openai_api_key

# OpenAI GPT Response Function
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful AI assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data["message"]
    response = ask_gpt(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
