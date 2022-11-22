import json
from src.models.ingredient import Ingredients
from src.utils.initdb import db, create_db
from src.services.ingservice import IngredientDetails, IngredientSearch
from flask import request

def create():
    create_db()


# insert data into table.
def details(): 
    id = request.args.get("id")
    name = request.args.get("name")
    return IngredientDetails(id, name)    

def search(): 
    return IngredientSearch(request.args.get("key"))  
