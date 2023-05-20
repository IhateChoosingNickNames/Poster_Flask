from flask import Flask

from setting import SECRET_KEY

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"

if __name__ == '__main__':
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["DEBUG"] = True
    app.run(port=8000)