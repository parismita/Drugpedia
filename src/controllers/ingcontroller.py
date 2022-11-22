from flask import render_template, request, Blueprint, redirect, url_for, session
from src.models.ingredient import Ingredients
from src.utils.initdb import db, create_db
from src.services.ingservice import IngredientDetails, IngredientSearch

def create():
    create_db()


# insert data into table.
def details(): 
    id = request.args.get("id")
    name = request.args.get("name")
    return IngredientDetails(id, name)    

def search(): 
    return IngredientSearch(request.args.get("key"))


def search_ingredient():
    if request.method == 'POST':
        session['drug_search'] = request.form['drug-search']
        return redirect(url_for('ingredient.search_ingredient_results'))
    else:
        return render_template('search-ingredient.html')  


def search_ingredient_results():
    search_response = IngredientSearch(session.get('drug_search'))
    search_response = search_response['data']
    session['search_response'] = search_response
    #print(search_response)
    # if(not search_response):
    #     return redirect(url_for('index'))
    if request.method == 'POST':
        session['ingredient_name'] = request.form['medicine-name']
        #print(session['medicine_name'])
        return redirect(url_for('ingredient.ingredient_details'))
    else:
        return render_template('search-ingredient-results.html', search_response = search_response)


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
