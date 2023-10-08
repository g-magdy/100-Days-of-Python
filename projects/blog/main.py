from flask import Flask, render_template
from post import Post
import requests
all_posts = []
response = requests.get("https://api.npoint.io/b12e63937b88ab35fa3c")
response.raise_for_status()
all_posts = response.json()
all_posts = [Post(info=p) for p in all_posts]

app = Flask(__name__)

@app.route('/')
def home():
    global all_posts
    return render_template("index.html", all_posts=all_posts)

@app.route('/post/<int:index>')
def get_post(index):
    global all_posts
    if index < len(all_posts):
        return render_template("post.html", post=all_posts[index])
    else:
        return "Invalid: check the index in URL"

if __name__ == "__main__":
    app.run(debug=True)
