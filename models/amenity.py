#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from os import environ
from models.base_model import BaseModel, Base, Column, String, relationship


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "PlaceAmenity",
            cascade="all, delete-orphan",
            backref="amenities"
        )
    else:
        name = ''
