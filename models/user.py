#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String


class User(BaseModel, Base):
    """User class handles all application users"""

    __tablename__ = 'users'

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
