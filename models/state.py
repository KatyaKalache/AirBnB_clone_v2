#!/usr/bin/python3
"""
State Class from Models Module
"""

from os import environ
from models.base_model import BaseModel, Base, Column, String, relationship


class State(BaseModel, Base):
    """State class handles all application states"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              cascade='all, delete-orphan',
                              backref='State')
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
