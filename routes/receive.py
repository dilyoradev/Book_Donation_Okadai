import os
from flask import Blueprint, render_template, request, current_app, flash
from werkzeug.utils import secure_filename
from models import db, Book
from datetime import datetime
from flask_login import current_user, login_required

receive_bp = Blueprint("receive", __name__)

@receive_bp.route("/receive")
def receive():
    books = Book.query.all()  # later you can add search filtering
    return render_template("receive.html", books=books)
