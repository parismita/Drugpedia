import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from src.utils.initdb import db

# routes here
from src.routes.medroute import med
from src.routes.ingroute import ingredient
from src.routes.homeroute import home

# getting env variables from .env
load_dotenv()
USER = os.getenv('USER')
PASS = os.getenv('PASS')
HOST = os.getenv('HOST')
DB = os.getenv('DB')
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


def none_check(str, default):
    if (str is None):
        return (default)
    return (str)

# initializing flask and configuring sqlalchemy orm


def create_app():
    app = Flask(__name__, template_folder='src/templates')
    uri = none_check(USER, "postgresql")+":" + \
        none_check(PASS, "") + "@" + \
        none_check(HOST, "localhost") + "/" + \
        none_check(DB, "drugpedia")

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://" + uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    db.init_app(app)
    return app


app = create_app()

# all blurprints here
app.register_blueprint(med, url_prefix='/medicine')
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(ingredient, url_prefix='/ingredient')

# migrate
migrate = Migrate(app, db)

# running the app
if __name__ == '__main__':
    app.run(host=HOST, port=8080)