#!/usr/bin/python3
"""
Unit Test for User Class
"""
import unittest
from datetime import datetime
import models
import json
import inspect
from os import environ

User = models.User
BaseModel = models.BaseModel


class TestUserDocs(unittest.TestCase):
    """Class for testing User Class docs"""

    all_funcs = inspect.getmembers(User, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   User  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nUser Class from Models Module\n'
        actual = models.user.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'User class handles all application users'
        actual = User.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in User file"""
        AF = TestUserDocs.all_funcs
        for f in AF:
            self.assertTrue(len(f[1].__doc__) > 1)


class TestUserInstances(unittest.TestCase):
    """testing for class instances"""

    user = User(**{"email": "bettyholbertn@gmail.com",
                   "password": "apass",
                   "first_name": "a_name",
                   "last_name": "a_last_name"})
    user.save()

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  User  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new user for testing"""
        self.user = TestUserInstances.user

    def test_instantiation(self):
        """... checks if User is properly instantiated"""
        self.assertIsInstance(self.user, User)

    def test_to_string(self):
        """... checks if User is properly casted to string"""
        my_str = str(self.user)
        my_list = ['User', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "Only FS should have updated at")
    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        self.user = User()
        my_str = str(self.user)
        not_in = True
        if 'updated_at' in my_str:
            not_in = False
        self.assertTrue(not_in)

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') == 'db',
                     "Test only for DB Storage: ")
    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        actual = type(self.user.updated_at)
        expected = type(datetime.utcnow())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.user_json = self.user.to_json()
        serializable = True
        try:
            serialized = json.dumps(self.user_json)
        except:
            serializable = False
        self.assertTrue(serializable)

    def test_json_class(self):
        """... to_json should include class key with value User"""
        self.user_json = self.user.to_json()
        actual = None
        if self.user_json['__class__']:
            actual = self.user_json['__class__']
        expected = 'User'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        if hasattr(self.user, 'email'):
            actual = self.user.email
        else:
            actual = ''
        expected = "bettyholbertn@gmail.com"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
