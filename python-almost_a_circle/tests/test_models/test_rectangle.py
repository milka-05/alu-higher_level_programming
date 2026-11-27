#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle

BAD_TYPES = ("a", 1.5, None, [1], (1,), {1}, {"a": 1})


def build(attr, value):
    """Build a valid Rectangle where attr is replaced by value."""
    args = {"width": 1, "height": 2, "x": 0, "y": 0}
    args[attr] = value
    return Rectangle(**args)


def output_of(func):
    """Return what func prints."""
    with patch("sys.stdout", new_callable=io.StringIO) as out:
        func()
    return out.getvalue()


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_is_base(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        self.assertEqual(Rectangle(1, 2).id, 1)
        self.assertEqual(Rectangle(1, 2).id, 2)
        self.assertEqual(Rectangle(1, 2, id=7).id, 7)
        self.assertEqual(Rectangle(1, 2).id, 3)

    def test_attributes(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_defaults(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_missing_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_type_errors(self):
        for attr in ("width", "height", "x", "y"):
            for bad in BAD_TYPES:
                with self.subTest(attr=attr, value=bad):
                    with self.assertRaises(TypeError) as ctx:
                        build(attr, bad)
                    self.assertEqual(str(ctx.exception),
                                     attr + " must be an integer")

    def test_width_height_value_errors(self):
        for attr in ("width", "height"):
            for bad in (0, -1, -50):
                with self.subTest(attr=attr, value=bad):
                    with self.assertRaises(ValueError) as ctx:
                        build(attr, bad)
                    self.assertEqual(str(ctx.exception),
                                     attr + " must be > 0")

    def test_x_y_value_errors(self):
        for attr in ("x", "y"):
            for bad in (-1, -50):
                with self.subTest(attr=attr, value=bad):
                    with self.assertRaises(ValueError) as ctx:
                        build(attr, bad)
                    self.assertEqual(str(ctx.exception),
                                     attr + " must be >= 0")

    def test_x_y_zero_allowed(self):
        r = Rectangle(1, 2, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_validation_order(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a", "b", "c", "d")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "b", "c", "d")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "c", "d")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "d")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, "b")

    def test_setters(self):
        r = Rectangle(1, 2)
        r.width = 10
        r.height = 20
        r.x = 3
        r.y = 4
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 20, 3, 4))

    def test_setters_validate(self):
        r = Rectangle(1, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "a"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -1
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = 2.5

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_after_change(self):
        r = Rectangle(3, 2)
        r.width = 10
        self.assertEqual(r.area(), 20)

    def test_area_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).area(1)

    def test_display(self):
        self.assertEqual(output_of(Rectangle(2, 3).display), "##\n##\n##\n")
        self.assertEqual(output_of(Rectangle(1, 1).display), "#\n")

    def test_display_with_x_y(self):
        self.assertEqual(output_of(Rectangle(2, 2, 2, 1).display),
                         "\n  ##\n  ##\n")
        self.assertEqual(output_of(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")
        self.assertEqual(output_of(Rectangle(1, 1, 0, 2).display),
                         "\n\n#\n")

    def test_display_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).display(1)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)), "[Rectangle] (1) 1/0 - 5/5")

    def test_print(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(output_of(lambda: print(r)),
                         "[Rectangle] (12) 2/1 - 4/6\n")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_args_before_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, id=5, width=3)
        self.assertEqual((r.id, r.width), (89, 10))

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_unknown_kwarg(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(foo=3)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_validates(self):
        r = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "a")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 2, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="b")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 5, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_to_dictionary_is_a_copy(self):
        r = Rectangle(10, 2, 1, 9, 5)
        r.to_dictionary()["width"] = 99
        self.assertEqual(r.width, 10)

    def test_to_dictionary_update_round_trip(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_to_dictionary_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
