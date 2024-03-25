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
        FileStorage.__objects.update({f"{key}": obj})

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
        if not os.path.exists(FileStorage.__file_path):
            # Create the file if it doesn't exist
            with open(FileStorage.__file_path, 'w') as file:
                file.write('{}')

        # Check if the file is empty
        if os.path.getsize(FileStorage.__file_path) == 0:
            # If the file is empty, write '{}' to it
            with open(FileStorage.__file_path, 'w') as file:
                file.write('{}')

        if os.path.exists(FileStorage.__file_path):
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
                        FileStorage.__objects.update({f"{key}": classes[
                                            value['__class__']](**value)})
            except Exception as err:
                print(err)
