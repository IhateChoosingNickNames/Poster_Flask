from flask import request

from app import app
from models import Post


def paginator(objs):
    page = request.args.get("page")

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    return objs.paginate(page=page, per_page=app.config["PAGINATE_BY"])


def post_filter(posts):
    q = request.args.get("q")
    if q:
        posts = posts.filter(Post.title.contains(q) | Post.text.contains(q))
    return posts