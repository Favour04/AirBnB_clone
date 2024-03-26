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
    password = ""
    first_name = ""
    last_name = ""
    email = ""
