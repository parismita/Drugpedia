from flask import request
from src.models.medicine import Med
from src.utils.initdb import db, create_db
from src.services.medservice import Vsearch, Hsearch, OtcDetails, DrugDetails

def create():
    create_db()


def search(): 
    # arguments ie key=pan for eg
    key = request.args.get("key")
    return Vsearch(key)    

def details(): 
    name = request.args.get("name")
    return OtcDetails(name)
