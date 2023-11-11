#!/usr/bin/python3
"""Create Test"""
import unittest
from datetime import datetime
from models.state import State


class Test_state(unittest.TestCase):
    """want to pass"""

    def test_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test__init(self):
        self.assertEqual(State, type(State()))
