#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String, ForeignKey
from models.base_model import relationship
from os import environ


class City(BaseModel, Base):
    """City class handles all application cities"""
    __abstract__ = True

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
        places = relationship('Place',
                              cascade='all, delete-orphan',
                              backref='cities')
    else:
        state_id = ''
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
