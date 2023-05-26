from flask import render_template, request, redirect, url_for, Blueprint

from app import app, db
from core.forms import FeedbackForm

from posts.forms import PostCreateForm
from models import Post, Group, User



def show_profile(user_slug):
    user = User.query.filter_by(id=user_slug).first()
    context = {
        "user": user,
        "object_list": Post.query.filter_by(author_id=user.id)
    }
    return render_template("users/profile.html", **context)


def show_follows():
    return render_template("base.html")

def users_password_change_form():
    return render_template("base.html")

def users_logout():
    return render_template("base.html")

def users_login():
    return render_template("base.html")

def users_signup():
    return render_template("base.html")



