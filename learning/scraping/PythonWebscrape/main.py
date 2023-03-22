from bs4 import BeautifulSoup
import lxml
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

URL = "https://www.unibet.dk/betting/sports/drill-down/cycling"

PATH = "C:\\Users\\pvikp\\Dropbox\\2-semester\\Programmering\\Python\\chromedriver.exe" # or ./chromedriver (idk)
driver = webdriver.Chrome(PATH)
driver.get(URL)

time.sleep(1)
driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()  # allow cookies

time.sleep(1)
elems = driver.find_elements(By.CLASS_NAME, "KambiBC-drill-down-navigation__tree-item")

for i in elems:
    s = i.get_attribute("innerHTML")
    s1 = "data-path="
    s2 = "data-touch-feedback="
    print(s[s.index(s1) + len(s1): s.index(s2)])

time.sleep(3)

# upon entering event page - example url: https://www.unibet.dk/betting/sports/event/1019084858
time.sleep(1)
driver.find_element(By.CLASS_NAME, "KambiBC-react-collapsable-container__show-more").click()  # expand list

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
area = soup.find('div',
                 class_='KambiBC-outcomes-list KambiBC-outcomes-list--layout-labels-column-and-headers KambiBC-outcomes-list--columns-2')

riderList = [rider.text
             for rider in area.find_all('span', class_='KambiBC-outcomes-list__label')]

oddsList = [odds.text
            for odds in area.find_all('div', class_='OutcomeButton__Odds-sc-lxwzc0-6 gKPYii')]

res = {riderList[i]: oddsList[i] for i in range(len(riderList))}

print(res)

# print(riderList)
# print(oddsList)


# riderList = [rider.text
#             for rider in area.find_all('span', class_='gl-ParticipantBorderless_Name')]

# oddsList = [odds.text
#            for odds in area.find_all('span', class_='gl-ParticipantBorderless_Odds')]


# print(riderList)
# print(oddsList)

# print(soup.prettify())
