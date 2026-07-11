from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
CORS(app)
pairs = [
    [
        r"(hi|hello|hey|hai)",
        ["Hello 👋 How can I help you with medical coding?"]
    ],

    [
        r"(what is medical coding|define medical coding)",
        ["Medical coding is the process of converting diagnoses and procedures into standardized codes like ICD-10 and CPT."]
    ],

    [
        r"(what is icd-10|define icd)",
        ["ICD-10 is used to code diagnoses and medical conditions."]
    ],

    [
        r"(what is cpt|define cpt)",
        ["CPT codes are used to describe medical procedures and services."]
    ],

    [
        r"(difference between icd and cpt|icd vs cpt)",
        ["ICD codes describe diagnoses, while CPT codes describe procedures."]
    ],

    [
        r"(what is hcpcs|define hcpcs)",
        ["HCPCS codes are used for medical equipment, supplies, and non-physician services."]
    ],

    [
        r"(what are modifiers|define modifiers)",
        ["Modifiers are two-digit codes added to CPT codes to provide extra details."]
    ],
    [
        r"(who is abishek|about abishek)",
        ["he is captain of black pearl cc "]
    ],

    [
        r"(career in medical coding|medical coding career)",
        ["Medical coding offers roles like Medical Coder, Auditor, and Coding Specialist."]
    ],

    [
        r"(help|what can you do)",
        ["I can answer questions on ICD-10, CPT, HCPCS, modifiers, and medical coding basics."]
    ],

    [
        r"(thank you|thanks)",
        ["You're welcome 😊"]
    ],

    [
        r"(quit|exit|bye)",
        ["Goodbye 👋 Have a great day!"]
    ]
]
chatbot = Chat(pairs, reflections)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "message": "Medical Coding Chatbot Backend (NLTK) is live 🚀"
    })


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message field is required"}), 400

    user_message = data["message"].strip().lower()

    if user_message == "":
        return jsonify({"reply": "Please enter a valid medical coding query."})

    bot_reply = chatbot.respond(user_message)

    if bot_reply is None:
        bot_reply = "I'm sorry 😕 I don't have an answer for that. Try asking about ICD, CPT, or medical coding basics."

    return jsonify({
        "user": user_message,
        "reply": bot_reply
    })
if __name__ == "__main__":
    app.run(debug=True)