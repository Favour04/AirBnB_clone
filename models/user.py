#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
from models import storage


"""
    This Module contains the class
    User that inherits from BaseModel
"""


class User(BaseModel):
    """
        Base Model contains the public
        atributes that are self explainaty
        by name
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        if kwargs:
            for key, item in kwargs.items():
                if key == 'password':
                    self.password = item
                elif key == 'first_name':
                    self.first_name = item
                elif key == 'last_name':
                    self.last_name = item
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(item)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(item)
                elif key == 'id':
                    self.id = item
            kwargs = {}
        else:
            storage.new(self)
