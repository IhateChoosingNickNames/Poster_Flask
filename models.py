import datetime

from slugify import slugify

from app import db



class Post(db.Model):
    """Моделька постов."""

    __tablename__ = "Posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    text = db.Column(db.String(500))
    group_id = db.Column(db.Integer, db.ForeignKey("Groups.id"), nullable=True)
    group = db.relationship("Group", foreign_keys="Post.group_id")
    author_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    author = db.relationship("User", foreign_keys="Post.author_id")
    comment = db.relationship("Comment", back_populates="post")
    slug = db.Column(db.String(50), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.title)

    def __repr__(self):
        return (f"Post(id={self.id!r}, title={self.title[:15]!r}, "
                f"author={self.author!r})")

class User(db.Model):
    """Моделька юзеров."""

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    post = db.relationship("Post", back_populates="author")
    comment = db.relationship("Comment", back_populates="author")
    slug = db.Column(db.String(50), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.title)

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username[:15]!r})"


class Group(db.Model):
    """Моделька групп."""

    __tablename__ = "Groups"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    slug = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(500))
    post = db.relationship("Post", back_populates="group")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.title)

    def __repr__(self):
        return f"Group(id={self.id!r}, title={self.title[:15]!r})"


class Comment(db.Model):
    """Моделька комментов."""

    __tablename__ = "Comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    text = db.Column(db.String(500))
    author_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    author = db.relationship("User", foreign_keys="Comment.author_id")
    post_id = db.Column(db.Integer, db.ForeignKey("Posts.id"))
    post = db.relationship("Post", foreign_keys="Comment.post_id")

    def __repr__(self):
        return (f"Comment(id={self.id!r}, text={self.text[:15]!r}, "
                f"author={self.author!r})")


