#!/usr/bin/python3
"""
    This Module defines the the the Place class
    of the Airbnb_clone project which represent
    a Place
"""
from models.base_model import BaseModel
from datetime import datetime


class Place(BaseModel):
    """
        ATTRIBUTES:
            city_id - Id of the City the place is
            user_id - Id of the User
            name - Name of place
            description - Place description
            number_rooms - Number of rooms in the place
            number_bathrooms - Number of bathrooms in the place
            max_guest - Maximum number of guests the place can
            contain
            price_by_night - Price per night
            latitude - Latitude of the place
            longitude - Longitude of the place
            amenity_ids - List of Amenity ids
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
