# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, redirect, request, session, flash
import requests
import os

##from data import Articles, StoreItems, Challenges
from data_tienda import StoreItems
from data_noticias import Articles


## ----------------------------------------------------------------------------
## API SETUP
## GET https://api.fortnitetracker.com/v1/profile/{platform}/{epic-nickname}
## TRN-Api-Key: 31b3b777-f324-4650-8719-69652a8fa491
## ----------------------------------------------------------------------------
##
## Create URL & Header with valid token, and valid user
## URL = 'https://api.fortnitetracker.com/v1/profile/psp/MBA_53'
URL = 'https://api.fortnitetracker.com/v1/profile/{}/{}'
headers = {'TRN-Api-Key' : '31b3b777-f324-4650-8719-69652a8fa491'}

## Defautl Fortnite API Settings
## keysForMainStats = ['Score', 'Matches Played','Wins', 'Kills', 'K/d'. 'Top 5s', 'Top 3s', 'Top 6s'. 'Top 10', 'Top 12s', 'Top 25s']
keysForMainStats = ['Score', 'Matches Played','Wins', 'Kills', 'K/d']
platforms = ['psn', 'xbl', 'pc']


## ----------------------------------------------------------------------------
## App & Config
## ----------------------------------------------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or os.urandom(24)


## ----------------------------------------------------------------------------
## Dummy DATA
## ----------------------------------------------------------------------------
Articulos = Articles()
Store_items = StoreItems()
#Retos = Challenges()

## ----------------------------------------------------------------------------
## Custom Methods
## ----------------------------------------------------------------------------
def dailyItems():
    items = []

    for item in Store_items:
      if item['storeCategory'] == 'BRDailyStorefront':
        items.append(item)
    return items


def weeklyItems():
  items = []

  for item in Store_items:
    if item['storeCategory'] == 'BRWeeklyStorefront':
      items.append(item)
  return items  

def stringIsEmpty(string):
  result = 0
  for char in string:
    if char == " ":
      result += 1     # same as result = result + 1
  if result == len(string):
    return True
  else:
    return False

def statsForPlayer(player_data):
  ''' Returns a dictionary with the stats for a player
  '''
  stats_dict = {}

  for stat in player_data:
    key = stat['key']

    if key in keysForMainStats:
      stats_dict[key] = stat['value']

  return stats_dict

def namesOfPlayersInArray(players):
  ''' Returns an array of strings with all the names of an array of players
  '''
  playerNames = []

  for p in players:
    playerNames.append(p['name'])

  return playerNames

def playersInSession():
  ''' returns an array of players, if session exists and has players in it
  '''
  if 'players' in session:
    players = session['players']

    if players:
      return players

  else:
    return []


## ----------------------------------------------------------------------------
## API Interaction
## ----------------------------------------------------------------------------
def getPlayerLifeTimeStats(name, platform):
  ## Build stats_dict
  response = requests.get(URL.format(platform, name.strip()), headers=headers)
  response_json = response.json()

  ## Build Stats dictionary for Player
  lifeTimeStatsDataForPlayer = []

  if response_json:
    if response_json == {'error': 'Player Not Found'}:
      lifeTimeStatsDataForPlayer = []
    else:
      lifeTimeStatsDataForPlayer = statsForPlayer(response_json['lifeTimeStats'])

  return lifeTimeStatsDataForPlayer


## ----------------------------------------------------------------------------
## DELETE ON PRODUCTION
## ----------------------------------------------------------------------------
@app.route('/test')
def test():
  return  render_template('test.html')


## ----------------------------------------------------------------------------
## Routes & Views
## ----------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
  #return render_template('vs.html', players=players, vs=vs)

  ## holds player's data
  players = []

  if request.method == "POST":
    ## Check session data, and build players array if any, empty array if not
    players = playersInSession()

    playerName = request.form.get("playerName")
    playerPlatform = request.form.get("platform")  

    ## Check for valid names: flashes if error, and returns the previous players array 
    if not playerName or playerName == "" or stringIsEmpty(playerName):
      flash("Por favor introduce un nombre de usuario válido 😎")

    else:
      ## If there are more players already in session object
      ## print("*********** SESION *************")
      ## print(players)

      if playerName not in namesOfPlayersInArray(players):

        ## Create current Player object if it doesn't exists already
        currentPlayerStats = getPlayerLifeTimeStats(name=playerName, platform=playerPlatform)

        if currentPlayerStats == []:
          flash("Jugador no encontrado 😳")

        else:
          player = {
            'name' : playerName,
            'platform' : playerPlatform,
            'lifetimeStats' : currentPlayerStats
          }

          players.append(player)
          ## print(player)
          session['players']= players


    return render_template('vs.html', playerName=playerName, playerPlatform=playerPlatform, players=players)

  elif request.method == "GET":  
    items = weeklyItems()
    return render_template('index.html', articulos=Articulos, daily_items=items)

@app.route('/contacto')
def contacto():
  return  render_template('contacto.html')

@app.route('/privacidad')
def politicadeprivacidad():
  return  render_template('politicadeprivacidad.html')

@app.route('/condiciones')
def condicionesdeservicio():
  return  render_template('condicionesdeservicio.html')

@app.route('/clear')
def clear():
  session.clear()
  return redirect(url_for('index'))

@app.route('/cuentaatras')
def cuentaatras():
  return  render_template('cuentaatras.html')

@app.route('/voyatenersuerte')
def voyatenersuerte():
  return  render_template('voyatenersuerte.html')


@app.route('/noticias')
def noticias():
  return  render_template('noticias.html', articulos=Articulos)

@app.route('/tienda')
def articulostienda():
  return render_template('tienda.html', daily_items=dailyItems(), weekly_items=weeklyItems())


## ----------------------------------------------------------------------------
## Main
## ----------------------------------------------------------------------------
if __name__ == '__main__':
  app.run(debug=True, port=5000)





