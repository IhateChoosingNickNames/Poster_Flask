from flask import redirect, url_for, request
from flask_login import current_user


class LoginMixin:
    def is_accessible(self):
        return current_user.has_role("admin") or hasattr(current_user, "is_superuser") and current_user.is_superuser

    def inaccessible_callback(self, name, **kwargs):
        # TODO сделать редирект после логина
        return redirect(url_for("security.login", next=request.endpoint))