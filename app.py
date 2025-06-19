from flask import Flask, render_template, request

app = Flask(__name__)

def generate_response(prompt):
    prompt = prompt.lower().strip()

    responses = {
        "hello": "Hey! How can I assist you today?",
        "hi": "Hello! Ask me anything.",
        "how are you": "I'm just code, but I'm running smoothly 😎",
        "your name": "I'm Mini GPT — built from scratch, no APIs.",
        "joke": "Why don't programmers like nature? Too many bugs.",
        "bye": "See you later! Stay curious.",
        "help": "Try asking me about myself, tell you a joke, or just say hi."
    }

    for key in responses:
        if key in prompt:
            return responses[key]

    return "Hmm... I’m not sure how to answer that yet. Try something else!"

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    response = ""
    if request.method == "POST":
        user_input = request.form["prompt"]
        response = generate_response(user_input)
    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)
