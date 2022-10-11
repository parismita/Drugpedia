from src.models.ingredient import Ingredients
from flask import render_template, request, flash, Blueprint
from src.models.ingredient import Ingredients
from src.utils.initdb import db
from src.controllers.ingcontroller import index, search, create

ingredient = Blueprint('ingredient', __name__)

@ingredient.route("/", methods=['GET'])
def ingredientadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = Ingredients(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")

ingredient.route('/create', methods=['GET'])(create)
ingredient.route('/search', methods=['GET'])(search)

