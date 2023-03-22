from bs4 import BeautifulSoup
import requests


url = "https://www.procyclingstats.com/race/gp-de-denain/2023/result/live"


def get_km_to_go():
    req = requests.get(url)
    html = req.content

    soup = BeautifulSoup(html, 'lxml')

    area = soup.find('li', class_='kmtogo')

    km = area.findNext('div').findNext('div')

    print(km.text)

    return km.text

