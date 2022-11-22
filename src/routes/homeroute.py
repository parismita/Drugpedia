from flask import render_template, request, Blueprint, redirect, url_for, session

from src.services.medservice import Search, Details

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

@home.route("/search-results", methods=['POST', 'GET'])
def search_results():
    search_response = Search(session.get('drug_search'))
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
    medicine_details_response = Details(session.get('medicine_link'), session.get('medicine_name'))
    medicine_details_response = medicine_details_response['data']
    print(medicine_details_response)
    # if(not medicine_details_response):
    #     return redirect(url_for('index'))
    return render_template('medicine-details.html', name = session.get('medicine_name'), medicine_details_response = medicine_details_response)