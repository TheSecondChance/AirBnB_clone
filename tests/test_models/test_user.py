#!/usr/bin/python3
"""Unittests for models user"""
import models
import unittest
import os
from datetime import datetime
from models.user import User


class Testaleaow(unittest.TestCase):
    """testing to_dict method of the User"""

    def test_dicte(self):
        """Test user to dict"""
        self.assertTrue(dict, type(User().to_dict()))

    def test_correct_keys(self):
        """Test correct ther user key"""
        itmes = User()
        self.assertIn("id", itmes.to_dict())
        self.assertIn("created_at", itmes.to_dict())
        self.assertIn("updated_at", itmes.to_dict())
        self.assertIn("__class__", itmes.to_dict())

    def test_save_usr(self):
        """Test method for save."""
        first = User()
        not_first = first.updated_at
        first.save()
        self.assertNotEqual(first.updated_at, not_first)


if __name__ == "__main__":
    unittest.main()
