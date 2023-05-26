from flask import render_template, request, redirect, url_for

from app import app, db
from core.forms import FeedbackForm

from posts.forms import PostCreateForm
from models import Post, Group, User


def index():
    return render_template("posts/index.html", posts=Post.query.all())


def post_create():
    form = PostCreateForm()
    if form.validate_on_submit():
        title = request.form["title"]
        text = request.form["text"]
        group = Group.query.filter_by(slug=request.form["group"]).first()
        post = Post(title=title, text=text, group_id=group.id, author_id=1)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("posts.show_post", post_slug=post.slug))
    return render_template("posts/creation.html", form=form)


def show_post(post_slug):
    post = Post.query.filter_by(slug=post_slug)
    return render_template("posts/index.html", posts=post)


def posts_group_list():
    return render_template("base.html")


