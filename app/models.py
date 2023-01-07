from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(128), index=True, unique=True)
