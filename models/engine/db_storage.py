#!/usr/bin/python3
"""
mysql DB storage engine
"""

from os import environ
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

hbuser = environ.get('HBNB_MYSQL_USER')
hbpw = environ.get('HBNB_MYSQL_PWD')
hbhost = environ.get('HBNB_MYSQL_HOST')
hbdb = environ.get('HBNB_MYSQL_DB')


class DBStorage:
    """handles long term storage in mysql database"""

    __engine = None
    __session = None
    __classes = [Amenity, City, Place, Review, State, User]

    def __init__(self):
        """instantiation of mysql DB as python object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(hbuser, hbpw, hbhost, hbdb))
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """queries all objects in DB session depending on the class name"""
        d = {}
        if not cls:
            for c in DBStorage.__classes:
                a_query = self.__session.query(c)
                for obj in a_query:
                    obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                    d[obj_ref] = obj
        else:
            a_query = self.__session.query(cls)
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                d[obj_ref] = obj
        return d

    def new(self, obj):
        """add the object to the current DB session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current DB session"""
        self.__session.commit()

    def reload(self):
        """create all tables in DB & create current DB session from engine"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def delete(self, obj=None):
        """delete from the current DB session"""
        if obj:
            self.__session.delete(obj)

    def delete_all(self):
        """deletes all stored objects, for testing purposes"""
        for c in DBStorage.__classes:
            a_query = self.__session.query(c)
            all_objs = [obj for obj in a_query]
            for obj in range(len(all_objs)):
                to_delete = all_objs.pop(0)
                to_delete.delete()
        self.save()
