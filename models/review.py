#!/usr/bin/python3
"""
    This Module defines the the the review class
    of thr Airbnb_clone project which represent
    a review of a place
"""
from models.base_model import BaseModel
from datetime import datetime


class Review(BaseModel):
    """
        ATTRIBUTES:
            - place_id - Id of the place reviewed
            - user_id - Id of the user reviewing
            - text - Review text
    """
    place_id = ""
    user_id = ""
    text = ""
