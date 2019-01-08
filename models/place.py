#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
import models


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column("city_id", String(60),
                     ForeignKey("cities.id"), nullable=False)
    user_id = Column("user_id", String(60),
                     ForeignKey("users.id"), nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024), nullable=True)
    number_rooms = Column("number_rooms", Integer, default=0, nullable=False)
    number_bathrooms = Column("number_bathrooms",
                              Integer, default=0,  nullable=False)
    max_guest = Column("max_guest",
                       Integer, default=0,  nullable=False)
    price_by_night = Column("price_by_night",
                            Integer, default=0, nullable=False)

    latitude = Column("latitude", Float, nullable=True)
    longitude = Column("longitude", Float, nullable=True)

    reviews = relationship("Review", backref="place",
                           cascade="all, delete")

    @property
    def reviews(self):
        r_list = []
        # objects = models.storage.all()
        # for k, v in objects.items():
        #    if (v.__class__.__name__ == "Review" and v.place_id == self.id):
        #            r_list.append(v)
        # return(r_list)
        for v in models.storage.all(models.Review).values():
            if v.place_id == self.id:
                r_list.append(v)
        return(r_list)
