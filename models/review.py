#!/usr/bin/python3
"""
Review Class from Models Module
"""

from os import environ
from models.base_model import BaseModel, Base, String, Column
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """Review class handles all application reviews"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ''
        user_id = ''
        text = ''
