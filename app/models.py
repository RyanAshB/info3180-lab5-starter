# Add any model classes for Flask-SQLAlchemy here
from . import db
from app import db
from datetime import datetime

class movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

    def __repr__(self):
        return '<Movie {}>'.format(self.title)