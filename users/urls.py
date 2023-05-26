from flask import Blueprint

from users.views import show_profile, users_signup, users_login, users_logout, users_password_change_form, show_follows


users = Blueprint("users", __name__, template_folder="templates", static_folder="static")
users.add_url_rule("/<int:user_slug>/profile", "show_profile", show_profile)
users.add_url_rule("/", "show_follows", show_follows)
users.add_url_rule("/", "users_password_change_form", users_password_change_form)
users.add_url_rule("/", "users_logout", users_logout)
users.add_url_rule("/", "users_login", users_login)
users.add_url_rule("/", "users_signup", users_signup)
