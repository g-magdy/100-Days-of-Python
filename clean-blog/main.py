from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import dotenv_values


app = Flask(__name__)
response = requests.get("https://api.npoint.io/8ade52c30e2228fbf43e")
response.raise_for_status()
posts_data = response.json()

env = dotenv_values()
email = env["MY_EMAIL"]
pw = env["APP_PASSWORD"]


def send_mail(reciever : dict):
    assert (email is not None) and (pw is not None)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=pw)  
        message = f"Subject:Blog Message from {reciever['name']}\n\n{reciever['message']}\n\nSent from {reciever['email']}\n{reciever['phone']}"
        connection.sendmail(from_addr=email, to_addrs="georgetawfik09@gmail.com", msg=message)
        connection.close()
    

@app.route("/")
def homepage():
    return render_template("index.html", posts_data=posts_data)

@app.route("/home")
def home():
    return render_template("index.html", posts_data=posts_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", sent=False)
    else:
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["phone"])
        print(request.form["message"])
        send_mail(request.form)
        return render_template("contact.html", sent=True)
        

@app.route("/posts/<id>")
def get_post(id):
    pid = int(id) - 1
    if pid >= 0 and pid < len(posts_data):
        post_info = posts_data[pid]
        return render_template("post.html", post=post_info)
    else:
        return "This is an invalid post id"
        

if (__name__ == "__main__"):
    app.run(debug=True, port=4000)