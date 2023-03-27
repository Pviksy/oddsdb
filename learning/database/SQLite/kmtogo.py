import logging
from bs4 import BeautifulSoup
import requests
import lxml
import time


def get(race):
    global url
    if race == 'Stage 7 (Volta a Catalunya 2023)':
        url = 'https://www.procyclingstats.com/race/volta-a-catalunya/2023/stage-7/live'
    elif race == 'Gent-Wevelgem 2023':
        url = 'https://www.procyclingstats.com/race/gent-wevelgem/2023/result/live'
    else:
        return None

    req = requests.get(url)
    html = req.content

    soup = BeautifulSoup(html, 'lxml')

    area = soup.find('li', class_='kmtogo')

    km = area.findNext('div').findNext('div')

    return str(km.text)
