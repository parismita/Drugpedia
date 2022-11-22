from flask import render_template, request, Blueprint, redirect, url_for, session
from src.services.medservice import MedDetails, MedSearch
from src.services.ingservice import IngredientSearch, IngredientDetails

home = Blueprint('', __name__)

# search_response = {}
medicine_details_response = {}

@home.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        session['drug_search'] = request.form['drug-search']
        return redirect(url_for('search_results'))
    else:
        return render_template('index.html')

@home.route("/search-ingredient", methods=['POST', 'GET'])
def search_ingredient():
    if request.method == 'POST':
        session['drug_search'] = request.form['drug-search']
        return redirect(url_for('search_ingredient_results'))
    else:
        return render_template('search-ingredient.html')

@home.route("/search-ingredient-results", methods=['POST', 'GET'])
def search_ingredient_results():
    search_response = IngredientSearch(session.get('drug_search'))
    search_response = search_response['data']
    session['search_response'] = search_response
    print(search_response)
    # if(not search_response):
    #     return redirect(url_for('index'))
    if request.method == 'POST':
        session['ingredient_name'] = request.form['medicine-name']
        print(session['medicine_name'])
        return redirect(url_for('ingredient_details'))
    else:
        return render_template('search-ingredient-results.html', search_response = search_response)

@home.route("/search-results", methods=['POST', 'GET'])
def search_results():
    search_response = MedSearch(session.get('drug_search'))
    search_response = search_response['data']
    session['search_response'] = search_response
    # print(search_response)
    # if(not search_response):
    #     return redirect(url_for('index'))
    if request.method == 'POST':
        session['medicine_name'] = request.form['medicine-name']
        print(session['medicine_name'])
        return redirect(url_for('medicine_details'))
    else:
        return render_template('search-results.html', search_response = search_response)

@home.route("/medicine-details", methods = ['POST', 'GET'])
def medicine_details():
    for medicine in session.get('search_response'):
        if session['medicine_name'] == medicine['Name']:
            # print('yes')
            # print(medicine['Link'])
            session['medicine_link'] = medicine['Link']
    medicine_details_response = MedDetails(session.get('medicine_link'), session.get('medicine_name'))
    medicine_details_response = medicine_details_response['data']
    print(medicine_details_response)
    # if(not medicine_details_response):
    #     return redirect(url_for('index'))
    return render_template('medicine-details.html', name = session.get('medicine_name'), medicine_details_response = medicine_details_response)

@home.route("/ingredient-details", methods = ['POST', 'GET'])
def ingredient_details():
    for ingredient in session.get('search_response'):
        if session['ingredient_name'] == ingredient['Name']:
            # print('yes')
            # print(medicine['Link'])
            session['ingredient_link'] = ingredient['Link']
    ingredient_details_response = IngredientDetails(session.get('ingredient_link'), session.get('ingredient_name'))
    ingredient_details_response = ingredient_details_response['data']
    print(ingredient_details_response)
    # if(not medicine_details_response):
    #     return redirect(url_for('index'))
    return render_template('ingredient-details.html', name = session.get('ingredient_name'), ingredient_details_response = ingredient_details_response)