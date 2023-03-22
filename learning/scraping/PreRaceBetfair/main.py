from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import lxml
import time
import re

path = "C:\\Users\\pvikp\\Dropbox\\2-semester\\Programmering\\Python\\chromedriver.exe"



#driver = webdriver.Chrome(path)
#driver.get(URL)
#time.sleep(3)
#driver.find_element(By.ID, "onetrust-accept-btn-handler").click()  # allow cookies

URL = "https://www.betfair.com/sport/cycling"
req = requests.get(URL)

soup = BeautifulSoup(req.content, 'lxml')
area = soup.find('div', class_='coupon-list')

events = {"Race": [], "URL": []};

for a in area.find_all('a', href=True):
    if '/sport/cycling' in a['href']:
        events["URL"].append('https://www.betfair.com' + a['href'])  # gets urls for all individual cycling events
        events["Race"].append(a['title'])  # gets title - doesnt seem the perfect solution

print(events)


#def scrape(event):
#    print(events.get("URL"))
#    driver.get(events.get("URL"))
#
#    time.sleep(1)
#    riders = driver.find_elements(By.CLASS_NAME, "runner-name")
#    odds = driver.find_elements(By.CLASS_NAME, "ui-runner-price")
#
#    res = {riders[i].get_attribute("innerHTML"): odds[i].get_attribute("innerHTML").replace("\n", "") for i in
#           range(len(riders))}
#
#    for key in res:
#        print(key, ':', res[key])


#for event in events:
#    #scrape(event)
#    print(events)
