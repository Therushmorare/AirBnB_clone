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

    def test_initial_attributes(self):
        self.assertEqual(FileStorage.__file_path, "file.json")
        self.assertEqual(FileStorage.__objects, {})

    def test_new_method(self):
        user = User()
        FileStorage().new(user)
        self.assertIn("User.{}".format(user.id), FileStorage.__objects)

    def test_all_method(self):
        user = User()
        city = City()
        FileStorage().new(user)
        FileStorage().new(city)
        objects = FileStorage().all()
        self.assertEqual(len(objects), 2)
        self.assertIn("User.{}".format(user.id), objects)
        self.assertIn("City.{}".format(city.id), objects)

    def test_save_and_reload_methods(self):
        user = User()
        city = City()
        FileStorage().new(user)
        FileStorage().new(city)
        FileStorage().save()

        self.assertTrue(os.path.isfile(FileStorage.__file_path))

        FileStorage.__objects = {}

        FileStorage().reload()
        objects = FileStorage().all()

        self.assertEqual(len(objects), 2)
        self.assertIn("User.{}".format(user.id), objects)
        self.assertIn("City.{}".format(city.id), objects)

if __name__ == '__main__':
    unittest.main()
