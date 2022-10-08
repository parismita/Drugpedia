import json
from src.models.medicine import Med
from src.utils.initdb import db, create_db
from src.services.medservice import insert_logic

def index():
    return {
        'status': 'OK',
        'code': 200,
        'data': ''
    }


def create():
    create_db()


# insert data into table.
def insert(): 
    insert_logic()    