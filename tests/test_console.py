#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
import models
from datetime import datetime
import console

Place = models.place.Place
HBNBCommand = console.HBNBCommand
FS = console.FS


class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Console  .......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nCommand interpreter for Holberton AirBnB project\n'
        actual = console.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Command inerpreter class'
        actual = HBNBCommand.__doc__
        self.assertEqual(expected, actual)


class TestHBNBCommandI(unittest.TestCase):
    """testing for class instances"""

    cli = HBNBCommand()
    obj = None

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new CLI object: ', end='')
        TestHBNBCommandI.cli.do_create('Place '
                                       'city_id="0001" '
                                       'user_id="0001" '
                                       'name="My_little_house" '
                                       'number_rooms=4 '
                                       'number_bathrooms=2 '
                                       'max_guest=10 '
                                       'price_by_night=300 '
                                       'latitude=37.773972 '
                                       'longitude=-122.431297')
        print('')
        fs_o = FS.all()
        for v in fs_o.values():
            TestHBNBCommandI.obj = v

    def setUp(self):
        """initializes new HBNBCommand instance for testing"""

    def test_instantiation(self):
        """... checks if HBNBCommand is properly instantiated"""
        print(self.cli)
        fs_o = FS.all()
        self.assertIsInstance(TestHBNBCommandI.cli, HBNBCommand)

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(TestHBNBCommandI.obj, Place)

    def test_attr_user_id(self):
        """... checks if proper parameter for user_id was created"""
        actual = TestHBNBCommandI.obj.user_id
        expected = "0001"
        self.assertEqual(expected, actual)

    def test_attr_city_id(self):
        """... checks if proper parameter for city_id was created"""
        actual = TestHBNBCommandI.obj.city_id
        expected = "0001"
        self.assertEqual(expected, actual)

    def test_attr_name(self):
        """... checks if proper parameter for name was created"""
        actual = TestHBNBCommandI.obj.name
        expected = 'My little house'
        self.assertEqual(expected, actual)

    def test_attr_num_rm(self):
        """... checks if proper parameter for number_rooms was created"""
        actual = TestHBNBCommandI.obj.number_rooms
        expected = 4
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_num_btrm(self):
        """... checks if proper parameter for number_bathrooms was created"""
        actual = TestHBNBCommandI.obj.number_bathrooms
        expected = 2
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_max_guest(self):
        """... checks if proper parameter for max_guest was created"""
        actual = TestHBNBCommandI.obj.max_guest
        expected = 10
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_price_bn(self):
        """... checks if proper parameter for price_by_night was created"""
        actual = TestHBNBCommandI.obj.price_by_night
        expected = 300
        self.assertEqual(expected, actual)
        self.assertEqual(type(actual), int)

    def test_attr_lat(self):
        """... checks if proper parameter for latitude was created"""
        actual = TestHBNBCommandI.obj.latitude
        expected = 37.773972
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), float)

    def test_attr_long(self):
        """... checks if proper parameter for longitude was created"""
        actual = TestHBNBCommandI.obj.longitude
        expected = -122.431297
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), float)


class TestHBNBCommandErr(unittest.TestCase):
    """testing for class instances
    These tests attempt to throw errors"""

    cli = HBNBCommand()
    obj = None

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('... Can I Kill your program ? ...')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new CLI object: ', end='')
        TestHBNBCommandErr.cli.do_create('Place '
                                         'city_id="00""""01" '
                                         'user_id="00_01" '
                                         'name="My____little____house" '
                                         'number_rooms="""4""" '
                                         'number_bathrooms=2.0 '
                                         'max_guest="\'\'"HEy-O"\'\'" ')
        print('')
        fs_o = FS.all()
        for v in fs_o.values():
            TestHBNBCommandErr.obj = v

    def setUp(self):
        """initializes new HBNBCommand instance for testing"""

    def test_instantiation(self):
        """... checks if HBNBCommand is properly instantiated"""
        print(self.cli)
        fs_o = FS.all()
        self.assertIsInstance(TestHBNBCommandErr.cli, HBNBCommand)

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(TestHBNBCommandErr.obj, Place)

    def test_attr_user_id(self):
        """... checks if proper parameter for user_id was created"""
        actual = TestHBNBCommandErr.obj.user_id
        expected = '00 01'
        self.assertEqual(expected, actual)

    def test_attr_city_id(self):
        """... checks if proper parameter for city_id was created"""
        actual = TestHBNBCommandErr.obj.city_id
        expected = '00""""01'
        self.assertEqual(expected, actual)

    def test_attr_name(self):
        """... checks if proper parameter for name was created"""
        actual = TestHBNBCommandErr.obj.name
        expected = 'My    little    house'
        self.assertEqual(expected, actual)

    def test_attr_num_rm(self):
        """... checks if proper parameter for number_rooms was created"""
        actual = TestHBNBCommandErr.obj.number_rooms
        expected = '""4""'
        self.assertEqual(expected, actual)

    def test_attr_num_btrm(self):
        """... checks if proper parameter for number_bathrooms was created"""
        actual = TestHBNBCommandErr.obj.number_bathrooms
        expected = 2.0
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), float)

    def test_attr_max_guest(self):
        """... checks if proper parameter for max_guest was created"""
        actual = TestHBNBCommandErr.obj.max_guest
        expected = '\'\'"HEy-O"\'\''
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
