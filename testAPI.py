import requests


## GET https://api.fortnitetracker.com/v1/profile/{platform}/{epic-nickname}
## TRN-Api-Key: 31b3b777-f324-4650-8719-69652a8fa491

## Create URL & Header with valid token, and valid user
## URL = 'https://api.fortnitetracker.com/v1/profile/psp/MBA_53'
URL = 'https://api.fortnitetracker.com/v1/profile/{}/{}'
headers = {'TRN-Api-Key' : '31b3b777-f324-4650-8719-69652a8fa491'}

## Defautl Settings
keysForMainStats = ['Score', 'Matches Played','Wins', 'Kills', 'Time Played', 'Avg Survival Time']
platforms = ['psn', 'xbl', 'pc']
name = 'MBA_53'

## Build stats_dict
#response = requests.get(URL.format(platforms[0], name.strip()), headers=headers)
URL1 = URL.format(platforms[0], name.strip())
URL2 = 'https://api.fortnitetracker.com/v1/store'
URL3 = 'https://api.fortnitetracker.com/v1/challenges'
URL4 = 'https://fortniteinsider.com/category/fortnite-news/'
response = requests.get(URL2, headers=headers)
print(response.text)
#response_json = response.json()