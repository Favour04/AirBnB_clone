#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
from models import storage


"""
    This Module contains the class
    City that inherits from BaseModel
"""


class City(BaseModel):
    """
        City inherit from the class basemodel
        and it contains some public
        atributes that are self explainaty
        by name
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.state_id = ""
        self.name = ""
        if kwargs:
            for key, item in kwargs.items():
                if key == 'name':
                    self.name = item
                elif key == 'state_id':
                    self.state_id = item
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(item)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(item)
                elif key == 'id':
                    self.id = item
            kwargs = {}
        else:
            storage.new(self)
