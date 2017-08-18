#!/usr/bin/python3
"""
Unit Test for File Storage Class
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
if environ.get('HBNB_TYPE_STORAGE') != 'db':
    FileStorage = models.file_storage.FileStorage
storage = models.storage
F = './dev/file.json'


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') == 'db',
                 "DB Storage doesn't use FileStorage")
class TestFileStorageDocs(unittest.TestCase):
    """Class for testing File Storage docs"""

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        all_funcs = inspect.getmembers(FileStorage, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        """sets up the class"""
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ("\nHandles I/O, writing and reading, of JSON for storage "
                    "of all class instances\n")
        actual = models.file_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'handles long term storage of all class instances'
        actual = FileStorage.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in file_storage file"""
        AF = TestFileStorageDocs.all_funcs
        for f in AF:
            self.assertIsNotNone(f[1].__doc__)


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') == 'db',
                 "DB Storage doesn't use FileStorage")
class TestBmFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        """sets up the class"""
        print('\n\n.................................')
        print('...... Testing FileStorate ......')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def setUp(self):
        """initializes new storage object for testing"""
        self.bm_obj = BaseModel()
        self.bm_obj.save()

    def tearDown(self):
        """tidies up the tests removing storage objects"""
        storage.delete_all()

    def test_instantiation(self):
        """... checks proper FileStorage instantiation"""
        self.assertIsInstance(storage, FileStorage)

    def test_storage_file_exists(self):
        """... checks proper FileStorage instantiation"""
        os.remove(F)
        self.bm_obj.save()
        self.assertTrue(os.path.isfile(F))

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        bm_id = self.bm_obj.id
        all_obj = storage.all()
        actual = False
        for k in all_obj.keys():
            if bm_id in k:
                actual = True
        self.assertTrue(True)

    def test_obj_saved_to_file(self):
        """... checks proper FileStorage instantiation"""
        os.remove(F)
        self.bm_obj.save()
        bm_id = self.bm_obj.id
        actual = False
        with open(F, mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        for k in storage_dict.keys():
            if bm_id in k:
                actual = True
        self.assertTrue(True)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        my_model_json = self.bm_obj.to_json()
        actual = True
        try:
            serialized = json.dumps(my_model_json)
        except:
            actual = False
        self.assertTrue(actual)

    def test_reload(self):
        """... checks proper usage of reload function"""
        os.remove(F)
        self.bm_obj.save()
        bm_id = self.bm_obj.id
        actual = False
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k in all_obj.keys():
            if bm_id in k:
                actual = True
        self.assertTrue(actual)

    def test_save_reload_class(self):
        """... checks proper usage of class attribute in file storage"""
        os.remove(F)
        self.bm_obj.save()
        bm_id = self.bm_obj.id
        actual = False
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k, v in all_obj.items():
            if bm_id in k:
                if type(v).__name__ == 'BaseModel':
                    actual = True
        self.assertTrue(actual)


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') == 'db',
                 "DB Storage doesn't use FileStorage")
class TestUserFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        """sets up the class"""
        print('\n\n.................................')
        print('...... Testing FileStorage ......')
        print('.......... User  Class ..........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new user for testing"""
        self.user = User()
        self.user.save()
        self.bm_obj = BaseModel()
        self.bm_obj.save()

    def tearDown(self):
        """tidies up the tests removing storage objects"""
        storage.delete_all()

    def test_storage_file_exists(self):
        """... checks proper FileStorage instantiation"""
        os.remove(F)
        self.user.save()
        self.assertTrue(os.path.isfile(F))

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        u_id = self.user.id
        all_obj = storage.all()
        actual = False
        for k in all_obj.keys():
            if u_id in k:
                actual = True
        self.assertTrue(actual)

    def test_obj_saved_to_file(self):
        """... checks proper FileStorage instantiation"""
        os.remove(F)
        self.user.save()
        u_id = self.user.id
        actual = False
        with open(F, mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        for k in storage_dict.keys():
            if u_id in k:
                actual = True
        self.assertTrue(actual)

    def test_reload(self):
        """... checks proper usage of reload function"""
        os.remove(F)
        self.bm_obj.save()
        u_id = self.bm_obj.id
        actual = False
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k in all_obj.keys():
            if u_id in k:
                actual = True
        self.assertTrue(actual)

if __name__ == '__main__':
    unittest.main
    storage.delete_all()
