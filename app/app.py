from flask import Flask, render_template, flash, redirect, url_for
from models import db, User, Book, BookRequest
from config import Config
from flask_login import LoginManager
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.permanent_session_lifetime = timedelta(days=5)

    db.init_app(app)

    # Flask-Login setup
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @login_manager.unauthorized_handler
    def unauthorized():
        flash("You are not logged in!", "warning")
        return redirect(url_for("auth.login"))

    # Register blueprints
    from routes.auth import auth_bp
    from routes.donate import donate_bp
    from routes.receive import receive_bp
    from routes.books import books_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(donate_bp)
    app.register_blueprint(receive_bp)
    app.register_blueprint(books_bp)


    @app.route("/")
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)