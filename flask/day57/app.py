from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    year =datetime.datetime.today().year
    return render_template("index.html", year=year)

@app.route('/guess/<string:person>')
def guess(person:str):
    response = requests.get(url=f"https://api.genderize.io/?name={person}")
    response.raise_for_status()
    gender = response.json()['gender']
    response = requests.get(f"https://api.agify.io?name={person}")
    response.raise_for_status()
    age = response.json()['age']
    return render_template("guess.html", friend=person.capitalize(), gender=gender, age = age)

if __name__ == "__main__":
    app.run(debug=True)
    