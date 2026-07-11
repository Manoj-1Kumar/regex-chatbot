🤖 Regex-Based Tech Support Chatbot

A simple web-based Tech Support Chatbot built using Python, Flask, NLTK, Regular Expressions (Regex), HTML, CSS, and JavaScript. The chatbot answers predefined technical support questions through a user-friendly web interface.

---

📌 Features

- 💬 Interactive web-based chatbot interface
- 🧠 Regex-based intent matching using NLTK
- ⚡ Flask REST API backend
- 🎨 Responsive frontend using HTML, CSS, and JavaScript
- 🔄 Real-time communication using the Fetch API
- 📝 Handles common greetings, technical queries, recommendations, and basic conversations

---

🛠️ Technologies Used

Backend

- Python
- Flask
- Flask-CORS
- NLTK
- Regular Expressions (Regex)

Frontend

- HTML5
- CSS3
- JavaScript (Fetch API)

---

📂 Project Structure

TechSupportChatbot/
│

├── backend/

│ ├── app.py

│ └── requirements.txt


├── frontend/

│ ├── index.html

│ ├── style.css

│ └── script.js


└── README.md

---

🚀 Installation

1. Clone the Repository

git clone <repository-url>

cd TechSupportChatbot

2. Install Dependencies

pip install -r requirements.txt

or

pip install flask flask-cors nltk

---

▶️ Running the Backend

Navigate to the backend folder and start the Flask server.

cd backend

python app.py

The backend will run at:

http://127.0.0.1:5000

---

🌐 Running the Frontend

Open the "frontend" folder and launch "index.html".

Recommended:

- Open using VS Code Live Server

or simply double-click:

index.html

---

💬 Sample Conversation

You: Hi
Bot: Hello!

You: What is your name?
Bot: My name is Chatbot.

You: Recommend me a movie
Bot: Go watch INTERSTELLAR.

You: What is Python?
Bot: Python is a high-level, general-purpose programming language.

You: Thanks
Bot: You're welcome!

---

⚙️ How It Works

1. The user enters a message in the web interface.
2. JavaScript sends the message to the Flask backend using an HTTP POST request.
3. The backend processes the input using NLTK's "Chat" class and predefined regex patterns.
4. The chatbot selects an appropriate response.
5. The response is returned as JSON and displayed on the webpage.

---

📖 Example Regex Pattern

[
    r"(hi|hello|hey)",
    ["Hello!", "Hi there!", "Hey!"]
]

If the user's input matches the regex pattern, one of the predefined responses is returned.


---

🔮 Future Enhancements

- 🎤 Voice-based interaction
- 🌙 Dark mode UI
- 💾 Chat history using MongoDB
- 🔐 User authentication
- 🤖 AI-powered responses using Large Language Models (LLMs)
- 📱 Mobile-responsive interface

---

🎯 Learning Outcomes

This project demonstrates:

- Regular Expressions (Regex)
- Rule-based chatbot development
- REST API development with Flask
- Frontend and backend integration
- JSON data exchange
- JavaScript Fetch API
- Cross-Origin Resource Sharing (CORS)

---

👨‍💻 Author

Manojkumar P

B.Tech Information Technology

---

📄 License

This project is developed for educational and learning purposes. Feel free to modify and extend it for your own projects.
