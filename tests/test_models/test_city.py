#!/usr/bin/python3
""" Unit test City
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City

class TestCity(unittest.TestCase):
    """ Test City Class """

    def test_default_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_custom_attributes(self):
        custom_state_id = "GP"
        custom_name = "Pretoria"
        city = City(state_id=custom_state_id, name=custom_name)
        self.assertEqual(city.state_id, custom_state_id)
        self.assertEqual(city.name, custom_name)

    def test_to_dict_method(self):
        custom_state_id = "GP"
        custom_name = "Pretoria"
        city = City(state_id=custom_state_id, name=custom_name)

        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["state_id"], custom_state_id)
        self.assertEqual(city_dict["name"], custom_name)
        self.assertEqual(city_dict["__class__"], "City")

if __name__ == '__main__':
    unittest.main()
