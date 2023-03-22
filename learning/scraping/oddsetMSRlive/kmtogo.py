import logging
from bs4 import BeautifulSoup
import requests
import lxml
import time

url = "https://www.procyclingstats.com/race/milano-sanremo/2023/result/live"


def get():
    req = requests.get(url)
    html = req.content

    soup = BeautifulSoup(html, 'lxml')

    area = soup.find('li', class_='kmtogo')

    km = area.findNext('div').findNext('div')

    return str(km.text)
