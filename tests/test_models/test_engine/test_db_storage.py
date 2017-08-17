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
    """testing for Various State Class instances & methods"""

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

    def test_state_no_name(self):
        """... checks to create a state with no name"""
        with self.assertRaises(Exception) as context:
            s = State()
            self.assertTrue('"Column \'name\' cannot be null"'
                            in str(context.exception))

    def test_city_no_state(self):
        """... checks to create a city with invalid state"""
        with self.assertRaises(Exception) as context:
            c = City(name="Tapioca", state_id="NOT VALID")
            self.assertTrue('a child row: a foreign key constraint fails'
                            in str(context.exception))

    def test_place_no_user(self):
        """... checks to create a place with no city"""
        with self.assertRaises(Exception) as context:
            p = Place()
            print(context.exception)
            self.assertTrue('"Column \'city_id\' cannot be null"'
                            in str(context.exception))

    def test_review_no_text(self):
        """... checks to create a Review with no text"""
        with self.assertRaises(Exception) as context:
            r = Review()
            print(context.exception)
            self.assertTrue('"Column \'text\' cannot be null"'
                            in str(context.exception))

    def test_amenity_no_name(self):
        """... checks to create an amenity with no name"""
        with self.assertRaises(Exception) as context:
            a = Amenity()
            print(context.exception)
            self.assertTrue('"Column \'name\' cannot be null"'
                            in str(context.exception))

    def test_user_no_name(self):
        """... checks to create a user with no email"""
        with self.assertRaises(Exception) as context:
            u = User()
            print(context.exception)
            self.assertTrue('"Column \'email\' cannot be null"'
                            in str(context.exception))


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "DB Storage doesn't use FileStorage")
class TestTracebackTypeError(unittest.TestCase):
    """testing for throwing Traceback erros
    Setting attributes of wrong Type"""

    @classmethod
    def setUpClass(cls):
        """sets up the class for this round of tests"""
        print('\n\n....................................')
        print('.......... Testing DBStorage .......')
        print('. Throw Type Error for Place Class .')
        print('....................................\n\n')
        cls.s = State(name="Illinois")
        cls.s.save()
        cls.c = City(state_id=cls.s.id,
                     name="Chicago")
        cls.c.save()
        cls.u = User(email="holberton@holbertonschool.com",
                     password="pwd")
        cls.u.save()
        storage.save()

    def setUp(self):
        """initializes new user for testing"""
        self.s = TestTracebackTypeError.s
        self.c = TestTracebackTypeError.c
        self.u = TestTracebackTypeError.u
        self.cls = TestTracebackTypeError

    def test_description_int(self):
        """... create int type description"""
        with self.assertRaises(Exception) as context:
            p1 = Place(user_id=self.cls.u.id,
                       city_id=self.cls.c.id,
                       name="a house",
                       description=5)
            self.assertTrue('Incorrect string value:'
                            in str(context.exception))

    def test_number_rooms_str(self):
        """... create number_rooms that is str type"""
        with self.assertRaises(Exception) as context:
            p1 = Place(user_id=self.cls.u.id,
                       city_id=self.cls.c.id,
                       name="a house",
                       number_rooms="1.0")
            self.assertTrue('Incorrect integer value:'
                            in str(context.exception))

    def test_number_bathrooms_str(self):
        """... create number_bathrooms that is str type"""
        with self.assertRaises(Exception) as context:
            p1 = Place(user_id=self.cls.u.id,
                       city_id=self.cls.c.id,
                       name="a house",
                       number_bathrooms="1.0")
            self.assertTrue('Incorrect integer value:'
                            in str(context.exception))

    def test_max_guest_str(self):
        """... create max_guest str type"""
        with self.assertRaises(Exception) as context:
            p1 = Place(user_id=self.cls.u.id,
                       city_id=self.cls.c.id,
                       name="a house",
                       max_guest="1.0")
            self.assertTrue('Incorrect integer value:'
                            in str(context.exception))

    def test_amenity_no_name(self):
        """... create price_by_night str"""
        with self.assertRaises(Exception) as context:
            p1 = Place(user_id=self.cls.u.id,
                       city_id=self.cls.c.id,
                       name="a house",
                       price_by_night="1.0")
            self.assertTrue('Incorrect integer value:'
                            in str(context.exception))

if __name__ == '__main__':
    unittest.main
