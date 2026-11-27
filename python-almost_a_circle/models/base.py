#!/usr/bin/python3
"""Module that defines the Base class."""
import csv
import json


class Base:
    """Base class that manages the id of all the other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Set the id, or count a new object if id is None."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of a list of objects to <Class>.json."""
        data = []
        if list_objs is not None:
            data = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(data))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class>.json."""
        try:
            with open(cls.__name__ + ".json") as f:
                data = cls.from_json_string(f.read())
        except IOError:
            return []
        return [cls.create(**item) for item in data]

    @classmethod
    def _csv_fields(cls):
        """Return the CSV column names of the class."""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        return ["id", "size", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write a list of objects to <Class>.csv."""
        fields = cls._csv_fields()
        with open(cls.__name__ + ".csv", "w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs or []:
                writer.writerow([getattr(obj, key) for key in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from <Class>.csv."""
        fields = cls._csv_fields()
        try:
            with open(cls.__name__ + ".csv", newline="") as f:
                rows = [row for row in csv.reader(f) if row]
        except IOError:
            return []
        return [cls.create(**dict(zip(fields, map(int, row))))
                for row in rows]
