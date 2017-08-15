#!/usr/bin/python3
"""
Place Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String


class Place(BaseModel, Base):
    """Place class handles all application places"""

    __tablename__ = 'places'

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ['', '']

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)
