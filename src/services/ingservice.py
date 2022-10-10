#https://www.webmd.com/drugs/2/search?type=drugs&query=key
#301-http status - moved perm means dont show these in search result

import requests
from bs4 import BeautifulSoup as bs


def IngredientSearch(key):
    search_url = "https://www.webmd.com/drugs/2/drug-17633/pantoprazole-oral/details"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source = requests.get(search_url, headers = headers)
    soup = bs(source.content)

    drug_header = soup.find("h1", attrs = {"class": "drug-name"})
    drug_name = drug_header.get_text()
    print(drug_name)

    sections = ['uses-container', 'side-effects-container', 'precautions-container']

    for section in sections:
        container = soup.find("div", attrs = {"class": section})
        monograph_content_headline = container.find("div", attrs = {"class": "title-bg"})
        monograph_content = container.find("div", attrs = {"class": "monograph-content"})
        title = monograph_content_headline.get_text(strip = True)
        description = monograph_content.get_text()
        print(title)
        print(description)
    
    