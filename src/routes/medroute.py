from flask import render_template, request, flash, Blueprint
from src.models.medicine import Med
from src.utils.initdb import db
from src.controllers.medcontroller import index, search, create

med = Blueprint('med', __name__)

@med.route("/", methods=['GET'])
def medadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = Med(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")

med.route('/create', methods=['GET'])(create)
med.route('/search', methods=['GET'])(search)

