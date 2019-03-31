#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """
    This is the class for State objects.
    It is associated with the SQL table 'states'.

    Attributes:
        name: String, 128 characters
    """
    name = Column(String(128),
                  nullable=False)

    """
    TODO:
    Add relationship between state/city (different for FileStorage and DBStorage)
    Haven't done DBStorage or set env vars so still unsure how to do this.
    """
