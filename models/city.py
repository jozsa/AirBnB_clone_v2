#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """
    This is the class for City. It is linked to the cities table

    Attributes:
        state_id: String, Foreign Key to State ID associated with city
        name: String, name of city
    """
    __tablename__ = 'cities'

    state_id = Column(String(60),
                      ForeignKey(State.id),
                      nullable=False)
    name = Column(String(128),
                  nullable=False)
