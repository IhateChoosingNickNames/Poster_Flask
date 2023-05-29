from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from .mixins import LoginMixin

class BaseModelView(ModelView):


    def on_model_change(self, form, model, is_created):
        model.set_slug()
        return super().on_model_change(form, model, is_created)


class AdminView(LoginMixin, BaseModelView):
    pass

class IndexAdminView(LoginMixin, AdminIndexView):
    pass


class PostAdminView(AdminView, BaseModelView):
    can_create = False
    form_columns = ("title", "text", "group", "tags")


class GroupAdminView(AdminView, BaseModelView):
    form_columns = ("title", "description")


class CommentAdminView(AdminView, BaseModelView):
    can_create = False
    form_columns = ("text",)


class TagAdminView(AdminView, BaseModelView):
    form_columns = ("title",)


class UserAdminView(AdminView, BaseModelView):
    can_create = False
    form_columns = ("username", "first_name", "last_name", "email", "roles")