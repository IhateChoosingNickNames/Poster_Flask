from flask import Blueprint

from about.views import tech, author

about = Blueprint("about", __name__, template_folder="templates", static_folder="static")
about.add_url_rule("/author", "author", author)
about.add_url_rule("/tech", "tech", tech)
