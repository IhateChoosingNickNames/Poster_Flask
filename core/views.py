from flask import render_template, request, redirect, url_for

from core.forms import FeedbackForm


def error_403(err):
    return render_template("core/403.html"), 403


def error_404(err):
    return render_template("core/404.html"), 404


def error_500(err):
    return render_template("core/500.html"), 500


def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        email = request.form["email"]
        text = request.form["text"]
        print(email)
        print(text)
        return redirect(url_for("posts.index"))
    return render_template("core/feedback.html", form=form)


