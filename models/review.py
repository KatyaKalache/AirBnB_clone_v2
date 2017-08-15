#!/usr/bin/python3
"""
Review Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String


class Review(BaseModel, Base):
    """Review class handles all application reviews"""

    __tablename__ = 'reviews'

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
