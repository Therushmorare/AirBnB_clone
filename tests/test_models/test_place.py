#!/usr/bin/python3
"""Unit test for Place
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlace(unittest.TestCase):
    """ Test Place Class """

    def test_default_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_custom_attributes(self):
        custom_city_id = "city_id_123"
        custom_user_id = "user_id_456"
        custom_name = "Crazy Mension"
        custom_description = "Scarry things happen in here, think of this place as living in a house with Chucky"
        custom_number_rooms = 10
        custom_number_bathrooms = 5
        custom_max_guest = 20
        custom_price_by_night = 230
        custom_latitude = 45.123
        custom_longitude = -78.456
        custom_amenity_ids = ["amenity1", "amenity2"]

        place = Place(
            city_id=custom_city_id,
            user_id=custom_user_id,
            name=custom_name,
            description=custom_description,
            number_rooms=custom_number_rooms,
            number_bathrooms=custom_number_bathrooms,
            max_guest=custom_max_guest,
            price_by_night=custom_price_by_night,
            latitude=custom_latitude,
            longitude=custom_longitude,
            amenity_ids=custom_amenity_ids
        )

        self.assertEqual(place.city_id, custom_city_id)
        self.assertEqual(place.user_id, custom_user_id)
        self.assertEqual(place.name, custom_name)
        self.assertEqual(place.description, custom_description)
        self.assertEqual(place.number_rooms, custom_number_rooms)
        self.assertEqual(place.number_bathrooms, custom_number_bathrooms)
        self.assertEqual(place.max_guest, custom_max_guest)
        self.assertEqual(place.price_by_night, custom_price_by_night)
        self.assertEqual(place.latitude, custom_latitude)
        self.assertEqual(place.longitude, custom_longitude)
        self.assertEqual(place.amenity_ids, custom_amenity_ids)

if __name__ == '__main__':
    unittest.main()
