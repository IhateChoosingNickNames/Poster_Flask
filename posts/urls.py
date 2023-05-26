from flask import Blueprint

from posts.views import index, posts_group_list, show_post, post_create


posts = Blueprint("posts", __name__, template_folder="templates", static_folder="static")

posts.add_url_rule("/", "index", index)
posts.add_url_rule("/posts/create", "post_create", post_create, methods=["GET", "POST"])
posts.add_url_rule("/posts/<string:post_slug>", "show_post", show_post)
posts.add_url_rule("/posts", "posts_group_list", index)
posts.add_url_rule("/posts", "index", index)
