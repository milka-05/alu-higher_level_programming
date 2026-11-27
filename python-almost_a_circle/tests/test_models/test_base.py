#!/usr/bin/python3
"""Unit tests for Base class."""
import json
import os
import unittest

try:
    from models.base import Base
    HAS_MODELS = True
except ImportError:
    HAS_MODELS = False


class TestBase(unittest.TestCase):
    """Test Base behavior."""

    def setUp(self):
        """Reset private counter if available."""
        if HAS_MODELS and hasattr(Base, "_Base__nb_objects"):
            Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove generated JSON files."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    @unittest.skipUnless(HAS_MODELS, "models.base not yet present")
    def test_id_assignment(self):
        """Test automatic and custom id values."""
        b1 = Base()
        b2 = Base(42)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 42)
        self.assertEqual(b3.id, 2)

    @unittest.skipUnless(HAS_MODELS, "models.base not yet present")
    def test_json_helpers(self):
        """Test to_json_string and from_json_string."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        raw = Base.to_json_string([{"id": 9}])
        self.assertEqual(json.loads(raw), [{"id": 9}])
        self.assertEqual(Base.from_json_string(raw), [{"id": 9}])


if __name__ == "__main__":
    unittest.main()
