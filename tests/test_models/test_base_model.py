#!/usr/bin/python3
"""Test the BaseModle"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_init_method(unittest.TestCase):
    """Test init method

    Args:
        unittest (init): TestCase inheret from unittest module
    """

    def setUp(self):
        """Setup temp_model to BaseModel()"""
        self.temp_model = BaseModel()

    def test__init__(self):
        """Test init method"""
        self.assertIsInstance(self.temp_model.created_at, datetime)
        self.assertIsInstance(self.temp_model.updated_at, datetime)
        self.assertTrue(self.temp_model.id)
        self.assertIsNotNone(self.temp_model.id)
        self.assertIsNotNone(self.temp_model.created_at)
        self.assertIsNotNone(self.temp_model.updated_at)
        self.assertIsInstance(self.temp_model.id, str)

    def test_save(self):
        """Test save method"""
        start_update = self.temp_model.updated_at
        current_updated = self.temp_model.save()
        self.assertNotEqual(start_update, current_updated)


class Tedict(unittest.TestCase):
    def setUp(self):
        """Setup temp_model to BaseModel()"""
        self.temp_model = BaseModel()

    def test_to_dict(self):
        """Test to_dict method"""
        dict_check = self.temp_model.to_dict()
        self.assertIn("id", dict_check.keys())
        self.assertIn("created_at", dict_check.keys())
        self.assertIn("updated_at", dict_check.keys())
        self.assertIsInstance(dict_check, dict)
        self.assertEqual(dict_check["__class__"], "BaseModel")
        self.assertEqual(dict_check["id"], self.temp_model.id)
        self.assertEqual(
            dict_check["created_at"], self.temp_model.created_at.isoformat()
        )
        self.assertEqual(
            dict_check["updated_at"], self.temp_model.updated_at.isoformat()
        )

    def test_dict_attribute(self):
        """Test dict attribute"""
        self.temp_model.name = "Hello world"
        self.temp_model.my_number = 2016

        check_dict = self.temp_model.to_dict()

        self.assertIn("name", check_dict)
        self.assertIn("my_number", check_dict)
        self.assertEqual(check_dict["name"], "Hello world")
        self.assertEqual(check_dict["my_number"], 2016)


class Test_str(unittest.TestCase):
    def setUp(self):
        """Setup temp_model to BaseModel()"""
        self.temp_model = BaseModel()

    def test__str__(self):
        """Test __str__ method"""
        self.assertTrue(str(self.temp_model).startswith("[BaseModel]"))
        self.assertIn(self.temp_model.id, str(self.temp_model))
        self.assertIn(str(self.temp_model.__dict__), str(self.temp_model))
        must_be = f"""
        [{type(self.temp_model).__name__}]
        ({self.temp_model.id})
        {self.temp_model.__dict__}
        """
        self.assertEqual(self.temp_model.__str__(), must_be)


if __name__ == "__main__":
    unittest.main()
