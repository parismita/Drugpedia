from flask import render_template, request, redirect, url_for, session
from src.services.ingservice import IngredientDetails, IngredientSearch

# insert data into table.


def details():
    id = request.args.get("id")
    name = request.args.get("name")
    return IngredientDetails(id, name)

# search json result


def search():
    return IngredientSearch(request.args.get("key"))


# search home page ingredient
def search_ingredient():
    if request.method == 'POST':
        session['drug_search'] = request.form['drug-search']
        return redirect(url_for('ingredient.search_ingredient_results'))
    else:
        return render_template('search-ingredient.html')


# ingredient search results
def search_ingredient_results():
    search_response = IngredientSearch(session.get('drug_search'))
    search_response = search_response['data']
    session['search_response'] = search_response

    if request.method == 'POST':
        session['ingredient_name'] = request.form['medicine-name']
        return redirect(url_for('ingredient.ingredient_details'))
    else:
        return render_template('search-ingredient-results.html',
                               search_response=search_response)


# ingredient detail page
def ingredient_details():
    for ingredient in session.get('search_response'):
        if session['ingredient_name'] == ingredient['Name']:
            session['ingredient_link'] = ingredient['Link']
    ingredient_details_response = IngredientDetails(
        session.get('ingredient_link'), session.get('ingredient_name'))
    ingredient_details_response = ingredient_details_response['data']
    print(ingredient_details_response)

    # renaming for lint fix
    sess_name = session.get('ingredient_name')
    idr = ingredient_details_response
    return render_template('ingredient-details.html',
                           name=sess_name,
                           ingredient_details_response=idr)
