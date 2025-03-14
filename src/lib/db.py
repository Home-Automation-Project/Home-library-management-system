from tinydb import TinyDB, Query
import couchdb

class CouchEngine:
    
    COUCHDB_USER = "myadmin"
COUCHDB_PASSWORD = "mypassword"
COUCHDB_URL = f"http://{COUCHDB_USER}:{COUCHDB_PASSWORD}@localhost:5984/"
server = couchdb.Server(COUCHDB_URL)


def insert(self):
  server = couchdb.Server("http://admin:password@localhost:5984/")
  db = server.create("mydatabase")  # Creates a new database
  db.save({"name": "Alice", "age": 25})
   print(list(db))
  

class TinydbEngine:
  def insert(self):
     db = TinyDB('data.json')
     db.insert({'name': 'Alice', 'age': 25})
     print(db.all())
