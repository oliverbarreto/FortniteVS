# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, redirect, request, session, flash, make_response
import requests
import os
import json
from datetime import datetime,timedelta

##from data import Articles, StoreItems, Challenges
## from data_tienda import StoreItems
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
## ARTICULOS NOTICIAS
Articulos = Articles()


## ITEMS TIENDA
def dummyStore_Items():
  file_path = "static/data/data_tienda.py"
  if os.path.exists(file_path):
    with open (file_path, "r") as f:
      content = f.read()
      content_json = json.loads(content)["store_items"]
      #print(content_json)
      f.close()
      
      return content_json

  else:
    ## print("EMPTY data_tienda.py")
    return []

def StoreItems():
  store_items = dummyStore_Items()
  
  return store_items



Store_items = StoreItems()


#Retos = Challenges()

## ----------------------------------------------------------------------------
## Custom Methods
## ----------------------------------------------------------------------------
def stringIsEmpty(string):
  result = 0
  for char in string:
    if char == " ":
      result += 1     # same as result = result + 1
  if result == len(string):
    return True
  else:
    return False

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

def generateVS(players):

  '''
  versus = {
      'vs':  {
        'wins': {'label':'wins', 'player':'Oliver', 'value': 5376},
        'kills': {'label':'kills', 'player':'ana', 'value': 1061670},
        'k/d': {'label': 'k/d', 'player':'miguel', 'value': 10.29},
        'games': {'label': 'partidas', 'player':'raul', 'value': 15762},
        'score': {'label': 'score', 'player':'pepe', 'value': 6084158}
      }
    }
  '''
  
  versus = {
      'vs':  {
        'Wins': {'label':'wins', 'player':'', 'value': 0},
        'Kills': {'label':'kills', 'player':'', 'value': 0},
        'K/d': {'label': 'k/d', 'player':'', 'value': 0},
        'Matches Played': {'label': 'partidas', 'player':'', 'value': 0},
        'Score': {'label': 'score', 'player':'', 'value': 0}
      }
    }

  for player in players:
    for key in keysForMainStats:
      player_name = player['name']
      label = key
      player_value = 0
      versus_value = float(versus['vs'][key]['value'])

      if key == 'K/d':
        player_value = float(player['lifetimeStats'][key])
      else:
        player_value = float(player['lifetimeStats'][key].replace(',', ''))

      ##print(f'Player: {player_name} -> {label}: {player_value}({type(player_value)})')
      ##versus.vs.Wins.player

      if versus_value == player_value:
        versus['vs'][key]['player'] = f"{versus['vs'][key]['player']} & {player_name}"
        versus['vs'][key]['value'] = f"{player_value}".replace('.0', '')

      if versus_value < player_value or versus_value == '':
        versus['vs'][key]['player'] = f"{player_name}"
        versus['vs'][key]['value'] = f"{player_value}".replace('.0', '')


  return versus

###############################################################################
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


###############################################################################
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


    ## If we remove a player from versusl.html using the x button (post send with form on button)
    if "remove" in request.form:
      removePlayerName = request.form.get("remove")
      
      for index, player in enumerate(players):
        if player['name'] == removePlayerName:
          del players[index]
          session['players'] = players

      versus = None
      if len(players) == 0:
        items = weeklyItems()
        return render_template('index.html', articulos=Articulos, daily_items=items)
      if len(players) > 1:
        versus = generateVS(players=players)

      return render_template('vs.html', players=players, versus=versus)


    ## If we search for a player from index.html or versus.html search box form
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
          session['players'] = players


    versus = None
    if len(players) > 1:
      versus = generateVS(players=players)

    return render_template('vs.html', players=players, versus=versus)

  elif request.method == "GET":  
    items = weeklyItems()
    return render_template('index.html', articulos=Articulos, daily_items=items)


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

@app.route('/update/updatetienda')
def updatetienda():
  ## Get current items from API 
  URL = 'https://api.fortnitetracker.com/v1/store'
  response = requests.get(URL, headers=headers)
  response_json = response.json()
  response_text = response.text
  
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
    f.write(json.dumps(store_items))
    ##print(store_items)

    f.close()

  Store_items = StoreItems()




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
    
  
  return redirect(url_for('index'))




## ----------------------------------------------------------------------------
## website contact & legal info 
## ----------------------------------------------------------------------------
@app.route('/contacto')
def contacto():
  return  render_template('contacto.html')

@app.route('/privacidad')
def politicadeprivacidad():
  return  render_template('politica_privacidad.html')

@app.route('/condiciones')
def condicionesdeservicio():
  return  render_template('condiciones_servicio.html')

@app.route('/politicacookies')
def politicacookies():
  return  render_template('politica_cookies.html')


@app.route('/robots.txt/')
def robots():
  ## LIVE VERSION ####
  ## return("User-agent: *\nDisallow: /register/\nDisallow: /login/\nDisallow: /donation-success/")

  ###### DEV VERSION #####
  return("User-agent: *\nDisallow:")


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=(datetime.now() - timedelta(days=7)).date().isoformat()
      # static pages
      for rule in app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0:
              pages.append(
                           ["http://fortnitevs.herokuapp.com"+str(rule.rule),ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      #print(sitemap_xml)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"    
    
      return response
    except Exception as e:
        return(str(e))



## ----------------------------------------------------------------------------
## Main
## ----------------------------------------------------------------------------
if __name__ == '__main__':
  app.run(debug=True, port=5000)



