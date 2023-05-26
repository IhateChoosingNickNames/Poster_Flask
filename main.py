from app import app

from posts.urls import posts
from core.urls import core
from about.urls import about
from users.urls import users


app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(posts)
app.register_blueprint(core)
app.register_blueprint(about, url_prefix="/about")


if __name__ == '__main__':
    app.run(port=8000)