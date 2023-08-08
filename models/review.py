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
