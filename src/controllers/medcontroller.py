from flask import request
from src.models.medicine import Med
from src.utils.initdb import db, create_db
from src.services.medservice import Search, Details

def create():
    create_db()


def search(): 
    # arguments ie key=pan for eg
    key = request.args.get("key")
    return Search(key)    

def details(): 
    id = request.args.get("id")
    cat = request.args.get("cat")
    return Details(cat, id)
