async function sendMessage() {
    const inputBox = document.getElementById("user-input");
    const message = inputBox.value.trim();

    if (message === "") return;

    addMessage("You", message, "user");
    inputBox.value = "";

    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });
        if(!response.ok) {
            throw new Error("http error " + response.status);
        }

        const data = await response.json();
        addMessage("Bot", data.reply, "bot");

    } catch (error) {
        console.error("Error:", error);
        addMessage("Bot", "Server not reachable 😢", "bot");
    }
}

function addMessage(sender, text, className) {
    const chatBox = document.getElementById("chat-box");
    const msgDiv = document.createElement("div");

    msgDiv.classList.add("message", className);
    msgDiv.innerText = sender + ": " + text;

    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
