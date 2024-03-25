#!/usr/bin/python3
"""
This module contains the BaseModel class.

BaseModel is the base class for all other classes in the project.
It defines common attributes and methods that are inherited by other classes.
"""
from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): The unique identifier of the instance.
            created_at (datetime): The datetime when the instance was created.
            updated_at (datetime): The datetime when the instance was
            last updated.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            if "__class__" in kwargs:
                del kwargs["__class__"]
            self.__dict__.update(kwargs)
        else:
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: The string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime
          and saves the instance.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: The dictionary representation of the instance.
        """
        dict = {}
        dict.update(self.__dict__)
        dict["__class__"] = f"{self.__class__.__name__}"
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
