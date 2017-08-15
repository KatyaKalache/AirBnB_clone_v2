#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String, relationship


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "PlaceAmenity",
        cascade="all, delete-orphan",
        backref="amenities"
    )

    """
    name = ''
    """

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)


class PlaceAmenity(BaseModel, Base):
    """ placeholder """

    __tablename__ = 'placeholder'
    pass
