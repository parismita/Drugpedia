from flask import request
from src.models.medicine import Medicine
from src.utils.initdb import db, create_db
from src.services.medservice import MedSearch, MedDetails

def create():
    create_db()


def search(): 
    # arguments ie key=pan for eg
    key = request.args.get("key")
    return MedSearch(key)    

def details(): 
    id = request.args.get("id")
    name = request.args.get("name")
    return MedDetails(id, name)
