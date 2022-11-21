from flask import request
from src.models.medicine import Medicine
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
    return Details(id)
