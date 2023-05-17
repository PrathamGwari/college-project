import requests
import time
import pandas as pd
from datetime import datetime as dt

url = "https://astrology4.p.rapidapi.com/panchang"

# querystring = {"datetime":"2018-02-01T00:00:00+05:30","ayanamsa":"1","coordinates":"28,77"}

headers = {
    "Authorization": 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9. _y9sHF8OwZQzxFyk1ZXOUOZ',
    "X-RapidAPI-Key": "def04cc273msha25f027e1f20c12p1c0f83jsnd69d20433648",
    "X-RapidAPI-Host": "astrology4.p.rapidapi.com"
}

td = pd.date_range("2021-06-11", "2022-01-01")

df = pd.DataFrame(columns=['Paksha', "Tithi", "Start", "End"])

for i in td:

    cur = str(i)[:10]
    querystring = {"datetime": str(
        cur+"T00:00:00+05:30"), "ayanamsa": "1", "coordinates": "28,77"}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    print(response.text)
    a = response.json()

    for i in a["data"]['tithi']:
        df.loc[len(df.index)] = [i["paksha"], i["name"], i["start"], i["end"]]
        print(i)
    df.to_csv("part2.csv")

    time.sleep(30)

df.to_csv("part2.csv")
print("end")
