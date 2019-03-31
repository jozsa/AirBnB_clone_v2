#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String


class City(BaseModel, Base):
    """
    This is the class for City. It is linked to the cities table

    Attributes:
        state_id: String, Foreign Key to State ID associated with city
        name: String, name of city
    """
    __tablename__ = 'cities'

    state_id = Column(String(60),
                      nullable=False,
                      ForeignKey(State.id))
    name = Column(String(128),
                  nullable=false)
