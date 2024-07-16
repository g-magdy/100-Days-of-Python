from flask import Flask, render_template, redirect, url_for, request
# from flask_wtf import FlaskForm
# from flask_wtf.form import _Auto
# from wtforms import StringField, EmailField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Length, Email
# import email_validator
# from flask_bootstrap import Bootstrap5

from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

class EditForm(FlaskForm):
    rating = FloatField(label="Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)
# CREATE TABLE

#! Mapped[int] is important

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year : Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

def getAllMovies():
    return db.session.execute(db.select(Movie)).scalars().all()

@app.route("/")
def home():
    return render_template("index.html", movies=getAllMovies())

@app.route("/edit", methods=["GET", "POST"])
def editRating():
    form : FlaskForm = EditForm()
    target = request.args.get("id")
    req_movie = db.get_or_404(Movie, target)
    if form.validate_on_submit():
        r = float(form.rating.data)
        req_movie.rating = r if r <=10 else 10
        req_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template("edit.html", form = EditForm(), movie=req_movie)
    
        


if __name__ == '__main__':
    app.run(debug=True)
