# Handles Signup and Login
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

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

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already exists. Please log in instead!", "warning")
            return redirect(url_for("auth.login"))


        # Hash the password
        password_hash = generate_password_hash(password)

        new_user = User (
            first_name=first_name,
            last_name=last_name,
            faculty=faculty,
            email=email,
            password_hash=password_hash
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully. Please log in.", "success")
            return redirect(url_for("auth.login"))
        except Exception as e:
            db.session.rollback()
            flash(f"There was an issue in signing you up: {e}", "danger")
            return redirect(url_for("auth.signup"))
    else:
        # Show all users
        users = User.query.order_by(User.date_joined).all()
        return render_template("/signup.html", users=users)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        email = request.form["email"]
        password = request.form["password"]

        # Look up for the user
        user = User.query.filter_by(email=email).first()
        
        if not user:
            flash("No account found with that email.", "danger")
            return redirect(url_for("auth.login"))

        # If found → check password
        if not check_password_hash(user.password_hash, password):
            flash("Incorrect password. Please try again.", "danger")
            return redirect(url_for("auth.login"))

        # If correct → log them in
        login_user(user, remember=True)
        session["user"] = user.id

        flash(f"Welcome back, {user.first_name}!", "success")

        # Redirect to dashboard or home
        next_page = request.args.get("next")
        return redirect(next_page or url_for("index"))  # or homepage
    else:
        if "user" in session:
            return redirect(url_for("auth.user_page"))

        return render_template("login.html")

@auth_bp.route("/user")
@login_required
def user_page():
    return f"<h1>{current_user.first_name}</h1>"

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("auth.login"))
