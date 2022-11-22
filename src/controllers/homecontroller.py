from flask import render_template, request, Blueprint, redirect, url_for, session
from src.models.ingredient import Ingredients
from src.utils.initdb import db, create_db
from src.services.ingservice import IngredientDetails, IngredientSearch


def index():
    if request.method == 'POST':
        session['drug_search'] = request.form['drug-search']
        return redirect(url_for('medicine.search_results'))
    else:
        return render_template('index.html')