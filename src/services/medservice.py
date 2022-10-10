import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def Vsearch(key):
    url = 'https://www.1mg.com/search/all?filter=true&name='+key
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)' +
              'Chrome/83.0.4103.97 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    # print(html.status_code)

    soup = bs(html.content, 'html.parser')

    product_name = []
    for name in soup.find_all('span', {
            'class': 'style__pro-title___3zxNC'}):
        product_name.append(name.text.strip())

    pack_size = []
    for size in soup.find_all('div', {
            'class': 'style__pack-size___254Cd'}):
        pack_size.append(size.text.strip())

    mrp = []
    for price in soup.find_all('div', {
            'class': 'style__price-tag___B2csA'}):
        mrp.append(price.text.replace('₹', '').replace('MRP', '').strip())

    link = []
    for div in soup.find_all('div', {
            'class': 'style__horizontal-card___1Zwmt' +
            ' style__height-158___1XIvD'}):
        link.append(div.a['href'])

    df = pd.DataFrame({'Product Name': product_name, 'Link': link})
    # print(df)
    return {"data":list(df)}


def Hsearch(key):
    url = 'https://www.1mg.com/search/all?filter=true&name='+key
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)' +
              'Chrome/83.0.4103.97 Safari/537.36'
              }
    html = requests.get(url=url, headers=header)
    # print(html.status_code)

    soup = bs(html.content, 'html.parser')

    product_name = []
    for name in soup.find_all('div', {
            'class': 'style__pro-title___3G3rr'}):
        product_name.append(name.text.strip())

    pack_size = []
    for size in soup.find_all('div', {
            'class': 'style__pack-size___3jScl'}):
        pack_size.append(size.text.strip())

    mrp = []
    for price in soup.find_all('div', {
            'class': 'style__price-tag___KzOkY'}):
        mrp.append(price.text.replace('₹', '').replace('MRP', '').strip())

    link = []
    for url in soup.find_all('a', {
            'class': 'style__product-link___1hWpa'}, href=True):
        link.append(url['href'])

    # print(product_name, pack_size, mrp)
    df = pd.DataFrame({
        'Product Name': product_name,
        'Link': link})
    # print(df)
    return {"data":list(df)}


# Vsearch("Pan")
# Vsearch("s")
# Hsearch("crocin")
