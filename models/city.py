#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel, Base, String, Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class City(BaseModel, Base):
    """City class handles all application cities"""

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
