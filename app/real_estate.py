
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

querystring = {"state_code": input("State Code:"),"city": input("City:"),"limit": input("Limit:"),"offset":"0","sort":"sold_date"}

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
print(parsed_reponse)

#soldhomes_df=pd.DataFrame.from_dict(parsed_reponse)

#df = pd.DataFrame(soldhomes_df, columns=["price_min", "price_max"])
#for col in soldhomes_df:
    #print(col)
#print(soldhomes_df.head(10))

#print(soldhomes_df)