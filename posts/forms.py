from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

from models import Group, Tag


class PostCreateForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    text = TextAreaField("Описание", validators=[DataRequired()])
    group = SelectField("Группа", choices=[elem.slug for elem in Group.query.all()])
    tags = SelectMultipleField("Теги", choices=[elem.slug for elem in Tag.query.all()])
