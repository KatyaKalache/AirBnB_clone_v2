#!/usr/bin/python3
"""
State Class from Models Module
"""

from os import environ
from models.base_model import BaseModel, Base, Column, String


class State(BaseModel, Base):
    """State class handles all application states"""

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'states'
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
