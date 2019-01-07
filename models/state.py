#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from os import getenv



class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    # name = ""

    __tablename__ = "states"
    
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref=backref("state", cascade="all, delete-orphan"))
