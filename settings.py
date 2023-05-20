import os
from dotenv import load_dotenv
from flask import Flask

from about.main import about
from core.main import core


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


app = Flask(__name__)
app.register_blueprint(about, url_prefix="/about")
app.register_blueprint(core)