from FlaskApp import db
from flask_user import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication field
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_ad = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # # User fields
    # active = db.Column(db.Boolean()),
    # first_name = db.Column(db.String(50), nullable=False)
    # last_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username