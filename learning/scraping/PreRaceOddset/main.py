from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import lxml
import time
import re



#driver = webdriver.Chrome('./chromedriver')
#driver.get(URL)
#time.sleep(3)
#driver.find_element(By.ID, "ensSave").click()  # allow cookies
#html = driver.page_source

URL2 = "https://danskespil.dk/oddset/sports/competition/19794/cykling/international/international-tour-de-france/outrights?outrightseventid=6221150"
URL = "https://danskespil.dk/oddset/sport/660/cykling/matches"
req = requests.get(URL)
print(req.text)

soup = BeautifulSoup(req.content, 'lxml')

#area = soup.find('div', class_='heading heading--timeband heading--timeband--outrights')

events = []

#for a in area.find_all('a', href=True):
#    if 'eventid=' in a['href']:
#        events.append('https://danskespil.dk' + a['href'])  # gets urls for all individual cycling events

#print(soup.prettify())

print(events)

#def scrape(event):
#    driver.get(event)
#
#    time.sleep(1)
#    driver.find_element(By.CLASS_NAME, "market__body__more-outcomes__button--show-more").click()  # expand list
#
#    time.sleep(1)
#    riders = driver.find_elements(By.CLASS_NAME, "button--outcome__text-title")
#    odds = driver.find_elements(By.CLASS_NAME, "button--outcome__price")
#
#    res = {riders[i].get_attribute("innerHTML"): odds[i].get_attribute("innerHTML") for i in
#           range(len(riders) - 4)}  # -4 or it grabs unwanted data
#
#    for key in res:
#        print(key, ':', res[key])


#for event in events:
#    scrape(event)
