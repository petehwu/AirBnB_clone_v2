#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
import os
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """DBStorage Class
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantialize DBStorage engine"""
        user = os.getenv('HBNB_MYSQL_USER'),
        pwd = os.getenv('HBNB_MYSQL_PWD'),
        host = os.getenv('HBNB_MYSQL_HOST'),
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                       .format(usr, pwd, host, db),
                                       pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query the current db for all objects
            Args:
                cls: classname of the object to be queried
        """
        pass
        # if cls:
        #     for v in self.__session.query(models.classes[cls]).all():
        #         k = '{}.{}'.format(obj.__class__.__name__, obj.id)
        #         db_dict[k] = v

    
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
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """recreate all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
