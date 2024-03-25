#!/usr/bin/python3
"""
    This module provides a FileStorage class that handles
    the serialization and deserialization
    of objects to and from a JSON file.
"""
import json
import os


class FileStorage:
    """
    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary that stores all the objects.

    Methods:
        all(self): Returns the dictionary of all objects.
        new(self, obj): Adds a new object to the dictionary.
        save(self): Saves the objects to the JSON file.
        reload(self): Loads the objects from the JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.

        Returns:
            dict: The dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary.

        Args:
            obj: The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the objects to the JSON file.
        """
        obj = {}
        obj.update(FileStorage.__objects)
        for key in obj.keys():
            obj[key] = obj[key].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj, file)

    def reload(self):
        """
        Loads the objects from the JSON file.
        """
        try:
            objects = {}
            with open(FileStorage.__file_path, "r") as file:
                objects = json.load(file)
                for key, value in objects.items():
                    # imported here to prevent circular importation
                    from ..amenity import Amenity
                    from ..base_model import BaseModel
                    from ..city import City
                    from ..place import Place
                    from ..review import Review
                    from ..state import State
                    from ..user import User
                    classes = {
                        'Amenity': Amenity,
                        'BaseModel': BaseModel,
                        'City': City,
                        'Place': Place,
                        'Review': Review,
                        'State': State,
                        'User': User,
                    }
                    if key not in FileStorage.__objects.keys():
                        FileStorage.__objects[key] = classes[value[
                                                    '__class__']](**value)
                    else:
                        continue
        except FileNotFoundError as err:
            FileStorage.__objects = {}
            print(err)
