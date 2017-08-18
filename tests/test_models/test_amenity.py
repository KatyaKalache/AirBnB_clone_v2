#!/usr/bin/python3
"""
Unit Test for Amenity Class
"""
import unittest
from datetime import datetime
import models
import json
import inspect
from os import environ

Amenity = models.Amenity
BaseModel = models.BaseModel


class TestAmenityDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    all_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   Amenity  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nAmenity Class from Models Module\n'
        actual = models.amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Amenity class handles all application amenities'
        actual = Amenity.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in amenity file"""
        AF = TestAmenityDocs.all_funcs
        for f in AF:
            self.assertTrue(len(f[1].__doc__) > 1)


class TestAmenityInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Amenity  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new amenity for testing"""
        self.amenity = Amenity({"name": "buckets"})

    def test_instantiation(self):
        """... checks if Amenity is properly instantiated"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.amenity)
        my_list = ['Amenity', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "DB Storage is initialized with updated at")
    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.amenity)
        not_in = True
        if 'updated_at' in my_str:
            not_in = False
        self.assertTrue(not_in)

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                     "DB Storage only initializes with updated at")
    def test_updated_at(self):
        """... to see if updated at included with initialization"""
        actual = type(type(self.amenity.updated_at))
        expected = type(type(datetime.now()))
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.amenity_json = self.amenity.to_json()
        serializable = True
        try:
            serialized = json.dumps(self.amenity_json)
        except:
            serializable = False
        self.assertTrue(serializable)

    def test_json_class(self):
        """... to_json should include class key with value Amenity"""
        self.amenity_json = self.amenity.to_json()
        actual = None
        if self.amenity_json['__class__']:
            actual = self.amenity_json['__class__']
        expected = 'Amenity'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... update name attribute"""
        self.amenity.name = "greatWifi"
        if hasattr(self.amenity, 'name'):
            actual = self.amenity.name
        else:
            actual = ''
        expected = "greatWifi"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
