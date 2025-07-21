from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

def ask_llama2(prompt):
    """Interact with Llama 2 via Ollama CLI."""
    result = subprocess.run(["ollama", "run", "llama2", prompt], capture_output=True, text=True)
    return result.stdout.strip()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")

    ai_response = ask_llama2(user_message)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
