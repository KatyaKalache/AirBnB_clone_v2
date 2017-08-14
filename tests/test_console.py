#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
import models
from datetime import datetime
import console
import inspect
from contextlib import contextmanager
from io import StringIO
import sys

Place = models.Place
State = models.State
User = models.User

HBNBCommand = console.HBNBCommand
FS = console.FS
CNC = models.CNC


@contextmanager
def redirect_streams():
    """function redirects streams: stdout & stderr for testing purposes
    first creates StringIO obj, then saves / updates stdout & stderr"""
    new_stdout, new_stderr = StringIO(), StringIO()
    old_stdout, sys.stdout = sys.stdout, new_stdout
    old_stderr, sys.stderr = sys.stderr, new_stderr
    try:
        # returns new file streams
        yield new_stdout, new_stderr
    finally:
        # restore std streams to the previous value
        sys.stdout, sys.stderr = old_stdout, old_stderr


class TestHBNBcmdDocs(unittest.TestCase):
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
        AF = TestHBNBcmdDocs.all_funcs
        for f in AF:
            if "_HBNBCommand_" in f[0]:
                self.assertTrue(len(f[1].__doc__) > 1)


class TestHBNBcmdCreate(unittest.TestCase):
    """testing instantiation of CLI & create() function"""

    cli = HBNBCommand()

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('.... Test create() w/ params ....')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new Place object: ', end='')
        CLI = TestHBNBcmdCreate.cli
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
            TestHBNBcmdCreate.obj = v

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBcmdCreate.cli
        self.obj = TestHBNBcmdCreate.obj

    def test_instantiation(self):
        """... checks if HBNBCommand CLI Object is properly instantiated"""
        self.assertIsInstance(self.CLI, HBNBCommand)

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(self.obj, CNC['Place'])

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


class TestHBNBcmdErr(unittest.TestCase):
    """Tests create method -> attempts to throw errors with strange params"""

    cli = HBNBCommand()

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('... Can I Kill your program ? ...')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new Place object: ', end='')
        CLI = TestHBNBcmdErr.cli
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
            TestHBNBcmdErr.obj = v

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBcmdErr.cli
        self.obj = TestHBNBcmdErr.obj

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(self.obj, CNC['Place'])

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


class TestHBNBcmdFunc(unittest.TestCase):
    """Test CLI for create, update, destroy Standard Notation"""

    cli = HBNBCommand()

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('.. Testing All other Functions ..')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new State object: ', end='')
        TestHBNBcmdFunc.cli.do_create('State')
        print('')
        fs_o = FS.all()
        for v in fs_o.values():
            TestHBNBcmdFunc.obj = v

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBcmdFunc.cli
        self.obj = TestHBNBcmdFunc.obj

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(self.obj, CNC['State'])

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


class TestHBNBcmdDotNotation(unittest.TestCase):
    """Tests for .function() notation for: .create(), .update(), .destroy()"""

    cli = HBNBCommand()
    obj = None
    obj2 = None

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n..................................')
        print('... Tests .function() notation ....')
        print('..... For HBNBCommand Class ......')
        print('..................................\n\n')
        FS.delete_all()
        print('...creating new User object: ', end='')
        TestHBNBcmdDotNotation.cli.do_User('.create()')
        print('...creating new User object: ', end='')
        TestHBNBcmdDotNotation.cli.do_User('.create()')
        print('')
        fs_o = FS.all()
        for v in fs_o.values():
            if not TestHBNBcmdDotNotation.obj:
                TestHBNBcmdDotNotation.obj = v
            else:
                TestHBNBcmdDotNotation.obj2 = v

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBcmdDotNotation.cli
        self.obj = TestHBNBcmdDotNotation.obj
        self.obj2 = TestHBNBcmdDotNotation.obj2

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


