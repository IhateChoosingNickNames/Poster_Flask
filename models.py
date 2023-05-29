import datetime
from slugify import slugify
from flask_security.models import fsqla_v3 as fsqla

from app import db


posts_tags = db.Table(
    "posts_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("Posts.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("Tags.id"))
)


class Post(db.Model):
    """Моделька постов."""

    __tablename__ = "Posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    text = db.Column(db.String(500))
    group_id = db.Column(db.Integer, db.ForeignKey("Groups.id"), nullable=True)
    group = db.relationship("Group", foreign_keys="Post.group_id")
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("User", foreign_keys="Post.author_id")
    comment = db.relationship("Comment", back_populates="post")
    slug = db.Column(db.String(50), unique=True)
    tags = db.relationship("Tag", secondary=posts_tags, back_populates="posts", lazy="dynamic")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_slug()

    def set_slug(self):
        self.slug = slugify(self.title)

    def __repr__(self):
        return (f"Post(id={self.id!r}, title={self.title[:15]!r}, "
                f"author={self.author!r})")


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
        self.set_slug()

    def set_slug(self):
        self.slug = slugify(self.title)

    def __repr__(self):
        return f"Group(id={self.id!r}, title={self.title[:15]!r})"


class Comment(db.Model):
    """Моделька комментов."""

    __tablename__ = "Comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    text = db.Column(db.String(500))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("User", foreign_keys="Comment.author_id")
    post_id = db.Column(db.Integer, db.ForeignKey("Posts.id"))
    post = db.relationship("Post", foreign_keys="Comment.post_id")

    def __repr__(self):
        return (f"Comment(id={self.id!r}, text={self.text[:15]!r}, "
                f"author={self.author!r})")


class Tag(db.Model):
    """Моделька комментов."""

    __tablename__ = "Tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    title = db.Column(db.String(500))
    posts = db.relationship('Post', secondary=posts_tags, back_populates='tags')
    slug = db.Column(db.String(50), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_slug()

    def set_slug(self):
        self.slug = slugify(self.title)

    def __repr__(self):
        return f"Tag(id={self.id!r}, title={self.title[:15]!r})"


### Users ###
fsqla.FsModels.set_db_info(db)


class User(db.Model, fsqla.FsUserMixin):
    """Моделька юзеров."""

    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    is_superuser = db.Column(db.Boolean, default=False)
    post = db.relationship("Post", back_populates="author")
    comment = db.relationship("Comment", back_populates="author")
    slug = db.Column(db.String(50), unique=True)
    roles = db.relationship('Role', secondary='roles_users',
                         backref=db.backref('users', lazy='dynamic'))
    active = db.Column(db.Boolean)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_slug()

    def set_slug(self):
        self.slug = slugify(self.username)

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username[:15]!r})"


class Role(db.Model, fsqla.FsRoleMixin):
    """Моделька ролей."""

    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(500))


