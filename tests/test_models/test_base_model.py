#!/usr/bin/python3
""" Unit test for base_model
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test Base Model Class """
    def test_default_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_custom_attributes(self):
        custom_id = "custom_id"
        custom_created_at = datetime.now()
        custom_updated_at = datetime.now()
        model = BaseModel(
            id=custom_id,
            created_at=custom_created_at.isoformat(),
            updated_at=custom_updated_at.isoformat(),
            custom_attr="custom_value"
        )

        self.assertEqual(model.id, custom_id)
        self.assertEqual(model.created_at, custom_created_at)
        self.assertEqual(model.updated_at, custom_updated_at)
        self.assertEqual(model.custom_attr, "custom_value")

    def test_save_method(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        custom_id = "custom_id"
        custom_created_at = datetime.now()
        custom_updated_at = datetime.now()
        model = BaseModel(
            id=custom_id,
            created_at=custom_created_at.isoformat(),
            updated_at=custom_updated_at.isoformat(),
            custom_attr="custom_value"
        )

        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["id"], custom_id)
        self.assertEqual(model_dict["created_at"], custom_created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], custom_updated_at.isoformat())
        self.assertEqual(model_dict["custom_attr"], "custom_value")
        self.assertEqual(model_dict["__class__"], "BaseModel")

if __name__ == '__main__':
    unittest.main()

