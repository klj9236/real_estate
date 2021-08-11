
# this is the "app/real_estate.py" file
#conda create -n realestate-env python=3.8 # (first time only)
#conda activate realestate-env

#pip install -r requirements.txt

import requests
import pandas as pd

from dotenv import load_dotenv
import os

api_key = os.environ.get("USREALESTATE_API_KEY")

url = "https://us-real-estate.p.rapidapi.com/sold-homes"


querystring = {"state_code": input("State Initials:"),"city": input("City:"),"property_type": "single_family","limit": input("Limit:"),"offset":"0","sort":"sold_date"}



headers = {
    'x-rapidapi-key': "7aff1b2018msh8e6327ddeadeee1p1debe6jsnece1277059fc",
    'x-rapidapi-host': "us-real-estate.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
#print(type(response.text))

r = response.text

import json

from pprint import pprint

parsed_reponse = json.loads(r)
print(type(parsed_reponse))
pprint(parsed_reponse)

quit()
from pandas import DataFrame

clean_list = []
for item in d["data"]["results"]:
  # print(item["listing_id"])
  
  
  clean_item = {
      "listing_id":item["listing_id"],
      "lat":item["location"]["address"]["coordinate"]['lat'],
      "long":item["location"]["address"]["coordinate"]['lon'],
      "property_type":item["description"]["type"],
      "street_address":item["location"]["address"]["line"],
      "city":item["location"]["address"]["city"],
      "state":item["location"]["address"]["state"],
      "zip_code":item["location"]["address"]["postal_code"],
      "square_feet":item["description"]["sqft"],
      "beds":item["description"]["beds"],
      "full_baths":item["description"]["baths_full"],
      "half_baths":item["description"]["baths_half"],
      "garage":item["description"]["garage"],
      "lot_size_sf":item["description"]["lot_sqft"],
      "year_built":item["description"]["year_built"],
      "list_price":item["list_price"],
      "sold_price":item["description"]["sold_price"],
      "list_date":item["list_date"],
      "sold_date":item["description"]["sold_date"],
      "primary_phot_url":item["primary_photo"]["href"],
      "url_photo_1":None,
      "url_photo_2":None,
      "url_photo_3":None,
      "url_photo_4":None,
      "url_photo_5":None,
      
  }

  try:
    clean_item["url_photo_1"] = item["photos"][0]["href"]
  except IndexError:
    pass
  
  try:
    clean_item["url_photo_2"] = item["photos"][1]["href"]
  except IndexError:
    pass

  try:
    clean_item["url_photo_3"] = item["photos"][2]["href"]
  except IndexError:
    pass

  try:
    clean_item["url_photo_4"] = item["photos"][3]["href"]
  except IndexError:
    pass

  try:
    clean_item["url_photo_5"] = item["photos"][4]["href"]
  except IndexError:
    pass

  clean_list.append(clean_item)

df = DataFrame(clean_list)

df.to_csv("home_price_results.csv")

print(df)