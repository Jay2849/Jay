from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # ✅ Enable CORS to allow frontend requests

# 🔑 Configure Gemini API Key (Replace with your actual API key)
GENAI_API_KEY = "AIzaSyCfrLUoxf1rOPn9pYXwMOhIVEvqBnkHloU"
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    """ Serve the frontend UI """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """ Handle chat requests from frontend """
    data = request.json  # Get JSON data from request
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No input provided"}), 400  # Handle empty input

    try:
        # 🔥 Send input to Gemini API
        response = model.generate_content(user_input)

        # ✅ Check if response has valid text
        bot_reply = response.text if hasattr(response, 'text') else "Sorry, I couldn't understand."

        return jsonify({"response": bot_reply})  # Send response to frontend

    except Exception as e:
        print(f"Error: {e}")  # Log error for debugging
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)  # Run Flask app in debug mode
