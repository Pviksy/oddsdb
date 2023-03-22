import json
import requests
import pyodbc as pyodbc
import datetime
import Entities

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-8KEOEI7\\SQLEXPRESS'
DB_NAME = 'OddsOnly1'

conn = pyodbc.connect('Driver=' + DRIVER_NAME + ';'
                                                'Server=' + SERVER_NAME + ';'
                                                                          'Database=' + DB_NAME + ';'
                                                                                                  'Trusted_Connection=yes;')

cursor = conn.cursor()

url = "https://eu-offering-api.kambicdn.com/offering/v2018/ubdk/listView/cycling/all/all/all/competitions.json"

querystring = {"lang": "da_DK", "market": "DK", "client_id": "2", "channel_id": "1", "ncid": "1675880965142",
               "useCombined": "true"}

payload = ""
headers = {
    "authority": "eu-offering-api.kambicdn.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "da-DK,da;q=0.9",
    "origin": "https://www.unibet.dk",
    "referer": "https://www.unibet.dk/",
    "sec-ch-ua": "^\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

#response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
#data = response.json()

file = open("unibet.json", "r")
example = file.read()
file.close()
data = json.loads(example)

events = data['events']

prev_odds = []


def get_odds():
    for event in events:
        print(event['event']['englishName'])

        race_name = event['event']['englishName']

        now = datetime.datetime.now()
        datetime_string = now.strftime("%Y/%m/%d %H:%M:%S")

        betOffers = event['betOffers']

        for betOffer in betOffers:
            outcomes = betOffer['outcomes']

            for outcome in outcomes:
                size = (outcome['odds'] / 1000).__str__()
                rider_name_arr = outcome['englishLabel'].split(",")

                first_name = rider_name_arr[1][:0] + "" + rider_name_arr[1][1:]
                last_name = rider_name_arr[0]

                rider_name = first_name + " " + last_name

                # cursor.execute("INSERT INTO [odds] VALUES ('" + race_name.replace("'", " ") + "', '" + rider_name.replace("'", " ") + "', '" + size + "', '" + datetime_string + "');")
                # conn.commit()

                this_odds = Entities.Odds(race_name, rider_name, size)

                prev_odds.append(this_odds)
                this_odds.toString()

                # print(event['event']['englishName'] + " - " + rider_name.replace("'", " ") + " - " + size + " - " + datetime_string)


for event in events:
    print("       name:", event['event']['name'])
    print("englishName:", event['event']['englishName'])
    print("   homeName:", event['event']['homeName'])
    print("      group:", event['event']['group'])
    print()
