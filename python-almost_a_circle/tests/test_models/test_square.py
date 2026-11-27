#!/usr/bin/python3
"""Unit tests for Square class."""
import unittest

try:
    from models.base import Base
    from models.square import Square
    HAS_SQUARE = True
except ImportError:
    HAS_SQUARE = False


class TestSquare(unittest.TestCase):
    """Test Square behavior and validation."""

    def setUp(self):
        """Reset Base counter if available."""
        if HAS_SQUARE and hasattr(Base, "_Base__nb_objects"):
            Base._Base__nb_objects = 0

    @unittest.skipUnless(HAS_SQUARE, "models.square not yet present")
    def test_size_update_dict(self):
        """Test Square size property, update, and to_dictionary."""
        s = Square(5, 0, 0, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.area(), 25)
        s.size = 6
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)
        s.update(8, 2, 1, 1)
        self.assertEqual(str(s), "[Square] (8) 1/1 - 2")
        self.assertEqual(
            s.to_dictionary(),
            {"id": 8, "size": 2, "x": 1, "y": 1},
        )

    @unittest.skipUnless(HAS_SQUARE, "models.square not yet present")
    def test_square_errors(self):
        """Test Square validation errors."""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-2)


if __name__ == "__main__":
    unittest.main()
