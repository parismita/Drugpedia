from flask import render_template, request, flash, Blueprint
from src.controllers.medcontroller import search, create, details

med = Blueprint('med', __name__)

med.route('/create', methods=['GET'])(create)
med.route('/search', methods=['GET'])(search)
med.route('/details', methods=['GET', 'POST'])(details)

"""
http://localhost:8080/med/details?cat=otc&id=crocin-650-advance-tablet-otc638914

"""