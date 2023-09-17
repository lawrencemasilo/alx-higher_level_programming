#!/usr/bin/python3
"""This is a unittest for the Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_id(self):
        """tests the id value"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(90, 100, 4, 6)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(90, 100, 4, 6, 50)
        self.assertEqual(r3.id, 50)

    def test_io_value(self):
        """Tests input output values"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.get_width, 4)

        r2 = Rectangle(90, 100, 4, 6)
        self.assertEqual(r2.get_height, 100)

        r3 = Rectangle(15, 39, 5, 7)
        self.assertEqual(r3.get_x, 5)

        r4 = Rectangle(15, 65, 20, 50)
        self.assertEqual(r4.get_y, 50)

    def test_raised_exceptions(self):
        """Tests the raised exceptions"""
        with self.assertRaises(ValueError):
            Rectangle(4, -2, 5, 5, 12)

        with self.assertRaises(ValueError):
            Rectangle(-4, 2, 5, 5, 12)

        with self.assertRaises(ValueError):
            Rectangle(0, 2, 5, 5, 12)

        with self.assertRaises(ValueError):
            Rectangle(4, 0, 5, 5, 12)

        with self.assertRaises(ValueError):
            Rectangle(4, 2, -1, 5, 12)

        with self.assertRaises(ValueError):
            Rectangle(4, 2, 1, -5, 12)

        with self.assertRaises(TypeError):
            Rectangle("1", 4, 5, 5, 12)

        with self.assertRaises(TypeError):
            Rectangle(1, "4", 5, 5, 12)

        with self.assertRaises(TypeError):
            Rectangle(1, 4, "5", 5, 12)

        with self.assertRaises(TypeError):
            Rectangle(1, 4, 5, "5", 12)
