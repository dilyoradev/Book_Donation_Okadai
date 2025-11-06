from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user, login_user

from models import db, Book, BookRequest


books_bp = Blueprint("books", __name__)

@books_bp.route("/book_details/<int:book_id>")
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("book-details.html", book=book)


@books_bp.route("/book_details/request/<int:book_id>", methods=["POST"])
@login_required
def request_book(book_id):
    book = Book.query.get_or_404(book_id)
    
    #Prevent from requesting own book
    if book.user_id == current_user.id:
        flash("You can not request your own book.", "warning")
        return redirect(url_for('books.book_details', book_id=book.id))

    #Prevent duplicate requests
    existing_request = BookRequest.query.filter_by(book_id=book.id, requester_id=current_user.id).first()
    if existing_request:
        flash("You have already requested this book!", "info")
        return redirect(url_for('books.my_requests', book_id=book.id))

    
    #Create a new request
    new_request = BookRequest(book_id=book.id, requester_id=current_user.id)
    db.session.add(new_request)
    db.session.commit()
    flash("Book request sent successfully!", "success")
    return redirect(url_for('books.book_details', book_id=book.id))


@books_bp.route("/my_requests")
def my_requests():
    user_requests = BookRequest.query.filter_by(requester_id=current_user.id).all()
    return render_template("my-requests.html", requests=user_requests)

@books_bp.route("/my_donations")
@login_required
def my_donations():
    user_donations = Book.query.filter_by(user_id=current_user.id).order_by(Book.id.desc()).all()
    return render_template("my-donations.html", donations=user_donations)