from flask import render_template, Blueprint


core = Blueprint("core", __name__, template_folder="templates", static_folder="static")


@core.app_errorhandler(403)
def error_403(err):
    return render_template("core/403.html")


@core.app_errorhandler(404)
def error_404(err):
    return render_template("core/404.html")


@core.app_errorhandler(500)
def error_500(err):
    return render_template("core/500.html")