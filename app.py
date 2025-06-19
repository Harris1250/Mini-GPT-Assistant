from flask import Flask, render_template, request

app = Flask(__name__)

# Simple fake GPT logic
def fake_gpt_response(prompt):
    prompt = prompt.lower()
    if "hello" in prompt:
        return "Hey there! How can I help you today?"
    elif "your name" in prompt:
        return "I'm a mini GPT assistant built from scratch!"
    elif "joke" in prompt:
        return "Why did the function cross the road? To return the chicken!"
    else:
        return "Sorry, I don't understand that yet. Try asking something else!"

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    response = ""
    if request.method == "POST":
        user_input = request.form["prompt"]
        response = fake_gpt_response(user_input)
    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)
