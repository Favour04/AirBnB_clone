#!/usr/bin/python3
import json
from datetime import datetime
import copy

"""
  This module contain the class
  FileStorage that serializes instances
  to a JSON file and deserializes JSON file
  to instances

  Flow of serialization-deserialization will be:
  ==============================================

  <class 'BaseModel'> -> to_dict() -> <class 'dict'> ->
  JSON dump -> <class 'str'> -> FILE -> <class 'str'> ->
  JSON load -> <class 'dict'> -> <class 'BaseModel'>

  ===============================================
"""


class FileStorage:
    """"
        Private class attributes:
        =========================
        * __file_path: string - path to the JSON file (ex: file.json)
        * __objects: dictionary - empty but will store all objects by
        <class name>.id
        (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)

        Public instance methods:
        =======================
        * all(self): returns the dictionary __objects
        * new(self, obj): sets in __objects the obj with key
        <obj class name>.id
        * save(self): serializes __objects to the JSON file (path: __file_path)
        * reload(self): deserializes the JSON file to __objects
        (only if the JSONfile (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
    """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        # The aim of 'objrepr' is to get the id in string
        objrepr = copy.deepcopy(obj)
        objrepr = objrepr.to_dict()
        """ 'BaseModel' + '.' + str(objrepr['id'])
            is the key the object is to be stored
            with. it will be like...
            'BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2'
        """
        self.__objects[str(objrepr["__class__"]) + '.' + str(objrepr['id'])]\
            = obj

    def save(self):
        """
            Lol i had to deepcopy so i can change
            the new obj to a dict without affecting the
            obj in self.__objects
        """
        obj = copy.deepcopy(self.__objects)
        for key in obj.keys():
            if not isinstance(obj[key], dict):
                obj[key] = obj[key].to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(obj, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                content = json.load(file)
                for key in content.keys():
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
                    clasuse = content[key]['__class__']
                    content[key] = classes[clasuse](**content[key])
                self.__objects = content
        except Exception as err:
            print(err)
