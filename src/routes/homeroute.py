from flask import render_template, request, flash, Blueprint

home = Blueprint('', __name__)

#static page render
@home.route("/", methods=['GET'])
def index():
    return render_template('index.html')
