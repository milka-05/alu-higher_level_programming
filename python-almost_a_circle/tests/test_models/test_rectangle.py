#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import unittest

try:
    from models.base import Base
    from models.rectangle import Rectangle
    HAS_RECT = True
except ImportError:
    HAS_RECT = False


class TestRectangle(unittest.TestCase):
    """Test Rectangle behavior and validation."""

    def setUp(self):
        """Reset Base counter if available."""
        if HAS_RECT and hasattr(Base, "_Base__nb_objects"):
            Base._Base__nb_objects = 0

    @unittest.skipUnless(HAS_RECT, "models.rectangle not yet present")
    def test_init_area_str_dict(self):
        """Test instantiation, area, __str__, and to_dictionary."""
        r = Rectangle(4, 2, 1, 3, 7)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.area(), 8)
        self.assertEqual(str(r), "[Rectangle] (7) 1/3 - 4/2")
        self.assertEqual(
            r.to_dictionary(),
            {"id": 7, "width": 4, "height": 2, "x": 1, "y": 3},
        )

    @unittest.skipUnless(HAS_RECT, "models.rectangle not yet present")
    def test_validation_errors(self):
        """Test TypeError and ValueError for invalid inputs."""
        with self.assertRaises(TypeError):
            Rectangle("4", 2)
        with self.assertRaises(TypeError):
            Rectangle(4, "2")
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(4, -1)
        with self.assertRaises(ValueError):
            Rectangle(4, 2, -1, 0)


if __name__ == "__main__":
    unittest.main()
