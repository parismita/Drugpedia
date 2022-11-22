import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from src.utils.initdb import db
from src.models.ingredient import Ingredients

def NullData():
    return {
        "status": 404,
        "data": None
    }
    

#insert into ingredient
def Insert(data):
    #post
    try:
        entry = Ingredients(
            name=data["name"], 
            precautions=data["precautions"], 
            url=data["url"], 
            use=data["use"], 
            side_effect=data["side_effect"])
        db.session.add(entry)
        db.session.commit()
    except Exception as e:
	    print(str(e))

#delete from ingredient
def Delete(url):
    try:
        Ingredients.query.filter_by(url=url).delete()
        db.session.commit()
    except Exception as e:
	    print(str(e))

#get by filter, from ingredient
def Get(url):
    try:
        res = Ingredients.query.filter_by(url=url).first()
        if(not res):
            return
        return res.json()
    except Exception as e:
	    print(str(e))

#the details of ingredient
def IngredientDetails(key, name):
    if(key=="" or key==None):
        return NullData()

    #from db
    data = Get(key)
    if(data):
        return {
            "status": 200,
            "data": data, 
            "from": "postgres"
        }

    #scrap
    search_url = "https://www.webmd.com" + key
    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    source = requests.get(search_url, headers=headers)
    soup = bs(source.content, 'html.parser')

    drug_header = soup.find("h1", attrs={"class": "drug-name"})
    if(not drug_header):
        return NullData()

    sections = ['uses-container',
                'side-effects-container', 'precautions-container']
    section_name = ['use', 'side_effect', 'precautions']

    #loop through the sections to get use, side effect, precaution
    res = {}
    res["name"]=name
    res["url"]=key
    for section, title in zip(sections, section_name):
        container = soup.find("div", attrs={"class": section})
        monograph_content = container.find(
            "div", attrs={"class": "monograph-content"})
        description = monograph_content.get_text()
        res[title] = description

    #insert when not in db
    Insert(res)

    return {
        "status": source.status_code,
        "data": res,
        "from": "webmd"
    }


#search for ingredients
def IngredientSearch(key):
    if(key=="" or key==None):
        return NullData()

    url = 'https://www.webmd.com/drugs/2/search?type=drugs&query='+key
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)

    soup = bs(html.content, 'html.parser')

    #scraping
    ing_name = []
    link = []

    #finding the exact matching 
    exact = soup.find('div', {
            'class': 'drugs-exact-search-list'})
    exact = exact.find_all('li')
    for div in exact:
        link.append(div.a['href'])
        ing_name.append(div.a.text.strip())
        print(div.a.text.strip()+"\n")

    #finding partial matchings
    partial = soup.find('div', {
            'class': 'drugs-partial-search-list'})
    partial = partial.find_all('li')
    for div in partial:
        if (div.a['href'] not in link):
            link.append(div.a['href'])
            ing_name.append(div.a.text.strip())

    #making it into dataframe
    df = pd.DataFrame({
        'Name': ing_name,
        'Link': link})
    
    return {
        "status": html.status_code,
        "data": df.to_dict(orient='records')
    }


# Search("pan")