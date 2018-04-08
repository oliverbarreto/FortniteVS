# -*- coding: utf-8 -*-

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


## App & Config
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or os.urandom(24)


## Models
'''
class PlayerStats():

  def __init__(self, name, platform, stats):
    self.name = name
    self.platform = platform
    self.stats = stats

    def jsonStr():
      return {
        'name' : self.name,
        'platfomr': self.platform,
        'stats': self.stats
      }

    def __repr__(self):
        return "PlayerStats({}, {}, {})".format(self.name, self.platform, self.stats)
'''

## Custom Methods
def generateVS(players):

  vs = {}
  keys = ['Kills', 'Score', 'Wins']

  for i, player in enumerate(players):
    player_stats = statsForPlayerSessionData(player)
    player_name = player['name']

    player_keys = list(player.keys())
    stats_keys = list(player_stats.keys())

    ## if vs doesn't exist: create the structure with this players data (first player)
    if vs == {}:
      ## print('** Creating new VS dict')
      for key in keys:
        value = dict()
        value['name'] = player_name
        value['value'] = player_stats[key]
        vs[key] = value
      ## print('VS -> {}'.format(vs))

    ## if vs exists: compare current data with current player
    else:
      ## print('** Updating VS dict')
      for key in keys:

        player_value = int(player_stats[key].replace(',' , ''))
        vs_value = int(vs[key]['value'].replace(',' , ''))

        if player_value > vs_value:
          value = dict()
          value['name'] = player_name
          value['value'] = str(player_value)
          vs[key] = value

        elif  player_value == vs_value:
          new_name = '{} & {}'.format(vs[key]['name'], player_name)
          value = dict()
          value['name'] = new_name
          value['value'] = str(player_value)
          vs[key] = value

      ## print('VS -> {}'.format(vs))
  return vs

def statsForPlayerSessionData(player):
  ''' Returns a dictionary winth the stats for a player extracted from a session player object
  '''
  stats_dict = {}

  if 'stats' in player:
    stats_dict = player['stats']

  return stats_dict


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



## Routes & Views
@app.route('/', methods=['GET', 'POST'])
def index():

  players = []

  if request.method == 'POST':


    ## Check session data, and build players array if any, empty array if not
    players = playersInSession()

    name = request.form.get('playerName')
    platform = request.form.get('platform')


    ## Check valid names
    if not name or name == "":
      flash("Please enter a valid player name 😎")
      vs = {}
      if len(players) > 0:
        session['players'] = players

      if len(players) > 1:
        vs = generateVS(players)

      return render_template('index.html', players=players, vs=vs)


    ## Check if player is already in the session, and if not, add current player to actual player list before passing
    playersNames = namesOfPlayersInArray(playersInSession())

    if name not in playersNames:

      ## Build stats_dict
      response = requests.get(URL.format(platform, name.strip()), headers=headers)
      response_json = response.json()

      ## Build Stats dictionary for Player
      lifeTimeStatsDataForPlayer = []

      if response_json:
        if response_json == {'error': 'Player Not Found'}:
          flash("Player Not Found 😳")

          vs = {}
          if len(players) > 0:
            session['players'] = players

          if len(players) > 1:
            vs = generateVS(players)

          return render_template('index.html', players=players, vs=vs)

        lifeTimeStatsDataForPlayer = response_json['lifeTimeStats']


      ## Create current Player object
      player = {
        'name' : name,
        'platform' : platform,
        'stats' : statsForPlayer(lifeTimeStatsDataForPlayer)
      }

      players.append(player)

    else:
      players = playersInSession()


  ## Check if any players to pass, then pass them
  vs = {}
  if len(players) > 0:
    session['players'] = players

  if len(players) > 1:
    ## print('calculating VS Stats')
    ## print(players)
    vs = generateVS(players)



  return render_template('index.html', players=players, vs=vs)



@app.route('/clear')
def clear():
  ##session.pop('players', None)
  session.clear()
  return redirect(url_for('index'))


## Main
if __name__ == '__main__':
  app.run(debug=True, port=5000)


