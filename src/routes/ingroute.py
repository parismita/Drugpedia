from flask import render_template, request, flash, Blueprint
from src.controllers.ingcontroller import ingredient_details, search_ingredient, create, search_ingredient_results

ingredient = Blueprint('ingredient', __name__) 

ingredient.route('/create', methods=['GET'])(create)
ingredient.route('/search', methods=['POST', 'GET'])(search_ingredient)
ingredient.route('/search-results', methods=['POST', 'GET'])(search_ingredient_results)
ingredient.route('/details', methods=['GET', 'POST'])(ingredient_details)
