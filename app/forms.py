from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'JPG and PNG Images only!')
    ])
