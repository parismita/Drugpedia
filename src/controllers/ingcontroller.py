import json
from src.models.ingredient import Ingredients
from src.utils.initdb import db, create_db
from src.services.ingservice import IngredientSearch, Search
from flask import request

def index():
    return {
        'status': 'OK',
        'code': 200,
        'data': ''
    }


def create():
    create_db()


# insert data into table.
def details(): 
    return IngredientSearch(request.args.get("name"))    

def search(): 
    return Search(request.args.get("key"))  
