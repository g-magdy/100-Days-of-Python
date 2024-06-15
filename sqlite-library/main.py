from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    def __init__(self, title : str, author : str, rating : float) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.rating = rating


def list_books():
    return db.session.execute(db.select(Book)).scalars().all()

def add_book(title: str, author: str, rating: float):
    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()

@app.route('/')
def home():
    return render_template("index.html", books=list_books())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        add_book(title=request.form["name"],
                 author=request.form["author"],
                 rating=request.form["rating"])
        return redirect("/")
        

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # e=update here
        book_id = request.form.get("id")
        updated_book = db.get_or_404(Book, book_id)
        updated_book.rating = float(request.form.get("new_rating"))
        db.session.commit()
        return redirect("/")
    else:
        book_id = request.args.get("id")
        book_to_edit = db.get_or_404(Book, book_id)
        return render_template("edit.html", book=book_to_edit)
    
@app.route("/delete")
def delete():
    id_to_delete = request.args.get("id")
    book_to_delete = db.get_or_404(Book, id_to_delete)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)

