from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    username = db.Column(db.String(150), primary_key=True)
    email = db.Column(db.String(150), unique=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    password = db.Column(db.String(150))
