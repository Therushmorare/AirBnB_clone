#!/usr/bin/python3
""" Unit test for User
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User

class TestUser(unittest.TestCase):
    """ Test User Class """
    def test_default_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_custom_attributes(self):
        custom_email = "Tanjiro@DemonSlayer.com"
        custom_password = "RedFlamingSword"
        custom_first_name = "Tanjiro"
        custom_last_name = "Kamado"

        user = User(
            email=custom_email,
            password=custom_password,
            first_name=custom_first_name,
            last_name=custom_last_name
        )

        self.assertEqual(user.email, custom_email)
        self.assertEqual(user.password, custom_password)
        self.assertEqual(user.first_name, custom_first_name)
        self.assertEqual(user.last_name, custom_last_name)

if __name__ == '__main__':
    unittest.main()
