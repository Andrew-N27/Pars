# scraper.py
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from requests.api import head

# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')

# print(soup)


URL = 'https://www.marvel.com/characters'
HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

def get_articles_urls():
    with requests.Session() as session:
        session = requests.Session()

    response = session.get(url = URL, headers = HEADERS)
    #response = requests.get(URL, headers = HEADERS)
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

def parse():
    URL = 'https://www.marvel.com/characters'
    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')
    items = soup.findAll('div', class_ = 'mvl-card mvl-card--explore')
    #items = items.findAll() #mvl-card mvl-card--explore
    comps = []
    cout = 0
    for item in items:
        comps.append({                      # card-body__headline
            'name': item.find('p', class_ = 'card-body__headline').get_text(strip = True),
            'link': 'https://www.marvel.com' + item.find('a', class_ = 'explore__link').get('href')
        })
        cout += 1
    print(cout)
    cout = 0
    for comp in comps:
        print(comp['name'], '-->' , '\t', comp['link'])
        cout += 1
    
    print(cout)

def get_text_from_html():
    with open('index.html', encoding='utf-8') as file:
        src = file.read()
    
    soup = BeautifulSoup(src, 'lxml')

    items = soup.findAll('p', class_ = 'card-body__headline')#'div', class_ = 'mvl-card mvl-card--explore'
    #items = items.findAll() #mvl-card mvl-card--explore
    comps = []
    cout = 0
    for item in items:
        comps.append({                      # card-body__headline
            'name': item.text.strip()
            #'name': item.find('p', class_ = 'card-body__headline').get_text(strip = True),
            #'link': 'https://www.marvel.com' + item.find('a', class_ = 'explore__link').get('href')
        })
        cout += 1
    print(cout)
    cout = 0
    for comp in comps:
        print(comp['name'])
        cout += 1
    
    print(cout)

get_text_from_html()

#parse()

#get_articles_urls()


# def main():
#     pass


# main()