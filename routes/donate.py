import os
from flask import Blueprint, render_template, request, current_app, flash
from werkzeug.utils import secure_filename
from models import db, Book
from datetime import datetime
from flask_login import current_user, login_required


donate_bp = Blueprint("donate", __name__)

@donate_bp.route("/donate/", methods=["GET", "POST"])
def donate():
    if request.method == "POST":
        book_name = request.form["book_name"]
        book_author = request.form["book_author"]
        faculty = request.form["faculty"]
        book_image = request.files["book_image"]
    
        if book_image:
            # Make file safe and store it
            filename = secure_filename(book_image.filename)
            image_path = os.path.join("static/uploads", filename)
            book_image.save(os.path.join(current_app.root_path, image_path))
        else:
            image_path = None

        # Save to database
        new_book = Book(
            book_name = book_name,
            book_author = book_author,
            faculty = faculty,
            book_image = image_path,
            date_added = datetime.now(),
            # user_id = current_user.id
            )

        db.session.add(new_book)
        db.session.commit()

        flash(f"{book_name} Book Donated Successfully!", "success")
    
    return render_template("donate.html")


