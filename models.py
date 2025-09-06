from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique = True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}>"

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def _repr_(self):
        return f"<User {self.email}>"