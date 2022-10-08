import json
from flask import request
from src.models.medicine import Med
from src.utils.initdb import db

# example service
"""def insert_logic():
    #data = json.load(open("data.json", 'r'))  # reading file data.json
    example = Inserttable(
            machineid=data["MachineId"], 
            stateid=data["StateId"],                 
            speed=data["Speed"], 
            statechange=data["StateChange"],
            unixtime=data["UnixTime"], 
            extras=data["Extras"],
            state="ON"
        )

    db.session.add(example)
    db.session.commit()
    return '==================DATA INSERTED=================='
"""
def insert_logic():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = Med(pname, color)
    db.session.add(entry)
    db.session.commit()

    return '==================DATA INSERTED=================='
