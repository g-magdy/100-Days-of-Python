from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cofee_choices = [("☕"*i, "☕"*i) for i in range(1, 6, 1)]
    wifi_choices = [("🪐"*i, "🪐"*i) for i in range(1, 6, 1)]
    power_choices = [("🔌"*i, "🔌"*i) for i in range(1, 6, 1)]
    cafe = StringField('Cafe name', validators=[DataRequired()])
    locationURL = URLField('Location URL', validators=[DataRequired(), URL()])
    openTime = TimeField("Open Time", validators=[DataRequired()])
    closeTime = TimeField("Close Time", validators=[DataRequired()])
    coffee_rating = SelectField("coffee rating", validators=[DataRequired()], choices=cofee_choices)
    wifi_rating = SelectField("wifi rating", validators=[DataRequired()], choices=wifi_choices)
    power_rating = SelectField("power rating", validators=[DataRequired()], choices=power_choices)
    submit = SubmitField('Submit', validators=[DataRequired()])

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        print(form.data)
    if form.validate_on_submit():
        with open("./cafe-data.csv", mode="a") as cafe_data:
            writer = csv.writer(cafe_data)
            writer.writerow([v for (k, v) in form.data.items()][:7])
            
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
