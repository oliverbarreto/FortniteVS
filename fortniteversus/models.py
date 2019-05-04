import os
import json
from datetime import datetime,timedelta
#from fortniteversus import db

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

Noticias_items = NewsItems()



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

Store_items = StoreItems()
