from flask import Blueprint
from src.controllers.homecontroller import index, create

home = Blueprint('', __name__)

home.route("/", methods=['POST', 'GET'])(index)
home.route("/create", methods=['POST', 'GET'])(create)
