
import requests
import pandas as pd

url = "https://us-real-estate.p.rapidapi.com/sold-homes"

querystring = {"state_code":"NY","city":"Latham","location":"12110","limit":"20","offset":"0","sort":"sold_date"}

headers = {
    'x-rapidapi-key': "API key",
    'x-rapidapi-host': "us-real-estate.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

import json

from pprint import pprint

r = response.text
parsed_response = json.loads(r)

print(parsed_response)

results = pd.DataFrame.from_dict(parsed_response["data"]["results"])

display(results)

results.to_csv("results.csv", columns=["location", "description", "list_price"])
