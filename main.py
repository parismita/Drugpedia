import os
from dotenv import load_dotenv
from flask import Flask, render_template
from src.routes.medroute import med
from flask_migrate import Migrate
from src.models.medicine import db

# getting env variables from .env
load_dotenv()
USER = os.getenv('USER')
PASS = os.getenv('PASS')
HOST = os.getenv('HOST')
DB = os.getenv('DB')
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

# initializing flask and configuring sqlalchemy orm
def create_app():
    app = Flask(__name__, template_folder='src/templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + \
        USER+':'+PASS+'@'+HOST+'/'+DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    return app


app = create_app()

#all blurprints here
app.register_blueprint(med, url_prefix='/med')

#migrate
migrate = Migrate(app, db)

#main page 
@app.route('/')
def index():
    return render_template('index.html')


# running the app
if __name__ == '__main__':
    app.run(host=HOST, port=8080)
