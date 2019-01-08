#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from os import getenv
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    # name = ""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="State",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        s_id = self.id
        objects = models.storage.all()
        c = []
        for k, v in objects.items():
            if (v.__class__.__name__ == "City" and v.state_id == s_id):
                c.append(v)
        return(c)
