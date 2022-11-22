from flask import render_template, request, flash, Blueprint
from src.controllers.medcontroller import search, create, medicine_details, search_results

med = Blueprint('medicine', __name__)

med.route('/create', methods=['GET'])(create)
med.route('/search', methods=['GET'])(search)
med.route('/details', methods=['GET', 'POST'])(medicine_details)
med.route("/search-results", methods=['POST', 'GET'])(search_results)

"""
http://localhost:8080/med/details?cat=otc&id=crocin-650-advance-tablet-otc638914

"""