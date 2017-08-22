#!/usr/bin/python3
"""
Unit Test for City Class
"""
import unittest
from datetime import datetime
import models
import json
import inspect
from os import environ

State = models.State
City = models.City
BaseModel = models.BaseModel


class TestCityDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    all_funcs = inspect.getmembers(City, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   City Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nCity Class from Models Module\n'
        actual = models.city.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'City class handles all application cities'
        actual = City.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in city file"""
        AF = TestCityDocs.all_funcs
        for f in AF:
            self.assertIsNotNone(f[1].__doc__)


class TestCityInstances(unittest.TestCase):
    """testing for class instances"""

    state = State(**{"name": "California"})
    state.save()
    city = City(**{"state_id": "{}".format(state.id),
                   "name": "SanFrancisco"})
    city.save()

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  City Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new city for testing"""
        self.state = TestCityInstances.state
        self.city = TestCityInstances.city

    def test_instantiation(self):
        """... checks if City is properly instantiated"""
        self.assertIsInstance(self.city, City)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.city)
        my_list = ['City', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                     "DB Storage is initialized with updated at")
    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        actual = type(self.city.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.city_json = self.city.to_json()
        serializable = True
        try:
            serialized = json.dumps(self.city_json)
        except:
            serializable = False
        self.assertTrue(serializable)

    def test_json_class(self):
        """... to_json should include class key with value City"""
        self.city_json = self.city.to_json()
        actual = None
        if self.city_json['__class__']:
            actual = self.city_json['__class__']
        expected = 'City'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... add update attribute"""
        if hasattr(self.city, 'name'):
            actual = self.city.name
        else:
            actual = ''
        expected = 'SanFrancisco'
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
