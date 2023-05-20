import datetime

from flask_sqlalchemy import SQLAlchemy
from settings import app


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    text = db.Column(db.String(500))
    group = db.Column(db.Integer, nullable=True)

app.app_context().push()

def create_db():
    with app.app_context():
        db.create_all()
