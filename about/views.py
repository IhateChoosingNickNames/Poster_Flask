from flask import render_template


def author():
    return render_template("about/author.html")


def tech():
    return render_template("about/tech.html")

