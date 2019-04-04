#!/usr/bin/python3
"""This is the review class"""
# import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.orm import relationship, backref


class Review(BaseModel, Base):
    """
    This is the class for Review objects.
    It is associated with the SQL table 'reviews'.

    Attributes:
        place_id: non-Null String from table `places`, 60 characters
        user_id: non-Null String from table `users`, 60 characters
        text: non-Null String, 1024 characters
    """
    __tablename__ = 'reviews'

    place_id = Column(String(60),
                      ForeignKey('places.id'),
                      nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    text = Column(String(1024),
                  nullable=False)
