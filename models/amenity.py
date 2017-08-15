#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""

    name = Column(String(128), nullable=False)
    __tablename__ = "amenities"
#    place_amenities = relationship("PlaceAmenity", secondary="amenities")

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
