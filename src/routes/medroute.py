from flask import render_template, request, flash, Blueprint
from src.models.medicine import Med
from src.utils.initdb import db
from src.controllers.medcontroller import search, create, details

med = Blueprint('med', __name__)

med.route('/create', methods=['GET'])(create)
med.route('/search', methods=['GET'])(search)
med.route('/details', methods=['GET'])(details)

