from flask import render_template, request, flash, Blueprint
from src.models.medicine import Med


med = Blueprint('med', __name__)

@med.route("/", methods=['GET'])
def medadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = Med(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")

