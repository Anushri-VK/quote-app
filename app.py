from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself.",
    "Push yourself, because no one else is going to do it for you.",
    "Hard work beats talent when talent doesn't work hard.",
    "Success is not for the lazy."
]

@app.route("/")
def quote():
    return random.choice(quotes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

