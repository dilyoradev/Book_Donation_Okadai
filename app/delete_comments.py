from app import db
from yourapp.models import Comment

# Drop and recreate the Comment table
Comment.__table__.drop(db.engine)
Comment.__table__.create(db.engine)
