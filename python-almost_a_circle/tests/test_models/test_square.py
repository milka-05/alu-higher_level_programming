#!/usr/bin/python3
"""Unit tests for the Square class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

BAD_TYPES = ("a", 1.5, None, [1], (1,), {1}, {"a": 1})


def output_of(func):
    """Return what func prints."""
    with patch("sys.stdout", new_callable=io.StringIO) as out:
        func()
    return out.getvalue()


class TestSquare(unittest.TestCase):
    """Tests for Square."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_ids(self):
        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1).id, 2)
        self.assertEqual(Square(1, id=9).id, 9)
        self.assertEqual(Square(1).id, 3)

    def test_attributes(self):
        s = Square(5, 2, 3, 7)
        self.assertEqual((s.size, s.x, s.y, s.id), (5, 2, 3, 7))
        self.assertEqual((s.width, s.height), (5, 5))

    def test_defaults(self):
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_missing_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_type_errors(self):
        for bad in BAD_TYPES:
            with self.subTest(value=bad):
                with self.assertRaisesRegex(TypeError,
                                            "must be an integer"):
                    Square(bad)

    def test_size_value_errors(self):
        for bad in (0, -1, -20):
            with self.subTest(value=bad):
                with self.assertRaisesRegex(ValueError, "must be > 0"):
                    Square(bad)

    def test_x_y_errors(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "a")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "a")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -1)

    def test_size_setter(self):
        s = Square(5)
        s.size = 9
        self.assertEqual((s.size, s.width, s.height), (9, 9, 9))

    def test_size_setter_validates(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "must be an integer"):
            s.size = "a"
        with self.assertRaisesRegex(ValueError, "must be > 0"):
            s.size = 0
        self.assertEqual(s.size, 5)

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(1).area(), 1)

    def test_display(self):
        self.assertEqual(output_of(Square(2).display), "##\n##\n")
        self.assertEqual(output_of(Square(2, 1, 1).display),
                         "\n ##\n ##\n")

    def test_str(self):
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(5, 2, 3, 12)), "[Square] (12) 2/3 - 5")

    def test_update_args(self):
        s = Square(5, 0, 0, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")
        self.assertEqual((s.width, s.height), (2, 2))

    def test_update_kwargs(self):
        s = Square(5, 0, 0, 1)
        s.update(size=7)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 7")
        s.update(x=2, y=3)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 7")
        s.update(y=1, size=2, id=89, x=3)
        self.assertEqual(str(s), "[Square] (89) 3/1 - 2")

    def test_update_args_before_kwargs(self):
        s = Square(5, 0, 0, 1)
        s.update(89, id=5, size=3)
        self.assertEqual((s.id, s.size), (89, 5))

    def test_update_no_args(self):
        s = Square(5, 1, 2, 3)
        s.update()
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_unknown_kwarg(self):
        s = Square(5, 1, 2, 3)
        s.update(foo=1)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_validates(self):
        s = Square(5, 1, 2, 3)
        with self.assertRaisesRegex(TypeError, "must be an integer"):
            s.update(1, "a")
        with self.assertRaisesRegex(ValueError, "must be > 0"):
            s.update(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-1)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 7)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 7, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_is_a_copy(self):
        s = Square(10, 2, 1, 7)
        s.to_dictionary()["size"] = 99
        self.assertEqual(s.size, 10)

    def test_to_dictionary_update_round_trip(self):
        s1 = Square(10, 2, 1, 7)
        s2 = Square(1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_to_dictionary_with_arg(self):
        with self.assertRaises(TypeError):
            Square(1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
