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
        self.assertEqual(r1.width, 4)

        r2 = Rectangle(90, 100, 4, 6)
        self.assertEqual(r2.height, 100)

        r3 = Rectangle(15, 39, 5, 7)
        self.assertEqual(r3.x, 5)

        r4 = Rectangle(15, 65, 20, 50)
        self.assertEqual(r4.y, 50)

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

    def test_raised_exceptions_TypeError_messages(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 4, "5", 5, 12)

        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 4, 5, "5", 12)

        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("1", 4, 5, 5, 12)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, "4", 5, 5, 12)

    def test_raised_exceptions_ValueError_messages(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, -4, 5, 5, 12)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-1, 4, 5, 5, 12)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(1, 4, -5, 5, 12)

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(1, 4, 5, -5, 12)


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


class TestStr(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_str(self):
        r1 = Rectangle(1, 9, 2, 10, 1)
        print(r1)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "[Rectangle] (1) 2/10 - 1/9\n")

    def test_str_exceptions(self):
        with self.assertRaises(TypeError):
            print(Rectangle("1", 2, 3, 5, 1))

        with self.assertRaises(TypeError):
            print(Rectangle(1, "2", 3, 5, 1))

        with self.assertRaises(ValueError):
            print(Rectangle(1, -6, 3, 5, 1))

        with self.assertRaises(ValueError):
            print(Rectangle(1, 6, 3, -5, 1))


class TestCoordinates(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_coordinates(self):
        r1 = Rectangle(2, 3, 2, 2, 1)
        r1.display()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "\n\n  ##\n  ##\n  ##\n")


class TestUpdate(unittest.TestCase):
    def test_update(self):
        r1 = Rectangle(2, 4, 1, 2, 1)
        r1.update(1, 4)
        self.assertEqual(r1.width, 4)

        r1.update(1, 4, 2)
        self.assertEqual(r1.height, 2)

        self.assertEqual(r1.id, 1)

        r1.update(1, 4, 2, 4, 1)
        self.assertEqual(r1.x, 4)

        self.assertEqual(r1.y, 1)

    def test_kwargs(self):
        r2 = Rectangle(2, 4, 1, 2, 1)
        r2.update(height=10)
        self.assertEqual(r2.height, 10)
        r2.update(id=100)
        self.assertEqual(r2.id, 100)
        r2.update(width=6035)
        self.assertEqual(r2.width, 6035)
        r2.update(x=1845)
        self.assertEqual(r2.x, 1845)
        r2.update(y=78)
        self.assertEqual(r2.y, 78)

    def test_exceptions(self):
        r1 = Rectangle(2, 4, 1, 2, 1)
        with self.assertRaises(ValueError):
            r1.update(1, -4)

        with self.assertRaises(ValueError):
            r1.update(1, 4, -1)

        with self.assertRaises(ValueError):
            r1.update(1, 4, 1, -2)

        with self.assertRaises(ValueError):
            r1.update(1, 4, 1, 2, -1)

        with self.assertRaises(TypeError):
            r1.update(1, "fgddsgsdfhf", 4, 5)

    def test_kwargs_exceptions(self):
        r2 = Rectangle(2, 4, 1, 2, 1)
        with self.assertRaises(ValueError):
            r2.update(height=-90)

        with self.assertRaises(TypeError):
            r2.update(width="ufabkshaihfbas")
