from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/b12e63937b88ab35fa3c"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", all_posts=all_posts) 

if __name__ == "__main__":
    app.run()
    