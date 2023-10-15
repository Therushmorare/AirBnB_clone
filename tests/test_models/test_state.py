#!/usr/bin/python3
"""Unit test for State
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State

class TestState(unittest.TestCase):
    """ Test State Class """

    def test_default_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_custom_attributes(self):
        custom_name = "Gauteng"
        state = State(name=custom_name)
        self.assertEqual(state.name, custom_name)

if __name__ == '__main__':
    unittest.main()
