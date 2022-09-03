from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            DataRequired("username required."),
            Length(1, 30, "length 1-30"),
        ]
    )
    email = StringField(
        "email",
        validators=[
            DataRequired("email required."),
            Email("format error.")
        ]
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired("password required.")
        ]
    )
    submit = SubmitField("register")

class LoginForm(FlaskForm):
    email = StringField(
        "email",
        validators=[
            DataRequired("email required."),
            Email("format error.")
        ]
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired("password required.")
        ]
    )
    submit = SubmitField("login")