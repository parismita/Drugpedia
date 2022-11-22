import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from src.utils.initdb import db
from src.models.ingredient import Ingredients

#db todo: CRUD med, ing
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


def Delete(url):
    try:
        Ingredients.query.filter_by(url=url).delete()
        db.session.commit()
    except Exception as e:
	    print(str(e))

def Get(url):
    try:
        res = Ingredients.query.filter_by(url=url).first()
        if(not res):
            return
        return res.json()
    except Exception as e:
	    print(str(e))

def IngredientDetails(key, name):
    if(key=="" or key==None):
        return {
        "status": 404,
        "data": None
    }

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
    drug_name = drug_header.get_text()
    print(drug_name)

    sections = ['uses-container',
                'side-effects-container', 'precautions-container']
    section_name = ['use', 'side_effect', 'precautions']

    res = {}
    res["name"]=name
    res["url"]=key
    for section, title in zip(sections, section_name):
        container = soup.find("div", attrs={"class": section})
        monograph_content_headline = container.find(
            "div", attrs={"class": "title-bg"})
        monograph_content = container.find(
            "div", attrs={"class": "monograph-content"})
        #title = monograph_content_headline.get_text(strip=True)
        description = monograph_content.get_text()
        res[title] = description

    #insert when not in db
    Insert(res)

    return {
        "status": source.status_code,
        "data": res,
        "from": "webmd"
    }


def IngredientSearch(key):
    if(key=="" or key==None):
        return {
        "status": 404,
        "data": None
    }

    url = 'https://www.webmd.com/drugs/2/search?type=drugs&query='+key
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    # print(html.status_code)

    soup = bs(html.content, 'html.parser')

    ing_name = []
    link = []
    for div in soup.find_all('div', {
            'class': 'drugs-exact-search-list'}):
        link.append(div.a['href'])
        ing_name.append(div.a.text.strip())

    for div in soup.find_all('div', {
            'class': 'drugs-partial-search-list'}):
        if (div.a['href'] not in link):
            link.append(div.a['href'])
            ing_name.append(div.a.text.strip())

    df = pd.DataFrame({
        'Name': ing_name,
        'Link': link})
    print(df)
    return {
        "status": html.status_code,
        "data": df.to_dict(orient='records')
    }


# Search("pan")