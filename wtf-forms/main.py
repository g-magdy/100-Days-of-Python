from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, EmailField , PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
import email_validator
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(), Email(granular_message=True)])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8, message="Minimum length = 8 characers")])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "hey there"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()            
    if form.validate_on_submit():
        if form.email.data == "admin@admin.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)
        

if __name__ == '__main__':
    app.run(debug=True)
