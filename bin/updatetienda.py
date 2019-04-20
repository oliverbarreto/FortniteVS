import requests

## Create URL & Header with valid token, and valid user
headers = {'TRN-Api-Key' : '31b3b777-f324-4650-8719-69652a8fa491'}

## Build stats_dict
URL = 'https://api.fortnitetracker.com/v1/store'
response = requests.get(URL, headers=headers)
print(response.text)
#response_json = response.json()