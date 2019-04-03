#!/usr/bin/python3
"""This is the place class"""
# import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """
    This is the class for Place objects.

    Attributes:
        city_id: non-Null String from table `cities`, 60 characters
        user_id: non-Null String from table `users`, 60 characters
        name: non-Null String, 128 characters
        description: nullable String, 1024 characters
        number_rooms: non-Null Integer, default 0
        number_bathrooms: non-Null Integer, default 0
        max_guest: non-Null Integer, default 0
        price_by_night: non-Null Integer, default 0
        latitude: nullable Float, default 0
        longitude: nullable Float, default 0
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    amenity_ids = []
