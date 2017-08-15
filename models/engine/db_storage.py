#!/usr/bin/python3
"""
mysql DB storage engine
"""

from models import base_model, amenity, city, place, review, state, user
from models import CNC


class DBStorage:
    """handles long term storage in mysql database"""

    __engine = None
    __session = None

    def init(self):
        """instantiation of mysql DB as python object"""
        self.__engine = None
        print(CNC)

    def all(self, cls=None):
        """queries all objects in DB session depending on the class name"""
        pass

    def new(self, obj):
        """add the object to the current DB session"""
        pass

    def save(self):
        """commit all changes of the current DB session"""
        pass

    def delete(self, obj=None):
        """delete from the current DB session"""
        pass

    def reload(self):
        """create all tables in DB & create current DB session from engine"""
        pass
