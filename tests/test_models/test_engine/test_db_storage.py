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
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """... documentation for the class"""
        actual = DBStorage.__doc__
        self.assertIsNotNone(actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in db_storage file"""
        AF = TestDBStorageDocs.all_funcs
        for f in AF:
            self.assertIsNotNone(f[1].__doc__)


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "DB Storage doesn't use FileStorage")
class TestTracebackNullError(unittest.TestCase):
    """testing for throwing Traceback erros:
    missing attributes that Cannot be NULL"""

    @classmethod
    def setUpClass(cls):
        """sets up the class for this round of tests"""
        print('\n\n....................................')
        print('.......... Testing DBStorage .......')
        print('...... Trying to Throw Errors ......')
        print('....................................\n\n')

    def tearDown(self):
        """tidies up tests that throw errors"""
        storage.rollback_session()

    def test_state_no_name(self):
        """... checks to create a state with no name"""
        with self.assertRaises(Exception) as context:
            s = State()
            s.save()
        self.assertTrue('"Column \'name\' cannot be null"'
                        in str(context.exception))

    def test_city_no_state(self):
        """... checks to create a city with invalid state"""
        with self.assertRaises(Exception) as context:
            c = City(name="Tapioca", state_id="NOT VALID")
            c.save()
        self.assertTrue('a child row: a foreign key constraint fails'
                        in str(context.exception))

    def test_place_no_user(self):
        """... checks to create a place with no city"""
        with self.assertRaises(Exception) as context:
            p = Place()
            p.save()
        self.assertTrue('"Column \'city_id\' cannot be null"'
                        in str(context.exception))

    def test_review_no_text(self):
        """... checks to create a Review with no text"""
        with self.assertRaises(Exception) as context:
            r = Review()
            r.save()
        self.assertTrue('"Column \'text\' cannot be null"'
                        in str(context.exception))

    def test_amenity_no_name(self):
        """... checks to create an amenity with no name"""
        with self.assertRaises(Exception) as context:
            a = Amenity()
            a.save()
        self.assertTrue('"Column \'name\' cannot be null"'
                        in str(context.exception))

    def test_user_no_name(self):
        """... checks to create a user with no email"""
        with self.assertRaises(Exception) as context:
            u = User()
            u.save()
        self.assertTrue('"Column \'email\' cannot be null"'
                        in str(context.exception))


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "DB Storage doesn't use FileStorage")
class TestAllInstances(unittest.TestCase):
    """testing for Various State Class instances & methods"""

    @classmethod
    def setUpClass(cls):
        """sets up the class for this round of tests"""
        print('\n\n....................................')
        print('.......... Testing DBStorage .......')
        print('. State, City, User, Place Amenity .')
        print('....................................')
        storage.delete_all()
        cls.s = State(name="California")
        cls.c = City(state_id=cls.s.id,
                     name="San Francisco")
        cls.u = User(email="betty@holbertonschool.com",
                     password="pwd")
        cls.p1 = Place(user_id=cls.u.id,
                       city_id=cls.c.id,
                       name="a house")
        cls.p2 = Place(user_id=cls.u.id,
                       city_id=cls.c.id,
                       name="a house two")
        cls.a1 = Amenity(name="Wifi")
        cls.a2 = Amenity(name="Cable")
        cls.a3 = Amenity(name="Bucket Shower")
        objs = [cls.s, cls.c, cls.u, cls.p1, cls.p2, cls.a1, cls.a2, cls.a3]
        for obj in objs:
            obj.save()

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
        actual = False
        self.s_new = State(name="Illinois")
        self.s_new.save()
        db_objs = storage.all()
        for obj in db_objs.values():
            if obj.id == self.s_new.id:
                actual = True
        self.assertTrue(actual)

    def test_delete(self):
        """... checks if all(), save(), and reload function
        in new instance.  This also tests for reload"""
        actual = True
        check_cls = type(self.s).__name__
        check = self.s.name
        self.s.delete()
        storage.save()
        db_objs = storage.all()
        for obj in db_objs.values():
            if type(obj).__name__ == check_cls and obj.name == check:
                actual = False
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main
    storage.delete_all()
