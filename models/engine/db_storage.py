#!/usr/bin/python3
"""
mysql DB storage engine
"""

from os import environ
from models import base_model, amenity, city, place, review, state, user
from models.basemodel import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.file_storage import CNC

Amenity = amenity.Amenity
City = city.City
Place = place.Place
Review = review.Review
State = state.State
User = user.User
hbuser = environ.get('HBNB_MYSQL_USER')
hbpw = environ.get('HBNB_MYSQL_PWD')
hbhost = environ.get('HBNB_MYSQL_HOST')
hbdb = environ.get('HBNB_MYSQL_DB')


class DBStorage:
    """handles long term storage in mysql database"""

    __engine = None
    __session = None
    __classes = [Amenity, BaseModel, City, Place, Review, State, User]

    def init(self):
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
                    d[obj.id] = obj
        else:
            a_query = self.__session.query(cls)
            d = {obj.id: obj for obj in a_query}
        return d

    def new(self, obj):
        """add the object to the current DB session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current DB session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current DB session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in DB & create current DB session from engine"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
