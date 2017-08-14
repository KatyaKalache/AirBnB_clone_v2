#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
import models
from datetime import datetime
import console
import inspect

Place = models.place.Place
State = models.state.State
User = models.user.User
HBNBCommand = console.HBNBCommand
FS = console.FS


class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    all_funcs = inspect.getmembers(console.HBNBCommand, inspect.isfunction)

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

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in console file"""
        AF = TestHBNBCommandDocs.all_funcs
        for f in AF:
            if "_HBNBCommand_" in f[0]:
                self.assertTrue(len(f[1].__doc__) > 1)


class TestHBNBCommandI(unittest.TestCase):
    """testing instantiation of CLI & create() function"""

    cli = HBNBCommand()
    obj = None

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('.... Test create() w/ params ....')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new Place object: ', end='')
        CLI = TestHBNBCommandI.cli
        CLI.do_create('Place '
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
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBCommandI.cli
        self.obj = TestHBNBCommandI.obj

    def test_instantiation(self):
        """... checks if HBNBCommand is properly instantiated"""
        self.assertIsInstance(self.CLI, HBNBCommand)

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(self.obj, Place)

    def test_attr_user_id(self):
        """... checks if proper parameter for user_id was created"""
        actual = self.obj.user_id
        expected = "0001"
        self.assertEqual(expected, actual)

    def test_attr_city_id(self):
        """... checks if proper parameter for city_id was created"""
        actual = self.obj.city_id
        expected = "0001"
        self.assertEqual(expected, actual)

    def test_attr_name(self):
        """... checks if proper parameter for name was created"""
        actual = self.obj.name
        expected = 'My little house'
        self.assertEqual(expected, actual)

    def test_attr_num_rm(self):
        """... checks if proper parameter for number_rooms was created"""
        actual = self.obj.number_rooms
        expected = 4
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_num_btrm(self):
        """... checks if proper parameter for number_bathrooms was created"""
        actual = self.obj.number_bathrooms
        expected = 2
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_max_guest(self):
        """... checks if proper parameter for max_guest was created"""
        actual = self.obj.max_guest
        expected = 10
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_price_bn(self):
        """... checks if proper parameter for price_by_night was created"""
        actual = self.obj.price_by_night
        expected = 300
        self.assertEqual(expected, actual)
        self.assertEqual(type(actual), int)

    def test_attr_lat(self):
        """... checks if proper parameter for latitude was created"""
        actual = self.obj.latitude
        expected = 37.773972
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), float)

    def test_attr_long(self):
        """... checks if proper parameter for longitude was created"""
        actual = self.obj.longitude
        expected = -122.431297
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), float)


class TestHBNBCommandErr(unittest.TestCase):
    """tests instantiation of CLI and create() function
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
        print('...creating new Place object: ', end='')
        CLI = TestHBNBCommandErr.cli
        CLI.do_create('Place '
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
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBCommandErr.cli
        self.obj = TestHBNBCommandErr.obj

    def test_instantiation(self):
        """... checks if HBNBCommand is properly instantiated"""
        self.assertIsInstance(self.CLI, HBNBCommand)

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(self.obj, Place)

    def test_attr_user_id(self):
        """... checks if proper parameter for user_id was created"""
        actual = self.obj.user_id
        expected = '00 01'
        self.assertEqual(expected, actual)

    def test_attr_city_id(self):
        """... checks if proper parameter for city_id was created"""
        actual = self.obj.city_id
        expected = '00""""01'
        self.assertEqual(expected, actual)

    def test_attr_name(self):
        """... checks if proper parameter for name was created"""
        actual = self.obj.name
        expected = 'My    little    house'
        self.assertEqual(expected, actual)

    def test_attr_num_rm(self):
        """... checks if proper parameter for number_rooms was created"""
        actual = self.obj.number_rooms
        expected = '""4""'
        self.assertEqual(expected, actual)

    def test_attr_num_btrm(self):
        """... checks if proper parameter for number_bathrooms was created"""
        actual = self.obj.number_bathrooms
        expected = 2.0
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), float)

    def test_attr_max_guest(self):
        """... checks if proper parameter for max_guest was created"""
        actual = self.obj.max_guest
        expected = '\'\'"HEy-O"\'\''
        self.assertEqual(expected, actual)


class TestHBNBCommandfunc(unittest.TestCase):
    """Test instantiation of CLI with tests for all other functions"""

    cli = HBNBCommand()
    obj = None

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('.. Testing All other Functions ..')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new State object: ', end='')
        TestHBNBCommandfunc.cli.do_create('State')
        print('')
        fs_o = FS.all()
        for v in fs_o.values():
            TestHBNBCommandfunc.obj = v

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBCommandfunc.cli
        self.obj = TestHBNBCommandfunc.obj

    def test_instantiation(self):
        """... checks if HBNBCommand is properly instantiated"""
        self.assertIsInstance(self.CLI, HBNBCommand)

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(self.obj, State)

    def test_attr_name(self):
        """... checks if proper parameter for name was created"""
        self.CLI.do_update('State {} name "California"'.format(self.obj.id))
        actual = self.obj.name
        expected = 'California'
        self.assertEqual(expected, actual)

    def test_destroy(self):
        """... checks if object can be destroyed"""
        self.CLI.do_destroy('State {}'.format(self.obj.id))
        try:
            self.obj
            self.assertTrue(False)
        except:
            self.assertIsNone(None)


class TestHBNBCommandfunc2(unittest.TestCase):
    """Test instantiation of CLI with tests for .function() notation"""

    cli = HBNBCommand()
    obj = None
    obj2 = None

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('... Tests .function() noation ...')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new User object: ', end='')
        TestHBNBCommandfunc2.cli.do_User('.create()')
        print('...creating new User object: ', end='')
        TestHBNBCommandfunc2.cli.do_User('.create()')
        print('')
        fs_o = FS.all()
        for v in fs_o.values():
            if not TestHBNBCommandfunc2.obj:
                TestHBNBCommandfunc2.obj = v
            else:
                TestHBNBCommandfunc2.obj2 = v

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBCommandfunc2.cli
        self.obj = TestHBNBCommandfunc2.obj
        self.obj2 = TestHBNBCommandfunc2.obj2

    def test_instantiation(self):
        """... checks if HBNBCommand is properly instantiated"""
        self.assertIsInstance(self.CLI, HBNBCommand)

    def test_create(self):
        """... tests creation of class User with attributes"""
        self.assertIsInstance(self.obj, User)

    def test_attr_update(self):
        """... checks if proper parameter for name was created"""
        self.CLI.do_User('.update("{}", "first_name", '
                         '"Mongo")'.format(self.obj.id))
        actual = self.obj.first_name
        expected = "Mongo"
        self.assertEqual(expected, actual)

    def test_update_dict(self):
        """... checks if proper parameters created with dict"""
        self.CLI.do_User('.update("{}", {{"last_name": "Nginx", '
                         '"age": 89}})'.format(self.obj.id))
        actual = self.obj.last_name
        expected = 'Nginx'
        self.assertEqual(expected, actual)
        actual = self.obj.age
        expected = 89
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_reupdate(self):
        """... checks if attribute can be reupdated"""
        self.CLI.do_User('.update("{}", "age", 55)'.format(self.obj.id))
        actual = self.obj.age
        expected = 55
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_destroy(self):
        """... checks if object can be destroyed"""
        self.CLI.do_destroy('User {}'.format(self.obj2.id))
        try:
            self.obj2
            self.assertTrue(False)
        except:
            self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main
