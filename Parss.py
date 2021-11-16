import requests
import json
import csv
import os

from bs4 import BeautifulSoup

os.system('mkdir heros_csv')
os.system('mkdir heros_json')

URL = 'https://www.marvel.com/v1/pagination/grid_cards?offset=0&limit=36&entityType=character&sortField=title&sortDirection=asc'
HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }


def get_data_json(url):
    response = requests.get(url)
    return response.json()['data']['results']['data']

def get_hero_list(data, heros):
    for i in range(0, 36):
        hero = {}
        hero['name'] = data[i]['link']['title']
        hero['link'] = 'https://www.marvel.com' + data[i]['link']['link']
        hero = hero | parse(hero['link'])
        heros.append(hero)
    return heros


def parse(url):
    response = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')
    items = soup.findAll('li', class_ = 'railBioInfo__Item')
    comps = {}
    
    for item in items:
        key = item.find('p', class_ = 'railBioInfoItem__label').get_text(strip = True)
        comps[key] = item.find('li').get_text(strip = True)

    return comps


def file_write_csv(heros):
    print('Створення CSV файлів')

    for hero in heros:
        with open(f"heros_csv/{hero['name']}.csv", "w", newline="") as file:
            writer = csv.writer(file)

            for key, value in hero.items():
                writer.writerow([key, value])
    
    print("CSV файли створені")

def file_write_json(heros):
    print('Створення JSON файлів')

    for hero in heros:
        heros_json = json.dumps(hero)  
        with open(f"heros_json/{hero['name']}.json", "w") as my_file:
            my_file.write(heros_json)

    print('JSON файли створені')


def main():
    heros = []
    dataset = get_data_json(URL)
    heros = get_hero_list(dataset, heros)

    file_write_csv(heros)
    file_write_json(heros)

if __name__ == '__main__':
    main()
