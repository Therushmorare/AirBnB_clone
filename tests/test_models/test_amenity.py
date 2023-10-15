#!/usr/bin/python
""" Unit test for amenity """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ Test amenity Class """
    def test_default_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_custom_name(self):
        custom_name = "7 Star-Hotel"
        amenity = Amenity(name=custom_name)
        self.assertEqual(amenity.name, custom_name)

if __name__ == '__main__':
    unittest.main()
