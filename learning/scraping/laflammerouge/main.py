from bs4 import BeautifulSoup
import requests
import lxml

year = 2022

url = 'https://www.la-flamme-rouge.eu/maps/races/view/' + str(year) + '/'

for i in range(1467):

    race = str(i - 1)

    req = requests.get(url + race)
    html = req.content

    soup = BeautifulSoup(html, 'lxml')

    area = soup.find('div', class_='raceViewBar__title')

    header = area.find('h1')

    print(race, "-", header.text)