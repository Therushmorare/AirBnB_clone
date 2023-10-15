#!/usr/bin/python3
"""Unit test for review
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

class TestReview(unittest.TestCase):
    """ Test Review Class """

    def test_default_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_custom_attributes(self):
        custom_place_id = "place_id_123"
        custom_user_id = "user_id_456"
        custom_text = "I was scared half of the time,so it was not worth it.."

        review = Review(
            place_id=custom_place_id,
            user_id=custom_user_id,
            text=custom_text
        )

        self.assertEqual(review.place_id, custom_place_id)
        self.assertEqual(review.user_id, custom_user_id)
        self.assertEqual(review.text, custom_text)

if __name__ == '__main__':
    unittest.main()
