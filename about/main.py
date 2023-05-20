from flask import Blueprint, render_template

about = Blueprint("about", __name__, template_folder="templates", static_folder="static")


@about.route("/author")
def author():
    return render_template("about/author.html")


@about.route("/tech")
def tech():
    return render_template("about/tech.html")