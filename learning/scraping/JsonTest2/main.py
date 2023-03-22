import json

with open("unibet.json", "r") as f:
    data = json.load(f)

for rider in data:
    name = rider['name']
    price = rider['price']
    first_name = ''.join(filter(str.isalpha, name))
    last_name = ''.join(filter(str.isalpha, name[::-1]))
    last_name = last_name[::-1]
    print(f"{first_name.capitalize()} {last_name.capitalize()}: {price:.2f}")