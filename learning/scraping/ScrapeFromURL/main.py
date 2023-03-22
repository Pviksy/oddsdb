from bs4 import BeautifulSoup
import lxml
import requests




with open('valenciana2.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

race = soup.find('div', class_='sph-EventHeader_Label').text

area = soup.find('div', class_='gl-MarketGroup_Wrapper src-MarketGroup_Container')

riderList = [rider.text
             for rider in area.find_all('span', class_='gl-ParticipantBorderless_Name')]

oddsList = [odds.text
            for odds in area.find_all('span', class_='gl-ParticipantBorderless_Odds')]

print(race)
print(riderList)
print(oddsList)

#print(soup.prettify())