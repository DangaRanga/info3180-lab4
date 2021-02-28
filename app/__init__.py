
from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
print(app.config.get('UPLOAD_FOLDER'))
from app import views
