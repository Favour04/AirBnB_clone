#!/usr/bin/python3
"""
    This module defines the State class, which
    represent a State in the Airbnb_clone project
"""
from models.base_model import BaseModel
from datetime import datetime


class State(BaseModel):
    """
        ATTRIBUTES:
            - name - Name of the state
    """
    name = ""
