#!/usr/bin/python3
"""Unit tests for create, save_to_file and load_from_file."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestFileMethods(unittest.TestCase):
    """Tests for create, save_to_file and load_from_file."""

    def setUp(self):
        """Reset the id counter and remove old files."""
        Base._Base__nb_objects = 0
        self.clean()

    def tearDown(self):
        """Remove the files created by the tests."""
        self.clean()

    @staticmethod
    def clean():
        """Remove the JSON files if they exist."""
        for name in ("Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_rectangle_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)

    def test_rectangle_create_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_rectangle_create_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_rectangle_create_x(self):
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r = Rectangle.create(**d)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_rectangle_create_y(self):
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.to_dictionary(), d)

    def test_rectangle_create_is_new_object(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_square_create(self):
        d = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s = Square.create(**d)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.to_dictionary(), d)
        self.assertEqual(Square.create(**{'id': 89}).id, 89)
        self.assertEqual(Square.create(**{'id': 89, 'size': 4}).size, 4)

    def test_rectangle_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_one(self):
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        with open("Rectangle.json") as f:
            content = f.read()
        self.assertIsInstance(content, str)
        self.assertEqual(json.loads(content),
                         [{"id": 1, "width": 1, "height": 2,
                           "x": 0, "y": 0}])

    def test_rectangle_save_two(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            data = json.load(f)
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_rectangle_save_overwrites(self):
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6)])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.load(f)), 1)

    def test_square_save(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        s = Square(1, 0, 0, 1)
        Square.save_to_file([s])
        with open("Square.json") as f:
            self.assertEqual(json.load(f), [s.to_dictionary()])

    def test_rectangle_load_missing(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_existing(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertIsInstance(loaded, list)
        self.assertEqual(len(loaded), 2)
        self.assertIsInstance(loaded[0], Rectangle)
        self.assertIsNot(loaded[0], r1)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_square_load(self):
        self.assertEqual(Square.load_from_file(), [])
        s = Square(5, 1, 2, 3)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertIsInstance(loaded[0], Square)
        self.assertIsNot(loaded[0], s)
        self.assertEqual(loaded[0].to_dictionary(), s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
