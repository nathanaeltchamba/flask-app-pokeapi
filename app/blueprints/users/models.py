from unicodedata import name
import uuid
from datetime import datetime as dt
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(db.Model, UserMixin):
    id = db.Column(db.String(32), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))

    def generate_password(self, password_from_form):
        self.password = generate_password_hash(password_from_form)

    def check_password(self, password_from_form):
        return check_password_hash(self.password, password_from_form)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f'<User: {self.email}>'



class Post(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    author = db.Column(db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f'<Post: {self.body[:30]}...>'

    def to_dict(self):
        return {
            'id': self.id,
            'body': self.body,
            'date_created': self.date_created,
            'author': User.query.get(self.author)
        }

class Pokemon():
    base_url = 'https://pokeapi.co/api/v2/pokemon/'

    # id = self.id
    # poke_name =
    # description = 
    # poke_type = 
    # date_created = db.Column(db.DateTime, default=dt.utcnow)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)