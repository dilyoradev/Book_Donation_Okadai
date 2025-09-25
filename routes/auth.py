# Handles Signup and Login
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash
from models import db, Signup

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Grab all form fields
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        faculty = request.form["faculty"]
        email = request.form["email"]
        password = request.form["password"]

        # Hash the password
        password_hash = generate_password_hash(password)

        new_user = Signup (
            first_name=first_name,
            last_name=last_name,
            faculty=faculty,
            email=email,
            password_hash=password_hash
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        except Exception as e:
            return f"There was an issue signing you up: {e}"
    else:
        # Show all users
        users = Signup.query.order_by(Signup.date_joined).all()
        return render_template("/signup.html", users=users)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.from == "POST":
        email = request.form["email"]
        password = request.form["password"]

        #Look up for the user
        user = Signup.query.filter_by(email=email).first()
        if user and check_password
    return render_template("login.html")