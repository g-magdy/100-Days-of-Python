from flask import Flask, render_template
from random import randint
from datetime import datetime as dt
import requests
import json

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html", rand_num=randint(1, 100), year=dt.today().year)

@app.route("/blog")
def guess():
    url = "https://api.npoint.io/31b63b0c80cbbee50ff3/"
    url2 = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url2)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)
    


if __name__ == "__main__":
    app.run(debug=True)