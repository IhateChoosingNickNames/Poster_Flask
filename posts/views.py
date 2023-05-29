from flask import render_template, request, redirect, url_for
from flask_login import login_required

from app import app, db
from core.forms import FeedbackForm

from posts.forms import PostCreateForm
from models import Post, Group, User, Tag
from .utils import paginator, post_filter


def index():
    posts = post_filter(Post.query)
    return render_template("posts/index.html", page_obj=paginator(posts))

@login_required
def post_create():
    form = PostCreateForm()
    if form.validate_on_submit():
        title = request.form["title"]
        text = request.form["text"]
        group = Group.query.filter_by(slug=request.form["group"]).first()
        post = Post(title=title, text=text, group_id=group.id, author_id=1)
        for value in request.form.getlist("tags"):
            tag = Tag.query.filter_by(slug=value).first()
            post.tags.append(tag)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("posts.show_post", post_slug=post.slug))
    return render_template("posts/creation.html", form=form)

@login_required
def post_edit(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    if request.method == "POST":
        form = PostCreateForm(formdata=request.form, obj=post)
        # Добавить поддержку заполнения связанных полей, возможно через ModelForm
        # Добавить замену слага при изменении имени
        for elem in form.data:
            print(elem)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for("posts.show_post", post_slug=post.slug))
    form = PostCreateForm(obj=post)
    return render_template("posts/creation.html", form=form)

@login_required
def show_post(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    # Исправить шаблон
    return render_template("posts/show_post.html", post=post)


def group_list():
    return render_template("posts/list_of_groups.html", groups=Group.query.all())


def post_group(group_slug):
    posts = Post.query.join(Group).filter(Group.slug == group_slug)
    posts = post_filter(posts)
    return render_template("posts/index.html", page_obj=paginator(posts))


def post_tag(tag_slug):
    posts = Post.query.join(Tag, Post.tags).filter(Tag.slug == tag_slug)
    posts = post_filter(posts)
    return render_template("posts/index.html", page_obj=paginator(posts))


