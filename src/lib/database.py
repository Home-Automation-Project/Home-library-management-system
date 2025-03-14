from abc import ABC, abstractmethod
from typing import Any, Dict, List

class DatabaseInterface(ABC):
    """Defines a common interface for database operations."""
    
    @abstractmethod
    def insert(self, data: Dict[str, Any]) -> str:
        """Inserts a document into the database and returns its ID."""
        pass

    @abstractmethod
    def delete(self, doc_id: str) -> bool:
        """Deletes a document by ID and returns whether it was successful."""
        pass

    @abstractmethod
    def update(self, doc_id: str, data: Dict[str, Any]) -> bool:
        """Updates a document by ID and returns whether it was successful."""
        pass

    @abstractmethod
    def get(self, doc_id: str) -> Dict[str, Any]:
        """Retrieves a document by ID."""
        pass
        
        
from tinydb import TinyDB, Query

class TinyDBHandler(DatabaseInterface):
    def __init__(self, db_path: str = "tinydb.json"):
        self.db = TinyDB(db_path)
        self.table = self.db.table("data")

    def insert(self, data: Dict[str, Any]) -> str:
        doc_id = self.table.insert(data)
        return str(doc_id)  # TinyDB returns int IDs

    def delete(self, doc_id: str) -> bool:
        return self.table.remove(doc_ids=[int(doc_id)]) > 0

    def update(self, doc_id: str, data: Dict[str, Any]) -> bool:
        return self.table.update(data, doc_ids=[int(doc_id)]) > 0

    def get(self, doc_id: str) -> Dict[str, Any]:
        result = self.table.get(doc_id=int(doc_id))
        return result if result else {}
        
        
import couchdb

class CouchDBHandler(DatabaseInterface):
    def __init__(self, url: str = "http://admin:password@localhost:5984", db_name: str = "data"):
        self.server = couchdb.Server(url)
        if db_name in self.server:
            self.db = self.server[db_name]
        else:
            self.db = self.server.create(db_name)

    def insert(self, data: Dict[str, Any]) -> str:
        doc_id, _ = self.db.save(data)
        return doc_id  # CouchDB returns a string ID

    def delete(self, doc_id: str) -> bool:
        try:
            doc = self.db[doc_id]
            self.db.delete(doc)
            return True
        except couchdb.http.ResourceNotFound:
            return False

    def update(self, doc_id: str, data: Dict[str, Any]) -> bool:
        try:
            doc = self.db[doc_id]
            doc.update(data)
            self.db.save(doc)
            return True
        except couchdb.http.ResourceNotFound:
            return False

    def get(self, doc_id: str) -> Dict[str, Any]:
        try:
            return self.db[doc_id]
        except couchdb.http.ResourceNotFound:
            return {}