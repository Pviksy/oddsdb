import requests


def make_request():
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
