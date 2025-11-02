from flask import Blueprint, render_template
from flask_login import login_required


books_bp = Blueprint("books", __name__)

@books_bp.route("/book_details/requests/<int:book_id>", method=["POST"])
@login_required
def book_details():
    return render_template("book-details.html")