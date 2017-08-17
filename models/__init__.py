#!/usr/bin/python3
from models.engine import file_storage
from models.engine import db_storage
from os import environ
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""conditional to determine the storage engine type"""
if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == 'db':
    storage = db_storage.DBStorage()
    CNC = db_storage.DBStorage.CNC
else:
    storage = file_storage.FileStorage()
    CNC = file_storage.FileStorage.CNC

storage.reload()

"""CNC - dictionary = { Class Name (string) : Class Type }"""
