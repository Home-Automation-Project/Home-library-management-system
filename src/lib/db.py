from tinydb import TinyDB, Query
import couchdb

class CouchEngine:
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
