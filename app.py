from flask import Flask, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from admin.admin import AdminView, IndexAdminView, PostAdminView, \
    UserAdminView, TagAdminView, GroupAdminView, CommentAdminView
from config import Configuration
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security

# add create_app
app = Flask(__name__)
app.config.from_object(Configuration)

# Constaint names
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

# db creation
db = SQLAlchemy(app, metadata=metadata)

# # ???
app.app_context().push()


import models
migrate = Migrate(app, db)


### Admin
admin = Admin(app, "Yatube Flask", url="/", index_view=IndexAdminView(name="Home"))
admin.add_view(PostAdminView(models.Post, db.session))
admin.add_view(UserAdminView(models.User, db.session))
admin.add_view(TagAdminView(models.Tag, db.session))
admin.add_view(GroupAdminView(models.Group, db.session))
admin.add_view(CommentAdminView(models.Comment, db.session))


### Authentication

user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
app.security = Security(app, user_datastore)


