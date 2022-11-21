import requests
import json
from bs4 import BeautifulSoup as bs
import pandas as pd

# from db after scrapping and storing

def Search(key):
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


# Vsearch("Pan")
# Vsearch("s")
# Hsearch("crocin")

def Details(cat, id):
    url = 'https://www.1mg.com/'+cat+"/"+id
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    # print(html.status_code)

    content = bs(html.content, 'html.parser')
    
    if(cat=="otc"):
        med_desc, med_side, med_use, med_ing = OtcDetails(content)
    if(cat=="drugs"):
        med_desc, med_side, med_use, med_ing = DrugDetails(content)


    return {
        "status": html.status_code,
        "data": {
            "description": med_desc,
            "side_effects": med_side,
            "usage": med_use,
            "ingredient": med_ing
        }
    }

# scrapped
def OtcDetails(content):
    # from db find the url of the key given
    # if no url then do search to find and store the url

    med_desc = content.find_all('div', {
        'class': 'ProductDescription__description-content___A_qCZ'})
    #med_desc = med_desc['ul']
    med_ing = med_desc[0].find('ul').get_text()

    med_side=med_desc[0].find_all('ul')[1].get_text()
    med_use = med_desc[0].find_all('ul')[2].get_text()

    #print(med_desc)
    return str("med_desc"), med_side, med_use, med_ing


def DrugDetails(content):

    med_desc = content.find_all('div', {
        'class': 'DrugOverview__content___22ZBX'})[0].text.strip()
    # print(med_desc)

    med_side = content.find_all('div', {
        'class': 'DrugOverview__list-container' +
        '___2eAr6 DrugOverview__content___22ZBX'})[0].text.strip()
    # print(med_side)

    med_use = content.find_all('div', {
        'class': 'ShowMoreArray__tile___2mFZk'})[0].text.strip()
    # print(med_use)
    med_ing = content.find_all('div', {
        'class': 'saltInfo DrugHeader__meta-value___vqYM0'})[0].text.strip()

    return med_desc, med_side, med_use, med_ing


"""OtcDetails("otc/digene-acidity-gas-relief-gel-mint-otc236576")
DrugDetails("drugs/wikoryl-10-tablet-680587")
DrugDetails("drugs/pan-40-tablet-325250")
OtcDetails("otc/crocin-650-advance-tablet-otc638914")"""
