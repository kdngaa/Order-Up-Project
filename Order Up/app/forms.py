from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, PasswordField
)
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    employee_number = StringField("Employee Number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
