#!/usr/bin/python3
"""This is a unittest for the Base class"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    def test_io_value(self):
        """Tests input output values"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base(15)
        self.assertEqual(b5.id, 15)
        b6 = Base(15 + 65 + 20 + 50)
        self.assertEqual(b6.id, 150)
        b7 = Base(-5)
        self.assertEqual(b7.id, -5)
        b8 = Base("neo")
        self.assertEqual(b8.id, "neo")
