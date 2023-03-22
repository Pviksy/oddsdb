import requests
from utility import service
from entities import odds
from database import db


def request_data():
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

    return requests.request("GET", url, data=payload, headers=headers, params=querystring)


def get_odds():
    entries = []

    response = request_data()

    data = response.json()

    odds_changed = 0
    events = data['events']

    for event in events:
        race = event['event']['englishName']
        live_or_pre = event['event']['state']  # is called "NOT_STARTED" when pre

        bet_offers = event['betOffers']

        for bet_offer in bet_offers:
            outcomes = bet_offer['outcomes']

            for outcome in outcomes:
                rider = outcome['englishLabel']
                size = (outcome['odds'] / 1000).__str__()

                timestamp = service.current_time()

                # entry = (None, 'Unibet', race, rider, size, timestamp)
                new_entry = odds.Odds(None, 1, 'event_id', 'team_id', 'rider_id', size, 'type', timestamp)

                prev_entry = db.find_prev_entry(new_entry)
                if prev_entry is not None:
                    prev_race = prev_entry[2]
                    prev_rider = prev_entry[3]
                    prev_size = str(prev_entry[4])

                    if race == prev_race and rider == prev_rider and size != prev_size:
                        entries.append(new_entry)

                        # do logging
    return entries
