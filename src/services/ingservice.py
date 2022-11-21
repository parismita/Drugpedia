import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def Details(key):
    search_url = "https://www.webmd.com/drugs/2/" + key
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

    res = {}
    for section in sections:
        container = soup.find("div", attrs={"class": section})
        monograph_content_headline = container.find(
            "div", attrs={"class": "title-bg"})
        monograph_content = container.find(
            "div", attrs={"class": "monograph-content"})
        title = monograph_content_headline.get_text(strip=True)
        description = monograph_content.get_text()
        res[title] = description

    return {
        "status": source.status_code,
        "data": res
    }


def Search(key):
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