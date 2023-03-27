import datetime
import json
import requests
import db
import time
import logging
import tabulate
import kmtogo
import req


def get_odds():
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    response = req.make_request()

    data = response.json()

    odds_changed = 0
    events = data['events']

    for event in events:
        race = event['event']['englishName']
        km_to_go = kmtogo.get(race)

        bet_offers = event['betOffers']

        for bet_offer in bet_offers:
            outcomes = bet_offer['outcomes']

            for outcome in outcomes:
                rider = outcome['englishLabel']
                size = (outcome['odds'] / 1000).__str__()

                entry = (None, 'Unibet', race, rider, size, now, km_to_go)

                # previous entry in db with the same rider and race name
                prev = db.select_entry(entry)
                if prev is not None:
                    prev_race = prev[2]
                    prev_rider = prev[3]
                    prev_size = str(prev[4])

                    # should print if any odds have changed since the previous entry of the same rider and race
                    if race == prev_race and rider == prev_rider and size != prev_size:
                        odds_changed += 1  # count for every time an entry changes odds

                        db.insert(entry)  # if odds changed, insert new entry now

                        db.select_entries(entry)  # show offers with odds that have changed (testing)

    print("Odds changed:", str(odds_changed))
    logging.info("Odds changed: " + str(odds_changed))


get_odds()

#updates = 0
#while True:
#    updates += 1
#    get_odds()
#    time.sleep(600)

# db.table_of('Stage 5 (Volta a Catalunya 2023)')
# db.table_of('Brugge-De Panne 2023')

# db.table_of('Paris - Roubaix 2023')
