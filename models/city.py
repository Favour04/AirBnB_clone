#!/usr/bin/python3
"""
    This module defines the City class, which represents
    a city in the AirBnB clone project.
    It contains attributes such as state_id and name.
"""
from models.base_model import BaseModel
from datetime import datetime


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
