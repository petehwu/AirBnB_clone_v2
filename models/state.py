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
    cities = relationship("City", backref="State", cascade="all, delete, delete-orphan")

    #TODO:
    #Link state and city together with getter attibute
    #FileStorage Attribute between State and City

    @property
    def cities(self):
        s_id = self.id
        type = self.__class__.__name__
        lookup = type + "." + s_id
        print("lookup_key:", lookup)
        c = []
        for k, v in FileStorage.__objects:
            if v["__class__"]== "City" and v["state_id"] == s_id:
                c.append(v)
        return(c)
         # my_dict = dict(FileStorage.__objects)
        # for k, v in my_dict.items():
        #     if v == obj:
        #         del FileStorage.__objects[k]
        #     self.save()
        
