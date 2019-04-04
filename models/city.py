#!/usr/bin/python3
"""This is the city class"""
import os
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """
    This is the class for City. It is linked to the cities table

    Attributes:
        state_id: non-Null String, Foreign Key to State ID associated with city
        name: non-Null String, name of city
    """
    __tablename__ = 'cities'

    # TODO verify this syntax for ForeignKey
    # https://docs.sqlalchemy.org/en/latest/orm/examples.html#writing-your-own-suites
    state_id = Column(String(60),
                      ForeignKey(State.id),
                      nullable=False)
    name = Column(String(128),
                  nullable=False)

    if 'HBNB_TYPE_STORAGE' in os.environ:
        if os.environ['HBNB_TYPE_STORAGE'] == 'db':
            # TODO implement the deletion requirement
            places = relationship('Place',
                                  cascade='delete, delete-orphan',
                                  backref='cities')
