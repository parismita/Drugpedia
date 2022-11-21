from flask import render_template, request, flash, Blueprint
from src.controllers.ingcontroller import details, search, create

ingredient = Blueprint('ingredient', __name__) 

ingredient.route('/create', methods=['GET'])(create)
ingredient.route('/search', methods=['GET'])(search)
ingredient.route('/details', methods=['GET'])(details)

