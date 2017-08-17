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

environ = os.environ
User = models.user.User
BaseModel = models.base_model.BaseModel
if environ.get('HBNB_TYPE_STORAGE') == 'db':
    DBStorage = models.db_storage.DBStorage
    storage = models.storage


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "DB Storage doesn't use FileStorage")
class TestDBStorageDocs(unittest.TestCase):
    """Class for testing DB Storage docs"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        all_funcs = inspect.getmembers(DBStorage, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
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
        """... tests for ALL DOCS for all functions in file_storage file"""
        AF = TestDBStorageDocs.all_funcs
        for f in AF:
            self.assertTrue(len(f[1].__doc__) > 1)


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "DB Storage doesn't use FileStorage")
class TestBmFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing DBStorate ........')
        print('..... For DBStorage Class .......')
        print('.................................\n\n')


if __name__ == '__main__':
    unittest.main
