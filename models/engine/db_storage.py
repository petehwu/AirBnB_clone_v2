#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
import os
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class DBStorage():
    """DBStorage Class
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantialize DBStorage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query the current db for all objects
            Args:
                cls: classname for the queried object
        """
        all_dict = {}
        if cls:
            result = self.__session.query(cls).all()
        else:
            result = []
            result += self.__session.query(User).all()
            result += self.__session.query(State).all()
            result += self.__session.query(City).all()
            result += self.__session.query(Amenity).all()
            result += self.__session.query(Place).all()
            result += self.__session.query(Review).all()
        for v in result:
            k = '{}.{}'.format(v.__class__.__name__, v.id)
            all_dict[k] = v
        return all_dict

    def new(self, obj):
        """add an object to the current datatabase session
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
