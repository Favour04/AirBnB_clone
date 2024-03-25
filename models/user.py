#!/usr/bin/python3
"""
    This module contain the city user
    class for Airbnb_clone
"""
from models.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
    """
        ATTRIBUTES:
            password - User password
            first_name - User name
            last_name - User last name
            email - User email
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        self.email = ""