class TestHBNBcmdCount(unittest.TestCase):
    """Tests .count() method for all Classes"""

    cli = HBNBCommand()

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests
        This setup creates an instance of each class"""
        print('\n\n.................................')
        print('..           .count()          ..')
        print('..... Tests for all classes .....')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        CLI = TestHBNBcmdCount.cli
        for k in CNC.keys():
            print('...creating new {} object: '.format(k), end='')
            CLI.do_create(k)
        print('')
        TestHBNBcmdCount.fs_o = FS.all()

    def setUp(self):
        """initializes new HBNBCommand instance and FS obj for each test"""
        self.CLI = TestHBNBcmdCount.cli
        self.FS_O = TestHBNBcmdCount.fs_o

    def test_create_all(self):
        """... tests creation of 1 instance of all classes"""
        check1 = set(v_class for v_class in CNC.values())
        check2 = set(type(v_obj) for v_obj in self.FS_O.values())
        self.assertEqual(check1, check2)

    def test_count_BM(self):
        """... tests .count() method for BaseModel Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_BaseModel('.count()')
        expected = '1\n'
        actual = std_out.getvalue()
        self.assertEqual(expected, actual)

    def test_count_amenity(self):
        """... tests .count() method for Amenity Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_Amenity('.count()')
        expected = '1\n'
        actual = std_out.getvalue()
        self.assertEqual(expected, actual)

    def test_count_city(self):
        """... tests .count() method for City Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_City('.count()')
        expected = '1\n'
        actual = std_out.getvalue()
        self.assertEqual(expected, actual)

    def test_count_state(self):
        """... tests .count() method for State Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_State('.count()')
        expected = '1\n'
        actual = std_out.getvalue()
        self.assertEqual(expected, actual)

    def test_count_user(self):
        """... tests .count() method for User Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_User('.count()')
        expected = '1\n'
        actual = std_out.getvalue()
        self.assertEqual(expected, actual)

    def test_count_review(self):
        """... tests .count() method for Review Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_Review('.count()')
        expected = '1\n'
        actual = std_out.getvalue()
        self.assertEqual(expected, actual)

    def test_count_place(self):
        """... tests .count() method for Place Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_Place('.count()')
        expected = '1\n'
        actual = std_out.getvalue()
        self.assertEqual(expected, actual)


class TestHBNBcmdAll(unittest.TestCase):
    """Tests .all() method for all Classes"""

    cli = HBNBCommand()

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests
        This setup creates an instance of each class"""
        print('\n\n.................................')
        print('..            .all()           ..')
        print('..... Tests for all classes .....')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        CLI = TestHBNBcmdAll.cli
        for k in CNC.keys():
            print('...creating new {} object: '.format(k), end='')
            CLI.do_create(k)
        print('')
        TestHBNBcmdAll.fs_o = FS.all()
        TestHBNBcmdAll.all_ids = list(v.id for v in
                                      TestHBNBcmdAll.fs_o.values())

    def setUp(self):
        """initializes new HBNBCommand instance and FS obj for each test"""
        self.CLI = TestHBNBcmdAll.cli
        self.FS_O = TestHBNBcmdAll.fs_o
        self.all_ids = TestHBNBcmdAll.all_ids

    def test_all_BM(self):
        """... tests .all() method for BaseModel Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_BaseModel('.all()')
        actual = std_out.getvalue()
        self.assertFalse(all(an_id not in actual for an_id in self.all_ids))

    def test_all_amenity(self):
        """... tests .all() method for Amenity Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_Amenity('.all()')
        actual = std_out.getvalue()
        self.assertFalse(all(an_id not in actual for an_id in self.all_ids))

    def test_all_city(self):
        """... tests .all() method for City Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_City('.all()')
        actual = std_out.getvalue()
        self.assertFalse(all(an_id not in actual for an_id in self.all_ids))

    def test_all_state(self):
        """... tests .all() method for State Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_State('.all()')
        actual = std_out.getvalue()
        self.assertFalse(all(an_id not in actual for an_id in self.all_ids))

    def test_all_user(self):
        """... tests .all() method for User Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_User('.all()')
        actual = std_out.getvalue()
        self.assertFalse(all(an_id not in actual for an_id in self.all_ids))

    def test_all_review(self):
        """... tests .all() method for Review Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_Review('.all()')
        actual = std_out.getvalue()
        self.assertFalse(all(an_id not in actual for an_id in self.all_ids))

    def test_all_place(self):
        """... tests .all() method for Place Class"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.do_Place('.all()')
        actual = std_out.getvalue()
        self.assertFalse(all(an_id not in actual for an_id in self.all_ids))


class TestHBNBcmdQuit(unittest.TestCase):
    """Tests Quit, EOF, and unknown input / RTN [Enter] button"""

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests
        This simply tests quit"""
        print('\n\n.................................')
        print('.... quit, EOF & newline CLI ....')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')

    def setUp(self):
        """initializes new HBNBCommand instance and FS obj for each test"""
        self.CLI = HBNBCommand()

    def test_quit_cli(self):
        """... tests 'quit' command from CLI, should quit and return True"""
        FS.delete_all()
        self.assertTrue(self.CLI.do_quit(self.CLI))

    def test_eof_cli(self):
        """... tests EOF  command from CLI, should quit and return True"""
        self.assertTrue(self.CLI.do_EOF(self.CLI))

    def test_carriage_return_cli(self):
        """... tests carriage return should simply print '\n'"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.default('')
        actual = std_out.getvalue()
        self.assertIs(actual, '')

    def test_unknown_cli(self):
        """... tests unknown command should simply print '\n'"""
        with redirect_streams() as (std_out, std_err):
            self.CLI.default('giggly goop magrouple')
        actual = std_out.getvalue()
        self.assertIs(actual, '')


if __name__ == '__main__':
    unittest.main
