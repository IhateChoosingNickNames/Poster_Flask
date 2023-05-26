from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

app.app_context().push()
import models
migrate = Migrate(app, db)


