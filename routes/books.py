from flask import Blueprint, render_template

books_bp = Blueprint("books", __name__)

@books_bp.route("/book_details")
def book_details():
    return render_template("book-details.html")