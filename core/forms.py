from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class FeedbackForm(FlaskForm):
    text = StringField("Описание", validators=[DataRequired()])
    email = TextAreaField("Почта", validators=[Email("Введите корректную почту")])
    submit = SubmitField("Отправить")