from flask import Blueprint

from core.views import feedback, error_403, error_404, error_500


core = Blueprint("core", __name__, template_folder="templates", static_folder="static")
core.add_url_rule("/feedback", "feedback", feedback, methods=["GET", "POST"])
core.register_error_handler(403, error_403)
core.register_error_handler(404, error_404)
core.register_error_handler(500, error_500)
