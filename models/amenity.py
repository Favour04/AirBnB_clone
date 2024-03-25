#!/usr/bin/python3
"""
This module contains the Amenity class.
"""
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class Amenity(BaseModel):
    """
    This class defines the Amenity object.
        ATTRIBUTES:
        name - name of an amentiy
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
