from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique = True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship
    books = db.relationship("Book", backref="user", lazy=True)
    requests = db.relationship("BookRequest", backref="requester", lazy=True)
    comments = db.relationship("Comments", backref="user", lazy=True)
    replies = db.relationship("Reply", backref="user", lazy=True)




class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    book_author = db.Column(db.String(100), nullable=False)
    faculty = db.Column(db.String(50), nullable=False)
    book_image = db.Column(db.String(200), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # link to a user
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    # Relationships
    requests = db.relationship("BookRequest", backref="book", lazy=True)
    comments = db.relationship("Comments", backref="book", lazy=True)


class BookRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    requester_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    status = db.Column(db.String(20), default="pending") #pending #accepted #complete
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    #Relationship
    # book = db.relationship("Book", backref="requests", lazy=True)
    # requester = db.relationship("User", backref="requests", lazy=True)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.Text, primary_key=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # user = db.relationship('User', backref='comments')

    # Link comment to a book
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=True)
    # book = db.relationship('Book', backref='comments')

    replies = db.relationship("Reply", backref="comment", lazy=True)

class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reply_content = db.Column(db.Text, primary_key=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to the comments
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)





