from flask import render_template, request, Blueprint, redirect, url_for, session

from src.services.medservice import Search

home = Blueprint('', __name__)

search_response = {}

#static page render
@home.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        session['drug_search'] = request.form['drug-search']
        return redirect(url_for('search_results'))
    else:
        return render_template('index.html')

@home.route("/search-results", methods=['POST', 'GET'])
def search_results():
    # search_results_json = details()
    # print()
    search_response = Search(session.get('drug_search'))
    search_response = search_response['data']
    if(not search_response):
        return redirect(url_for('index'))
    return render_template('search-results.html', search_response = search_response)
