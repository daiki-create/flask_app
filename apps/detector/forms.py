from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms import SubmitField

class UploadImageForm(FlaskForm):
    image = FileField(
        validators = [
            FileRequired("select image."),
            FileAllowed(["png", "jpg", "jpeg"], "unssupported type")
        ]
    )
    submit = SubmitField("upload")

class DetectorForm(FlaskForm):
    submit = SubmitField("detect")