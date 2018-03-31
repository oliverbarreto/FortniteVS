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
      return render_template('index.html', players=players)

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
          return render_template('index.html', players=players)

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
  if len(players) > 0:
    session['players'] = players

  return render_template('index.html', players=players)



@app.route('/clear')
def clear():
  ##session.pop('players', None)
  session.clear()
  return redirect(url_for('index'))


## Main
if __name__ == '__main__':
  app.run(debug=True, port=5000)


