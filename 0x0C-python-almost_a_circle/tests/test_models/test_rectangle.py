#!/usr/bin/python3
"""This is a unittest for the Rectangle class"""
import unittest
from models.rectangle import Rectangle
import sys
from io import StringIO


class TestBaseClass(unittest.TestCase):
    def test_id(self):
        """tests the id value"""
        r1 = Rectangle(4, 5, 1, 2, 1)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(90, 100, 4, 6, 3)
        self.assertEqual(r2.id, 3)

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


class TestArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Rectangle(4, 6).area(), 24)

        self.assertEqual(Rectangle(6, 2).area(), 12)

        self.assertEqual(Rectangle(5, 10, 10, 12, 15).area(), 50)

    def test_area_exceptions(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 4, 5, 5, 12).area()

        with self.assertRaises(ValueError):
            Rectangle(1, -4, 5, 5, 12).area()


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_display(self):
        Rectangle(4, 6).display()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "####\n####\n####\n####\n####\n####\n")

    def test_display_exceptions(self):
        with self.assertRaises(TypeError):
            Rectangle(4, "6").display()

        with self.assertRaises(TypeError):
            Rectangle("4", 6).display()

        with self.assertRaises(ValueError):
            Rectangle(-4, 6).display()

        with self.assertRaises(ValueError):
            Rectangle(4, -6).display()
