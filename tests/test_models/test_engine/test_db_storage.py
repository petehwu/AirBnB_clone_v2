#!/usr/bin/python3
"""test for db stroage"""
import unittest
import pep8
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """this will test the DBStorage"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.storage = DBStorage()
        cls.__session = Session()

        self.stored = DBStorage()
        self.__session = Session()
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        self.stored.reload()
        self.state1 = State1()
        self.state1.name = "California"
        self.state2 = State2()
        self.state2.name = "Arizona"

    def tearDown(self):
        """tear down method"""
        pass
        # del self.stored

    def testAttributes(self):
        """Tests if required functions exits"""
        self.assertTrue(hasattr())

    def test_pep8_DBStorage(self):
        """Tests for pep8 styling"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "Fails PEP8 compliance")

    def test_all(self):
        """Tests for all in DBStorage"""
        self.objs = self.storage.all()
        self.assertIsNotNone(self.objs)
        self.assertEqual(type(self.objs), dict)

    def test_new(self):
        """Tests for new objects in DBStorage"""
        pass

    def test_save(self):
        """Tests for saving objects in DBStorage"""
        pass

    def test_delete(self):
        """Tests for deleting objects in DBStorage"""
        pass

    def test_reload(self):
        """Tests for reloading objects in DBStorage"""
        pass


if __name__ == "__main__":
    unittest.main()
