from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/8ade52c30e2228fbf43e")
response.raise_for_status()
posts_data = response.json()

@app.route("/")
def homepage():
    return render_template("index.html", posts_data=posts_data)

@app.route("/home")
def home():
    return render_template("index.html", posts_data=posts_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/posts/<id>")
def get_post(id):
    pid = int(id) - 1
    if pid >= 0 and pid < len(posts_data):
        post_info = posts_data[pid]
        return render_template("post.html", post=post_info)
    else:
        return "This is an invalid post id"


if (__name__ == "__main__"):
    app.run(debug=True)