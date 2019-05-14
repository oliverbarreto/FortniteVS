import os
import json
from datetime import datetime
from fortniteversus import db

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

def StoreItems():
  store_items = dummyStore_Items()
  
  return store_items

# Store_items = StoreItems()




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
  id = db.Column(db.Integer, primary_key=True)
  manifest_id = db.Column(db.String(6), unique=True, nullable=False)
  name = db.Column(db.String(255), unique=True, nullable=False)
  rarity = db.Column(db.String(20), unique=False, nullable=False)
  image_url = db.Column(db.String(255), unique=False, nullable=False, default='')
  store_category = db.Column(db.String(50), unique=False, nullable=False)
  vbucks = db.Column(db.Integer, unique=False, nullable=False, default=0)
  ##occurences = db.relationship('StoreItem', backref='item', lazy='True')

  def __repr__(self):
    message = (
        f"Store Item:\n"
        f" - manifest_id: {self.manifest_id}\n"
        f" - name: {self.name}\n"
        f" - rarity: {self.rarity}\n"
        f" - store_category: {self.store_category}\n"
        f" - vbucks: {self.vbucks}\n"
        f" - image_url: {self.image_url}\n"        
      )
    return message
  

class StoreItemOccurrence(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, default=datetime.utcnow)
  ##item_id = db.Column(db.Integer, db.ForeignKey('storeItem.id'), nullable=False)


  def __repr__(self):
    message = (
        f"Store Item Occurrence:\n"
        f" - id: {self.id}\n"
        f" - date: {self.date}\n"
      )
    return message




## https://devcenter.heroku.com/articles/heroku-postgresql#local-setup
## pip install flask-sqlalchemy
## pip install psycopg2-binary

## https://www.youtube.com/watch?v=cYWiDiIUxQc&t=292s
## https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/05-Package-Structure
## https://github.com/realpython/discover-flask



## from forniteversus import db
## db.create_all()

## from fortniteversus import models  
## store_item = models.StoreItem(manifest_id=123, name="pico", rarity="comun", store_category="BRDailyStorefront", vbucks=2000)
## store_item2 = models.StoreItem(manifest_id=124, name="ala delta", rarity="raro", store_category="BRDailyStorefront", vbucks=1500)
## db.session.add(store_item)
## db.session.add(store_item2)
## store_item2.id
## db.session.commit()

## models.StoreItem.query.all()
## models.StoreItem.query.filter_by(manifest_id='123').all()
## models.StoreItem.query.filter_by(manifest_id='123').first()



## pip uninstall psycopg2
## pip list --outdated
## pip install --upgrade wheel
## pip install --upgrade setuptools
## pip install psycopg2