import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# from db after scrapping and storing


def Vsearch(key):
    url = 'https://www.1mg.com/search/all?filter=true&name='+key
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    # print(html.status_code)

    soup = bs(html.content, 'html.parser')

    med_name = []
    for name in soup.find_all('span', {
            'class': 'style__pro-title___3zxNC'}):
        med_name.append(name.text.strip())

    link = []
    for div in soup.find_all('div', {
            'class': 'style__horizontal-card___1Zwmt' +
            ' style__height-158___1XIvD'}):
        link.append(div.a['href'])

    df = pd.DataFrame({
        'Name': med_name,
        'Link': link})
    # print(df)
    return {
        "status": html.status_code,
        "data": df.to_dict(orient='records')
    }


def Hsearch(key):
    url = 'https://www.1mg.com/search/all?filter=true&name='+key
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)' +
              'Chrome/83.0.4103.97 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    # print(html.status_code)

    soup = bs(html.content, 'html.parser')

    med_name = []
    for name in soup.find_all('div', {
            'class': 'style__pro-title___3G3rr'}):
        med_name.append(name.text.strip())

    link = []
    for url in soup.find_all('a', {
            'class': 'style__product-link___1hWpa'}, href=True):
        link.append(url['href'])

    # print(product_name, pack_size, mrp)
    df = pd.DataFrame({
        'Name': med_name,
        'Link': link})
    # print(df)
    return {
        "status": html.status_code,
        "data": df.to_dict(orient='records')
    }

# Vsearch("Pan")
# Vsearch("s")
# Hsearch("crocin")


# scrapped
def OtcDetails(key):
    # from db find the url of the key given
    # if no url then do search to find and store the url
    url = 'https://www.1mg.com/'+key
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    # print(html.status_code)

    soup = bs(html.content, 'html.parser')

    med_desc = soup.find_all('div', {
        'class': 'ProductDescription__description-content___A_qCZ'})[0]

    print(med_desc)
    return {
        "status": html.status_code,
        "data": med_desc
    }


def DrugDetails(key):
    url = 'https://www.1mg.com/'+key
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; ' +
              'Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0' +
              'AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/104.0.0.0 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    # print(html.status_code)

    soup = bs(html.content, 'html.parser')

    med_desc = soup.find_all('div', {
        'class': 'DrugOverview__content___22ZBX'})[0].text.strip()
    # print(med_desc)

    med_side = soup.find_all('div', {
        'class': 'DrugOverview__list-container' +
        '___2eAr6 DrugOverview__content___22ZBX'})[0].text.strip()
    # print(med_side)

    med_use = soup.find_all('div', {
        'class': 'ShowMoreArray__tile___2mFZk'})[0].text.strip()
    # print(med_use)

    return {
        "status": html.status_code,
        "data": {
            "description": med_desc,
            "side_effects": med_side,
            "usage": med_use
        }
    }


"""OtcDetails("otc/digene-acidity-gas-relief-gel-mint-otc236576")
DrugDetails("drugs/wikoryl-10-tablet-680587")
DrugDetails("drugs/pan-40-tablet-325250")
OtcDetails("otc/crocin-650-advance-tablet-otc638914")"""
