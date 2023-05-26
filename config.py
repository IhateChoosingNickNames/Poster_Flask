import os
from dotenv import load_dotenv


load_dotenv()


class Configuration:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
