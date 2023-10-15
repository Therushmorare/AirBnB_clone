#!/usr/bin/python3
""" Unit test for File_Storage """
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """ Test File Storage Class """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    #FileStorage1 = FileStorage()
    def test_initial_attributes(self):
        FileStorage1 = FileStorage()
        self.assertEqual(FileStorage1.file_path, "file.json")
        self.assertEqual(FileStorage1.objects, {})

    def test_new_method(self):
        FileStorage1 = FileStorage()
        user = User()
        FileStorage().new(user)
        self.assertIn("User.{}".format(user.id), FileStorage1.objects)

    def test_all_method(self):
        user = User()
        city = City()
        FileStorage().new(user)
        FileStorage().new(city)
        objects = FileStorage().all()
        #self.assertEqual(len(objects), 2)
        self.assertIn("User.{}".format(user.id), objects)
        self.assertIn("City.{}".format(city.id), objects)

    def test_save_and_reload_methods(self):
        FileStorage1 = FileStorage()
        user = User()
        city = City()
        FileStorage().new(user)
        FileStorage().new(city)
        FileStorage().save()

        self.assertTrue(os.path.isfile(FileStorage1.file_path))

        FileStorage.objects = {}

        FileStorage().reload()
        objects = FileStorage().all()

        #self.assertEqual(len(objects), 2)
        self.assertIn("User.{}".format(user.id), objects)
        self.assertIn("City.{}".format(city.id), objects)

if __name__ == '__main__':
    unittest.main()
