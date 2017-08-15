#!/usr/bin/python3
"""
User Class from Models Module
"""

from os import environ
from models.base_model import BaseModel, Base, Column, String


class User(BaseModel, Base):
    """User class handles all application users"""

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'users'
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
