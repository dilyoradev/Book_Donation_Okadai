from flask import Flask, render_template
from models import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

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