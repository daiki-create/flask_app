from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length

class UserForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            DataRequired(message="username required."),
            length(max=30, message="less than 30.")
        ]
    )

    email = StringField(
        "email",
        validators=[
            DataRequired(message="email required."),
            Email(message="mail format.")
        ]
    )

    password = PasswordField(
        "password",
        validators=[
            DataRequired(message="password required.")
        ]
    )

    submit = SubmitField("register")