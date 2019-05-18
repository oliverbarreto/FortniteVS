import os
import json
from datetime import datetime
from fortniteversus import db
import requests

## ----------------------------------------------------------------------------
## Dummy DATA
## ----------------------------------------------------------------------------
## ARTICULOS SECCIÓN NOTICIAS
def dummyNews_Items():
  file_path = "fortniteversus/static/data/data_noticias.py"
  if os.path.exists(file_path):
    with open (file_path, "r") as f:
      content = f.read()
      content_json = json.loads(content)
      #print(content_json)
      f.close()
      
      return content_json

  else:
    ## print("EMPTY data_noticias.py")
    return []

def NewsItems():
  news_items = dummyNews_Items()
  
  return news_items

# Noticias_items = NewsItems()



## ARITCULOS DE LA TIENDA
def dummyStore_Items():
  file_path = "fortniteversus/static/data/data_tienda.py"
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


def updatetiendadehoy():
  ## Get current items from API 
  URL = 'https://api.fortnitetracker.com/v1/store'
  headers = {'TRN-Api-Key' : '31b3b777-f324-4650-8719-69652a8fa491'}
  response = requests.get(URL, headers=headers)
  response_json = response.json()
    
  for item in response_json:
    manifest_id = int(item['manifestId'])
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Si no existe, creamos el registro del item
    # o... Si existe, pero es de otra fecha, creamos el registro del item
    count = StoreItem.query.filter_by(manifest_id=manifest_id).count()
    count_day = StoreItem.query.filter_by(date=today, manifest_id=manifest_id).count()
    if count == 0 or count_day == 0:
      store_item = StoreItem(manifest_id=manifest_id, name= item['name'], rarity=item['rarity'], image_url = item['imageUrl'], store_category=item['storeCategory'], vbucks=item['vBucks'])
      db.session.add(store_item)
      
      print("Committing to DB ...")
      db.session.commit()


def getStoreItems(store_items):
  items = []
  for store_item in store_items:
    item = store_item.to_dict()
    items.append(item)
  
  return items

'''
{"imageUrl": "https://cdn.thetrackernetwork.com/cdn/fortnite/B19C10921_large.png", 
"manifestId": 10921, 
"name": "Choppa", 
"rarity": "Quality", 
"storeCategory": "BRWeeklyStorefront", 
"vBucks": 1200}
'''


def dbStoreItems():
  today = datetime.now().strftime("%Y-%m-%d")
  if StoreItem.query.filter_by(date=today).count() == 0:
    updatetiendadehoy()
  
  todays_items = StoreItem.query.filter_by(date=today).all()
    
  return getStoreItems(store_items=todays_items)

def StoreItems():
  store_items = dbStoreItems()
  
  return store_items

def dailyItems():
    items = []

    for item in dbStoreItems():
      if item['storeCategory'] == 'BRDailyStorefront':
        items.append(item)
    return items

def weeklyItems():
  items = []

  for item in dbStoreItems():
    if item['storeCategory'] == 'BRWeeklyStorefront':
      items.append(item)
  return items  


## -------------------------------------------------------------------------------------------
## SQLAlchemy Models
## -------------------------------------------------------------------------------------------
'''
{
"imageUrl": "https://cdn.thetrackernetwork.com/cdn/xth/A489upload.png", 
"manifestId": 6494, 
"name": "Battle Pass Tiers", 
"rarity": "Quality", 
"storeCategory": "BRDailyStorefront", 
"vBucks": 1500
}
'''
class StoreItem(db.Model):

  __tablename__ = 'store_items'

  # id = db.Column(db.Integer, primary_key=True)
  manifest_id = db.Column(db.Integer, primary_key=True)
  # date = db.Column(db.String(19), primary_key=True)
  date = db.Column(db.String(10), primary_key=True)
  name = db.Column(db.String(255), unique=False, nullable=False)
  rarity = db.Column(db.String(20), unique=False, nullable=False)
  image_url = db.Column(db.String(255), unique=False, nullable=False, default='')
  store_category = db.Column(db.String(50), unique=False, nullable=False)
  vbucks = db.Column(db.Integer, unique=False, nullable=False, default=0)

  def __init__(self, manifest_id, name, rarity, image_url, store_category, vbucks):
    self.manifest_id  = manifest_id
    self.date = datetime.now().strftime("%Y-%m-%d")
    # self.date = datetime.now().strftime("2019-02-29")
    # self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.name = name
    self.rarity = rarity
    self.image_url  = image_url
    self.store_category = store_category
    self.vbucks = vbucks

  def __str__(self):
    message = (
        f"Store Item:\n"
        f" - manifest_id: {self.manifest_id}\n"
        f" - date: {self.date}\n"
        f" - name: {self.name}\n"
        f" - rarity: {self.rarity}\n"
        f" - store_category: {self.store_category}\n"
        f" - vbucks: {self.vbucks}\n"
        f" - image_url: {self.image_url}\n"        
      )
    return message

  def __repr__(self):
    return json.dumps(self.__dict__)
      
  def to_dict(self):
    item = {}
    item['name'] = self.name
    item['manifestId'] = self.manifest_id
    item['rarity'] = self.rarity
    item['storeCategory'] = self.store_category
    item['vBucks'] = self.vbucks
    item['imageUrl'] = self.image_url
    return item

