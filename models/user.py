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
