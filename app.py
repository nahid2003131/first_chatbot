from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

chat_history = []  # Stores all chat messages

responses = {
    "hello": "Hey Boss! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a great day!",
}

@app.route("/")
def home():
    return render_template("index.html")  # Renders the UI

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip().lower()
    
    bot_response = responses.get(user_message, "I'm not sure how to respond to that.")
    
    # Store chat messages
    chat_history.append({"user": user_message, "bot": bot_response})

    return jsonify({"response": bot_response, "history": chat_history})

@app.route("/history", methods=["GET"])
def get_history():
    return jsonify({"history": chat_history})

if __name__ == "__main__":
    app.run(debug=True)
