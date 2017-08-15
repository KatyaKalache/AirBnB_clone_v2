#!/usr/bin/python3
"""
Review Class from Models Module
"""

from os import environ
from models.base_model import BaseModel, Base, Column, String


class Review(BaseModel, Base):
    """Review class handles all application reviews"""
    __abstract__ = True

    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'reviews'
    else:
        place_id = ''
        user_id = ''
        text = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
