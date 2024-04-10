import flask, random

INIT = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH_GIF_SRC = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW_GIF_SRC = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT_GIF_SRC = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
NUMBER = random.randint(0, 9)

app = flask.Flask(__name__)


@app.route('/')
def home():
    return f"<h1>Guess a number from 0 to 9</h1>\
             <h2>Put your guess in the URL</h2> \
             <img src={INIT}>"


@app.route("/<int:n>")
def guessed(n : int):
    if n < NUMBER:
        return f"<h1>Too low</h1>\
            <img src={LOW_GIF_SRC}>"
    elif n > NUMBER:
        return f"<h1>Too high</h1>\
            <img src={HIGH_GIF_SRC}>"
    else:
        return f"<h1>Correct</h1>\
            <img src={CORRECT_GIF_SRC}>"


if __name__ == "__main__":
    app.run(debug=True)
    