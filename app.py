from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/donate")
def donate():
    return rendeer_template("donate.html")

@app.route("/receive")
def receive():
    return render_template("/receive.html")

@app.route("/login")
def login():
    return render_template("/login.html")

@app.route("/book_details")
def book_details():
    return render_template("/book-details.html")

@app.route("/signup")
def signup():
    return render_template("/signup.html")

if __name__ == "__main__":
    app.run(debug=True)