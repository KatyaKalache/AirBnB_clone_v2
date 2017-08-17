#!/usr/bin/python3
"""
Unit Test for DataBase Storage Class
"""
import unittest
from datetime import datetime
import models
import json
import os
import inspect
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

storage = models.storage
environ = os.environ
if environ.get('HBNB_TYPE_STORAGE') == 'db':
    DBStorage = models.db_storage.DBStorage


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "DB Storage doesn't use FileStorage")
class TestDBStorageDocs(unittest.TestCase):
    """Class for testing DB Storage docs"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        all_funcs = inspect.getmembers(DBStorage, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        """sets up the class for this round of tests"""
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('...... For DBStorage Class ......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        actual = models.db_storage.__doc__
        if actual:
            actual = len(actual)
        else:
            actual = 0
        self.assertTrue(actual > 5)

    def test_doc_class(self):
        """... documentation for the class"""
        actual = DBStorage.__doc__
        if actual:
            actual = len(actual)
        else:
            actual = 0
        self.assertTrue(actual > 5)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in db_storage file"""
        AF = TestDBStorageDocs.all_funcs
        for f in AF:
            self.assertTrue(len(f[1].__doc__) > 1)


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "DB Storage doesn't use FileStorage")
class TestAllInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        """sets up the class for this round of tests"""
        print('\n\n....................................')
        print('.......... Testing DBStorage .......')
        print('. State, City, User, Place Amenity .')
        print('.. Initial Variables Provided by: ..')
        print('............ @glyif.................\n\n')
        cls.s = State(name="California")
        cls.s.save()
        cls.c = City(state_id=cls.s.id,
                     name="San Francisco")
        cls.c.save()
        cls.u = User(email="betty@holbertonschool.com",
                     password="pwd")
        cls.u.save()
        cls.p1 = Place(user_id=cls.u.id,
                       city_id=cls.c.id,
                       name="a house")
        cls.p1.save()
        cls.p2 = Place(user_id=cls.u.id,
                       city_id=cls.c.id,
                       name="a house two")
        cls.p2.save()
        cls.a1 = Amenity(name="Wifi")
        cls.a1.save()
        cls.a2 = Amenity(name="Cable")
        cls.a2.save()
        cls.a3 = Amenity(name="Bucket Shower")
        cls.a3.save()
        storage.save()

    def setUp(self):
        """initializes new user for testing"""
        self.s = TestAllInstances.s
        self.c = TestAllInstances.c
        self.u = TestAllInstances.u
        self.p1 = TestAllInstances.p1
        self.p2 = TestAllInstances.p2
        self.a1 = TestAllInstances.a1
        self.a2 = TestAllInstances.a2
        self.a3 = TestAllInstances.a3

    def test_all_reload_save(self):
        """... checks if all(), save(), and reload function
        in new instance.  This also tests for reload"""
        actual = 0
        db_objs = storage.all()
        for obj in db_objs.values():
            for x in [self.s.id, self.c.id, self.u.id, self.p1.id]:
                if x == obj.id:
                    actual += 1
        self.assertTrue(actual == 4)

    def test_new(self):
        """... checks if new() function returns newly created instance"""
        actual = 0
        self.s_new = State(name="Illinois")
        self.s_new.save()
        db_objs = storage.all()
        for obj in db_objs.values():
            if obj.id == self.s_new.id:
                actual += 1
        self.assertTrue(actual == 1)

    def test_delete(self):
        """... checks if all(), save(), and reload function
        in new instance.  This also tests for reload"""
        actual = 0
        check_cls = type(self.s).__name__
        check = self.s.name
        storage.delete(self.s)
        db_objs = storage.all()
        for obj in db_objs.values():
            if type(obj).__name__ == check_cls and obj.name == check:
                actual += 1
        self.assertTrue(actual == 0)

if __name__ == '__main__':
    unittest.main
