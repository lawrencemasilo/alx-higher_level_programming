#!/usr/bin/python3
"""This is a unittest for the Square class"""
import unittest
from models.square import Square
import sys
from io import StringIO


class TestBaseClass(unittest.TestCase):
    def test_id(self):
        """tests the id value"""
        s1 = Square(4, 1, 2, 1)
        self.assertEqual(s1.id, 1)

        s2 = Square(90, 4, 6, 3)
        self.assertEqual(s2.id, 3)

        s3 = Square(90, 4, 6, 50)
        self.assertEqual(s3.id, 50)

    def test_io_value(self):
        """Tests input output values"""
        s1 = Square(4)
        self.assertEqual(s1.get_width, 4)

        s2 = Square(100, 4, 6)
        self.assertEqual(s2.get_height, 100)

        s3 = Square(15, 5, 7)
        self.assertEqual(s3.get_x, 5)

        s4 = Square(15, 20, 50)
        self.assertEqual(s4.get_y, 50)

    def test_raised_exceptions(self):
        """Tests the raised exceptions"""
        with self.assertRaises(ValueError):
            Square(-2, 5, 5, 12)

        with self.assertRaises(ValueError):
            Square(-4, 5, 5, 12)

        with self.assertRaises(ValueError):
            Square(0, 5, 5, 12)

        with self.assertRaises(ValueError):
            Square(2, -1, 5, 12)

        with self.assertRaises(ValueError):
            Square(2, 1, -5, 12)

        with self.assertRaises(TypeError):
            Square("1", 5, 5, 12)

        with self.assertRaises(TypeError):
            Square(1, "5", 5, 12)

        with self.assertRaises(TypeError):
            Square(4, 5, "5", 12)


class TestArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Square(4).area(), 16)

        self.assertEqual(Square(6).area(), 36)

        self.assertEqual(Square(5, 10, 12, 15).area(), 25)

    def test_area_exceptions(self):
        with self.assertRaises(ValueError):
            Square(-1, 4, 5, 12).area()

        with self.assertRaises(ValueError):
            Square(-4, 5, 5, 12).area()


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_display(self):
        Square(4).display()
        output = sys.stdout.getvalue()
        self.assertEqual(output, "####\n####\n####\n####\n")

    def test_display_exceptions(self):
        with self.assertRaises(TypeError):
            Square("6").display()

        with self.assertRaises(TypeError):
            Square("4").display()

        with self.assertRaises(ValueError):
            Square(-4).display()

        with self.assertRaises(ValueError):
            Square(-6).display()


class TestStr(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_str(self):
        s1 = Square(1, 2, 10, 1)
        print(s1)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "[Square] (1) 2/10 - 1\n")

    def test_str_exceptions(self):
        with self.assertRaises(TypeError):
            print(Square("1", 3, 5, 1))

        with self.assertRaises(TypeError):
            print(Square("2", 3, 5, 1))

        with self.assertRaises(ValueError):
            print(Square(-6, 3, 5, 1))

        with self.assertRaises(ValueError):
            print(Square(6, 3, -5, 1))


"""
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
        self.assertEqual(r1.get_width, 4)

        r1.update(1, 4, 2)
        self.assertEqual(r1.get_height, 2)

        self.assertEqual(r1.id, 1)

        r1.update(1, 4, 2, 4, 1)
        self.assertEqual(r1.get_x, 4)

        self.assertEqual(r1.get_y, 1)

    def test_kwargs(self):
        r2 = Rectangle(2, 4, 1, 2, 1)
        r2.update(height=10)
        self.assertEqual(r2.get_height, 10)
        r2.update(id=100)
        self.assertEqual(r2.id, 100)
        r2.update(width=6035)
        self.assertEqual(r2.get_width, 6035)
        r2.update(x=1845)
        self.assertEqual(r2.get_x, 1845)
        r2.update(y=78)
        self.assertEqual(r2.get_y, 78)

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

"""
