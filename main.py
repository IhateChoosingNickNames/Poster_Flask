from flask import render_template, request, redirect, url_for

from posts.forms import PostCreateForm, FeedbackForm
from settings import SECRET_KEY, app
from posts.models import Post, db



@app.route("/")
def index():
    return render_template("index.html", posts=Post.query.all())
@app.route("/feedback")
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        email = request.form["email"]
        text = request.form["text"]
        print(email)
        print(text)
        return redirect(url_for("index"))
    return render_template("feedback.html", form=form)

@app.route("/create", methods=["GET", "POST"])
def post_create():
    form = PostCreateForm()
    if form.validate_on_submit():
        title = request.form["title"]
        text = request.form["text"]
        group = request.form["group"]
        post = Post(title=title, text=text, group=group)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("creation.html", form=form)
@app.route("/")
def show_follows():
    return render_template("base.html")
@app.route("/")
def users_password_change_form():
    return render_template("base.html")
@app.route("/")
def users_logout():
    return render_template("base.html")
@app.route("/")
def users_login():
    return render_template("base.html")
@app.route("/")
def show_profile():
    return render_template("base.html")
@app.route("/")
def users_signup():
    return render_template("base.html")

@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = Post.query.filter_by(id=post_id)
    return render_template("index.html", posts=post)


@app.route("/")
def posts_group_list():
    return render_template("base.html")

if __name__ == '__main__':
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["DEBUG"] = True
    app.run(port=8000)