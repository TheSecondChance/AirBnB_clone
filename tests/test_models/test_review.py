#!/usr/bin/python3
"""Unit tests for Reviw"""
import os
import unittest
from models.review import Review
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test Review"""

    def test_save(self):
        """Test method save"""
        eyta = Review()
        ymeje = eyta.updated_at
        eyta.save()
        self.assertNotEqual(eyta.updated_at, ymeje)


if __name__ == "__main__":
    unittest.main()
