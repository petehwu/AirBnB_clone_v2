#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
import models
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"), nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), nullable=False))


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
    amenity_ids = []

    amenities = relationship("Amenity", secondary=place_amenity,
                             backref="place_amenities", viewonly=False)
    # amenities = relationship("Amenity", secondary=place_amenity,
    #                        backref="Place", viewonly=False)

    reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") == "FileStorage":
        @property
        def reviews(self):
            r_list = []
            for v in models.storage.all(models.Review).values():
                if v.place_id == self.id:
                    r_list.append(v)
            return(r_list)

        @property
        def amenities(self):
            print("getter")
            a_list = []
            for v in self.amenity_ids:
                for val in models.storage.all(models.Amenity).values():
                    if v == val.id:
                        a_list.append(val)
            return(a_list)

        @amenities.setter
        def amenities(self, value):
            print("setter")
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
