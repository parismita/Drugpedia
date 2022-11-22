from flask import Blueprint
from src.controllers.homecontroller import index

home = Blueprint('', __name__)

home.route("/", methods=['POST', 'GET'])(index)