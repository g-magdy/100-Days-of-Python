from flask import Flask
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
        

with app.app_context():
    db.create_all()
        
    # add a book
    new_book = Book("Harry Potter", "J.K. Rowling", 9.3)
    db.session.add(new_book)
    db.session.commit()
    
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()