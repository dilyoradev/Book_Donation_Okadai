from flask import Blueprint, render_template

receive_bp = Blueprint("receive", __name__)

@receive_bp.route("/receive")
def receive():
    return render_template("receive.html")