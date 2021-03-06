
# Imports  
import requests
import json
from pprint import pprint
from pandas import DataFrame
from dotenv import load_dotenv
import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt

datetime.datetime.now()

load_dotenv()

api_key = os.getenv("USREALESTATE_API_KEY")

url = "https://us-real-estate.p.rapidapi.com/sold-homes"

# Old Input querystring = {"state_code":"NY","city":"Latham","location":"12110","limit":"20","offset":"0","sort":"sold_date"}

querystring = {"state_code": input("State Initials:"),"city": input("City:"),"location": input("Zip Code"),"property_type":"multi_family","limit":"20","offset":"0","sort":"sold_date","expand_search_radius":"1"}

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "us-real-estate.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

r = response.text
parsed_response = json.loads(r)

clean_list = []
for item in parsed_response["data"]["results"]:

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
      "primary_phot_url":None,
      "url_photo_1":None,
      "url_photo_2":None,
      "url_photo_3":None,
      "url_photo_4":None,
      "url_photo_5":None,
      
  }

  try:
    clean_item["primary_phot_url"] = item["primary_photo"]["href"]
  except:
    pass

  try:
    clean_item["url_photo_1"] = item["photos"][0]["href"]
  except:
    pass
  
  try:
    clean_item["url_photo_2"] = item["photos"][1]["href"]
  except:
    pass

  try:
    clean_item["url_photo_3"] = item["photos"][2]["href"]
  except:
    pass

  try:
    clean_item["url_photo_4"] = item["photos"][3]["href"]
  except:
    pass

  try:
    clean_item["url_photo_5"] = item["photos"][4]["href"]
  except:
    pass

  clean_list.append(clean_item)

df = DataFrame(clean_list)

msp = df[['sold_price']].div(df.square_feet, axis =0)

mspr = msp.rename(columns = {'sold_price':'median_price_per_sf'})

frames = [df , mspr]

result = pd.concat(frames, axis=1)

print(result)
result.to_csv(f"home_price_results_{datetime.datetime.now()}.csv")

import seaborn as sns

ax = sns.boxplot( x='median_price_per_sf', data = result, linewidth="2", palette = "muted")
ax = sns.swarmplot( x='median_price_per_sf', data = result, color = ".15")
plt.savefig(f"median_sf_values_{datetime.datetime.now()}.pdf")


import plotly.express as px
fig = px.scatter_mapbox(result, lat="lat", lon="long", color="median_price_per_sf", size="square_feet",
                  color_continuous_scale=px.colors.sequential.Emrld, size_max=30, zoom = 10,
                  mapbox_style="carto-positron")
fig.show()

fig.write_image("housing_map.pdf")