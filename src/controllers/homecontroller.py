from flask import render_template, request, redirect, url_for, session


def index():
    if request.method == 'POST':
        session['drug_search'] = request.form['drug-search']
        return redirect(url_for('medicine.search_results'))
    else:
        return render_template('index.html')
