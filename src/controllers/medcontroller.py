from flask import render_template, request, Blueprint, redirect, url_for, session
from src.models.medicine import Medicine
from src.utils.initdb import db, create_db
from src.services.medservice import MedSearch, MedDetails

def create():
    create_db()


def search(): 
    # arguments ie key=pan for eg
    key = request.args.get("key")
    return MedSearch(key)    

def details(): 
    id = request.args.get("id")
    name = request.args.get("name")
    return MedDetails(id, name)

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
        return redirect(url_for('medicine.medicine_details'))
    else:
        return render_template('search-results.html', search_response = search_response)

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



