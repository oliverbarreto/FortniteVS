import requests
import os
import json
from datetime import datetime


## Create URL & Header with valid token, and valid user
headers = {'TRN-Api-Key' : '31b3b777-f324-4650-8719-69652a8fa491'}


## Get current items from API 
URL = 'https://api.fortnitetracker.com/v1/store'
response = requests.get(URL, headers=headers)
response_json = response.json()
response_text = response.text
##print(response_json)
#response_json = response.json()

## Create JSON Object with current items in the store
today = datetime.now().strftime("%Y-%m-%d")
store_items = {
  "date": today,
  "store_items": response_json
}

## Write results data on file for Current Items in the store
file_path = "static/data/data_tienda.py"

if not os.path.exists(file_path):
  with open (file_path, "w") as f:
    f.close()

with open (file_path, "w") as f:
  content = f.write(json.dumps(store_items))
  f.close()


## Create backup JSON object from file 
file_path = "static/data/data_tienda_old.py"

if not os.path.exists(file_path):
  with open (file_path, "w") as f:
    f.close()

content_json = []
with open (file_path, "r") as f:
  content_text = f.read()

  if not len(content_text) == 0:
    content_json = json.loads(content_text)
  
  values = []
  for item in content_json:
    values.append(item['date'])
  
  if store_items['date'] not in values:  
    # print(content_json.__class__.__name__)
    content_json.append(store_items)
  
  with open (file_path, "w") as f:
    content = f.write(json.dumps(content_json))
    f.close()
