from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique = True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship
    books = db.relationship("Book", backref="user", lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    book_author = db.Column(db.String(100), nullable=False)
    faculty = db.Column(db.String(50), nullable=False)
    book_image = db.Column(db.String(200), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # link to a user
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # user = db.Column("User", backref=db.backref("books", lazy=True))


    def __repr__(self):
        return f"<User {self.email}>"

