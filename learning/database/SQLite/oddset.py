import requests

def get_odds():
    url = "https://content.sb.danskespil.dk/content-service/api/v1/q/event-list"

    querystring = {"eventSortsIncluded": "TNMT", "includeChildMarkets": "true", "drilldownTagIds": "19783"}

    headers = {
        "cookie": "visid_incap_2245573=yzORqaKYTT2Y+ZpxcVNgevS0F2MAAAAAQUIPAAAAAAA24oACRV/W7E6sG76nad/p; DANSKESPIL_ENSIGHTEN_PRIVACY_MODAL_LOADED=1; _p2s_uvi=544df011.7303837634601229.1662498037809; DS_ENS_Version=2; DANSKESPIL_ENSIGHTEN_PRIVACY_Version=2; _ga=GA1.2.1878448640.1662498038; ensClientID=1662498038247.7ux2wuk5; visid_incap_2245565=teorQiGKSKymlZUInVb9R/W0F2MAAAAAQUIPAAAAAACeTXGEkOtsH5cBLte+48Hd; visid_incap_2245568=NbhYJ0v0S7+VP2KRAVzyDva0F2MAAAAAQUIPAAAAAADn5zicr9BrZkyINaqW6W57; DANSKESPIL_ENSIGHTEN_PRIVACY_Statistiske=1; DANSKESPIL_ENSIGHTEN_PRIVACY_Marketing=1; DANSKESPIL_ENSIGHTEN_PRIVACY_Funktionelle=1; DANSKESPIL_ENSIGHTEN_PRIVACY_Nodvendige=1; DANSKESPIL_ENSIGHTEN_PRIVACY_MODAL_VIEWED=1; visid_incap_2245569=zM/OSjJ8QC2KZojVL1OFfQi1F2MAAAAAQUIPAAAAAABaqD3liJBGQijzszd+1Ypv; visid_incap_2245574=zDHA922aT6GByKiFMaiCUhu1F2MAAAAAQUIPAAAAAADjh49ewSad0v4aLpgcFmlS; _hjid=4ed020a0-8278-4a6b-85d7-70494d3cc3aa; _hjSessionUser_742515=eyJpZCI6IjdiOTNkZWUzLWRkY2QtNWYyMy04ZmRmLTBlNmRlZTU4MzM2OSIsImNyZWF0ZWQiOjE2NjI1Nzc4NzQ1NTcsImV4aXN0aW5nIjp0cnVlfQ==; incap_ses_1613_2245573=LqF4Mi5np264MaTHKYdiFhZxDGQAAAAAfOZN4gVVD/M2ZCJiCtInTg==; ensSessionID=1678536985384.3dpdn01h; incap_ses_1613_2245565=LDggG4V1Dl2HMqTHKYdiFhhxDGQAAAAA68ofFkLN11L/jr7L2X8dog==; incap_ses_1613_2245568=+/eWPe+F0APCNKTHKYdiFhlxDGQAAAAA331ohpvuTxzEcufnYQbcYg==",
        "authority": "content.sb.danskespil.dk",
        "accept": "application/json",
        "accept-language": "da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7,eu;q=0.6",
        "content-type": "application/json",
        "origin": "https://danskespil.dk",
        "referer": "https://danskespil.dk/",
        "sec-ch-ua": "^\^Chromium^^;v=^\^110^^, ^\^Not",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "x-accept-language": "da-DK",
        "x-ob-channel": "I"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    eventlist = data['data']['events']

    for event in eventlist:
        if event['id'] == '6735058':
            markets = event['markets']

            for market in markets:
                outcomes = market['outcomes']

                for outcome in outcomes:
                    name = outcome['name']

                    prices = outcome['prices']

                    for price in prices:
                        size = price['decimal']

                        print(size, name)
