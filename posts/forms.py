from settings import app
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email


class PostCreateForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    text = TextAreaField("Описание", validators=[DataRequired()])
    group = IntegerField("Группа")


class FeedbackForm(FlaskForm):
    text = StringField("Описание", validators=[DataRequired()])
    email = TextAreaField("Почта", validators=[Email("Введите корректную почту")])
    submit = SubmitField("Отправить")