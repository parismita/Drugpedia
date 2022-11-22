from flask import Blueprint
from src.controllers.ingcontroller import ingredient_details, \
    search_ingredient, search_ingredient_results

ingredient = Blueprint('ingredient', __name__)

ingredient.route('/search', methods=['POST', 'GET'])(search_ingredient)
ingredient.route('/search-results',
                 methods=['POST', 'GET'])(search_ingredient_results)
ingredient.route('/details', methods=['GET', 'POST'])(ingredient_details)
