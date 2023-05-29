from flask import Blueprint

from posts.views import index, show_post, post_create, post_tag, post_group, group_list, post_edit

posts = Blueprint("posts", __name__, template_folder="templates", static_folder="static")

posts.add_url_rule("/", "index", index)
posts.add_url_rule("/posts/create", "post_create", post_create, methods=["GET", "POST"])
posts.add_url_rule("/posts/<string:post_slug>/edit", "post_edit", post_edit, methods=["GET", "POST"])
posts.add_url_rule("/posts/<string:post_slug>", "show_post", show_post)
posts.add_url_rule("/posts/tag/<string:tag_slug>", "post_tag", post_tag)
posts.add_url_rule("/posts/group/<string:group_slug>", "post_group", post_group)
posts.add_url_rule("/posts/group_list", "group_list", group_list)
