
from flask import Flask, render_template, url_for, redirect, request, session, flash
import requests
import os


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
response = requests.get(URL.format(platforms[0], name.strip()), headers=headers)
response_json = response.json()

print(response_json)