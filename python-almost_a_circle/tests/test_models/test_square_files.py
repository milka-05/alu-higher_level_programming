#!/usr/bin/python3
"""Unit tests for the Square file methods."""
import json
import os
import unittest
from models.base import Base
from models.square import Square


class TestSquareFiles(unittest.TestCase):
    """Tests for Square.save_to_file and Square.load_from_file."""

    def setUp(self):
        """Reset the id counter and remove the old file."""
        Base._Base__nb_objects = 0
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        """Remove the file created by the test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one_square(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(json.load(f),
                             [{"id": 1, "size": 1, "x": 0, "y": 0}])

    def test_load_from_file_missing(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_existing(self):
        s = Square(5, 1, 2, 3)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertIsInstance(loaded[0], Square)
        self.assertIsNot(loaded[0], s)
        self.assertEqual(loaded[0].to_dictionary(), s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
