import requests, re
from bs4 import BeautifulSoup as bs
import pandas as pd
from src.utils.initdb import db
from src.models.medicine import Medicine

#404 response
def NullData():
    return {
        "status": 404,
        "data": None
    }

#insert into postgres - medicine   
def Insert(data):
    #post
    try:
        entry = Medicine(
            name=data["name"], 
            description=data["description"], 
            url=data["url"], 
            use=data["usage"], 
            side_effect=data["side_effect"],
            ingredient=data["ingredient"])
        db.session.add(entry)
        db.session.commit()
    except Exception as e:
	    print(str(e))

#delete from medicine
def Delete(url):
    try:
        Medicine.query.filter_by(url=url).delete()
        db.session.commit()
    except Exception as e:
	    print(str(e))

#select by filter id from medicine
def Get(url):
    try:
        res = Medicine.query.filter_by(url=url).first()
        if(not res):
            return
        return res.json()
    except Exception as e:
	    print(str(e))


# from db after scrapping and storing
def MedSearch(key):
    if(key=="" or key==None):
        return {
        "status": 404,
        "data": None
    }

    url = 'https://www.1mg.com/search/all?filter=true&name='+key
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    content = bs(html.content, 'html.parser')

    v = Vsearch(content)
    h = Hsearch(content)
    df = pd.concat([v,h])
    print(df, v, h)
    return {
        "status": html.status_code,
        "data": df.to_dict(orient='records')
    }


def Vsearch(content):
    med_name = []
    for name in content.find_all('span', {
            'class': 'style__pro-title___3zxNC'}):
        med_name.append(name.text.strip())

    link = []
    for div in content.find_all('div', {
            'class': 'style__horizontal-card___1Zwmt' +
            ' style__height-158___1XIvD'}):
        link.append(div.a['href'])

    df = pd.DataFrame({
        'Name': med_name,
        'Link': link})
    # print(df)
    return df



def Hsearch(content):
    med_name = []
    for name in content.find_all('div', {
            'class': 'style__pro-title___3G3rr'}):
        med_name.append(name.text.strip())

    link = []
    for url in content.find_all('a', {
            'class': 'style__product-link___1hWpa'}, href=True):
        link.append(url['href'])

    # print(product_name, pack_size, mrp)
    df = pd.DataFrame({
        'Name': med_name,
        'Link': link})
    # print(df)
    return df

def MedDetails(id, name):
    if(id=="" or id==None):
        return NullData()

    #from db
    data = Get(id)
    if(data):
        return {
            "status": 200,
            "data": data, 
            "from": "postgres"
        }
    
    #scrap
    url = 'https://www.1mg.com'+id
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)

    content = bs(html.content, 'html.parser')
    cat = id.split("/")[1]

    #initialize
    med_desc = None; med_side = None; med_use = None; med_ing = None

    #send to respective module based on if its otc or drug
    if(cat=="otc"):
        med_desc = OtcDetails(content)
    if(cat=="drugs"):
        med_desc, med_side, med_use, med_ing = DrugDetails(content)


    response =  {
        "status": html.status_code,
        "data": {
            "description": med_desc,
            "side_effect": med_side,
            "usage": med_use,
            "ingredient": med_ing,
            "name": name,
            "url": id
        },
        "from": "1mg"
    }

    #insert when not in db
    Insert(response['data'])
    return response

#data should be bsoup html data, return value string
def spacing(data):
    #newline on break
    data = str(data) \
                .replace("<br/>","\n") \
                .replace("<br>", "\n") 
    
    #spacing
    data = data \
                .replace("</li>","\n</li>") \
                .replace("</p>", " </p>") \
                .replace("</div>"," </div>")   
    return bs(data, 'html.parser') 

# scrapped
def OtcDetails(content):
    #no seperate classes or id found hence putting everythihng in description
    med_desc = content.find_all('div', {
        'class': 'ProductDescription__description-content___A_qCZ'})
    
    #none check
    if((not med_desc) or (not med_desc[0])):
        return NullData()
    
    #check spacing and get all data together as one string
    med_desc = spacing(med_desc[0]).get_text()
    med_desc = re.sub("\t+", " ", med_desc)
    return med_desc


def DrugDetails(content):
    #content spacing check and formatting
    content = spacing(content)

    #medicine description
    med_desc = content.find_all('div', {
        'class': 'DrugOverview__content___22ZBX'})[0].get_text()
    # print(med_desc)

    #medicine side effects
    med_side = content.find_all('div', {
        'class': 'DrugOverview__list-container' +
        '___2eAr6 DrugOverview__content___22ZBX'})[0].get_text()
    # print(med_side)

    #medicine usage
    med_use = content.find_all('div', {
        'class': 'ShowMoreArray__tile___2mFZk'})[0].get_text()
    # print(med_use)

    #medicine ingredients
    med_ing = content.find_all('div', {
        'class': 'saltInfo DrugHeader__meta-value___vqYM0'})[0].get_text()

    return med_desc, med_side, med_use, med_ing


"""OtcDetails("otc/digene-acidity-gas-relief-gel-mint-otc236576")
DrugDetails("drugs/wikoryl-10-tablet-680587")
DrugDetails("drugs/pan-40-tablet-325250")
OtcDetails("otc/crocin-650-advance-tablet-otc638914")
Vsearch("Pan")
Vsearch("s")
Hsearch("crocin")
"""
