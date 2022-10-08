import json
from src.models.medicine import Med
from src.utils.initdb import db

def insert_logic():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = Med(pname, color)
    db.session.add(entry)
    db.session.commit()

    return '==================DATA INSERTED=================='
