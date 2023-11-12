#!/usr/bin/python3
"""Unittes models"""
import models
import unittest
from models import storage
from datetime import datetime
from models.user import User


class Testaleaow(unittest.TestCase):
    """Test method of the User"""

    def test_conve_dicte(self):
        """Test conver to dict"""
        self.assertTrue(dict, type(User().to_dict()))

    def test_keys(self):
        """Test key"""
        itmes = User()
        self.assertIn("id", itmes.to_dict())
        self.assertIn("created_at", itmes.to_dict())
        self.assertIn("updated_at", itmes.to_dict())
        self.assertIn("__class__", itmes.to_dict())

    def test_tkel(self):
        """Test method check"""
        yemejeme = User()
        behula = yemejeme.updated_at
        yemejeme.save()
        self.assertNotEqual(yemejeme.updated_at, behula)


if __name__ == "__main__":
    unittest.main()
