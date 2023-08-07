#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
from models import storage


"""
    This Module contains the class
    Review that inherits from BaseModel
"""
class Review(BaseModel):
    """
        Review inherit from the class basemodel
        and it contains some public
        atributes that are self explainaty
        by name
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        if kwargs:
            for key, item in kwargs.items():
                if key == 'place_id':
                    self.place_id = item
                if key == 'user_id':
                    self.user_id = item
                if key == 'text':
                    self.text = item
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(item)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(item)
                elif key == 'id':
                    self.id = item
            kwargs = {}
        else:
            storage.new(self)
