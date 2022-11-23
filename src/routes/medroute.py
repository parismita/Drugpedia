from flask import Blueprint
from src.controllers.medcontroller import medicine_details, \
    search_results, details, search

med = Blueprint('medicine', __name__)

med.route('/details', methods=['GET', 'POST'])(medicine_details)
med.route("/search-results", methods=['POST', 'GET'])(search_results)
med.route('/details-json', methods=['GET', 'POST'])(details)
med.route('/search-json', methods=['GET', 'POST'])(search)
"""
http://localhost:8080/med/details?cat=otc&id=crocin-650-advance-tablet-otc638914

"""
