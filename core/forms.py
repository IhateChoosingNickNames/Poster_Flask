from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class FeedbackForm(FlaskForm):
    email = EmailField("Почта", validators=[Email("Введите корректную почту")])
    text = StringField("Описание", validators=[DataRequired()])
    submit = SubmitField("Отправить")