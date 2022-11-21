import json
from src.models.ingredient import Ingredients
from src.utils.initdb import db, create_db
from src.services.ingservice import Details, Search
from flask import request

def create():
    create_db()


# insert data into table.
def details():
    return Details(request.args.get("id"))    

def search(): 
    return Search(request.args.get("key"))  
