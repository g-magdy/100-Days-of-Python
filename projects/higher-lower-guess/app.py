from flask import Flask, render_template, request, redirect
from random import randint

app = Flask(__name__)
magic = randint(0, 9)

@app.route("/", methods=['GET', 'POST'])
def hello():
    global magic
    if request.method == 'GET':
        return render_template("index.html")
    else:
        answer = request.form.get("guessed")
        assert answer is not None
        answer = int(answer)
        if answer == magic:
            return render_template("correct.html")
        elif answer < magic:
            return render_template("too-low.html")
        elif answer > magic:
            return render_template("too-high.html")
        else:
            return "INVALID"

@app.route("/change")
def reset():
    global magic
    magic = randint(0, 9)
    return redirect("/")

if __name__ == "__main__":
    app.run()
    
