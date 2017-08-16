#!/usr/bin/python3
from models.engine import file_storage
from models import base_model, amenity, city, place, review, state, user
from os import environ

"""conditional to determine the storage engine type"""
if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == 'db':
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    storage = file_storage.FileStorage()
storage.reload()

Amenity = amenity.Amenity
BaseModel = base_model.BaseModel
City = city.City
Place = place.Place
Review = review.Review
State = state.State
User = user.User

"""CNC - dictionary = { Class Name (string) : Class Type }"""
CNC = file_storage.FileStorage.CNC
