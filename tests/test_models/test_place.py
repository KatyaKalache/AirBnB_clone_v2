#!/usr/bin/python3
"""
Unit Test for Place Class
"""
import unittest
from datetime import datetime
import models
import json
import inspect
from os import environ

User = models.User
State = models.State
City = models.City
Place = models.Place
BaseModel = models.BaseModel


class TestPlaceDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    all_funcs = inspect.getmembers(Place, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   Place Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nPlace Class from Models Module\n'
        actual = models.place.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Place class handles all application places'
        actual = Place.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in place file"""
        AF = TestPlaceDocs.all_funcs
        for f in AF:
            self.assertTrue(len(f[1].__doc__) > 1)


class TestPlaceInstances(unittest.TestCase):
    """testing for class instances"""

    state = State(**{"name": "California"})
    user = User(**{"email": "bettyholbertn@gmail.com",
                   "password": "apass",
                   "first_name": "a_name",
                   "last_name": "a_last_name"})
    user.save()
    state.save()
    city = City(**{"state_id": "{}".format(state.id),
                   "name": "SanFrancisco"})
    city.save()
    place = Place(**{'city_id': '{}'.format(city.id),
                     'user_id': '{}'.format(user.id),
                     'name': 'A humble home',
                     'number_rooms': 4,
                     'number_bathrooms': 2,
                     'max_guest': 99})

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Place Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new place for testing"""
        self.place = TestPlaceInstances.place

    def test_instantiation(self):
        """... checks if Place is properly instantiated"""
        self.assertIsInstance(self.place, Place)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.place)
        my_list = ['Place', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        actual = type(self.place.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.place_json = self.place.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.place_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value Place"""
        self.place_json = self.place.to_json()
        actual = None
        if self.place_json['__class__']:
            actual = self.place_json['__class__']
        expected = 'Place'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... check name attribute"""
        if hasattr(self.place, 'name'):
            actual = self.place.name
        else:
            actual = ''
        expected = 'A humble home'
        self.assertEqual(expected, actual)
        self.assertIsInstance(self.place, Place)

    def test_num_rms_attribute(self):
        """... check number of rooms attribute"""
        if hasattr(self.place, 'number_rooms'):
            actual = self.place.number_rooms
        else:
            actual = 0
        expected = 4
        self.assertEqual(expected, actual)
        self.assertIsInstance(self.place.number_rooms, int)

if __name__ == '__main__':
    unittest.main
