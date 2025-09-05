from flask import Blueprint, render_template

donate_bp = Blueprint("donate", __name__)

@donate_bp.route("/donate")
def donate():
    return render_template("donate.html")