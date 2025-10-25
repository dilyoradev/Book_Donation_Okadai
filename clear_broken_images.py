from app import create_app
from models import db, Book

app = create_app()
app.app_context().push()

# Delete all books
books = Book.query.all()
for book in books:
    db.session.delete(book)
db.session.commit()
