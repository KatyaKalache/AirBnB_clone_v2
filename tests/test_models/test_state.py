#!/usr/bin/python3
"""
Unit Test for State Class
"""
import unittest
from datetime import datetime
import models
import json
import inspect
from os import environ

State = models.State
BaseModel = models.BaseModel


class TestStateDocs(unittest.TestCase):
    """Class for testing State docs"""

    all_funcs = inspect.getmembers(State, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   State Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nState Class from Models Module\n'
        actual = models.state.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'State class handles all application states'
        actual = State.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in state file"""
        AF = TestStateDocs.all_funcs
        for f in AF:
            self.assertIsNotNone(f[1].__doc__)


class TestStateInstances(unittest.TestCase):
    """testing for class instances"""

    state = State(**{"name": "California"})
    state.save()

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  State Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new state for testing"""
        self.state = TestStateInstances.state

    def test_instantiation(self):
        """... checks if State is properly instantiated"""
        self.assertIsInstance(self.state, State)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.state)
        my_list = ['State', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                     "File Storage not initiated w/ updated_at")
    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        actual = type(self.state.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.state_json = self.state.to_json()
        serializable = True
        try:
            serialized = json.dumps(self.state_json)
        except:
            serializable = False
        self.assertTrue(serializable)

    def test_json_class(self):
        """... to_json should include class key with value State"""
        self.state_json = self.state.to_json()
        actual = None
        if self.state_json['__class__']:
            actual = self.state_json['__class__']
        expected = 'State'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... add name attribute"""
        if hasattr(self.state, 'name'):
            actual = self.state.name
        else:
            actual = ''
        expected = "California"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
