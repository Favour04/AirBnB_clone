#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
from models import storage


"""
    This Module contains the class
    Place that inherits from BaseModel
"""
class Place(BaseModel):
    """
        Place inherit from the class basemodel
        and it contains some public
        atributes that are self explainaty
        by name
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
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
        if kwargs:
            for key, item in kwargs.items():
                if key == 'city_id':
                    self.city_id = item
                elif key == 'user_id':
                    self.user_id = item
                elif key == 'name':
                    self.name = item
                elif key == 'description':
                    self.description = item
                elif key == 'number_rooms':
                    self.number_rooms = item
                elif key == 'number_bathrooms':
                    self.number_bathrooms = item
                elif key == 'max_guest':
                    self.max_guest = item
                elif key == 'price_by_night':
                    self.price_by_night = item
                elif key == 'latitude':
                    self.latitude = item
                elif key == 'longitude':
                    self.longitude = item
                elif key == 'amenity_ids':
                    self.amenity_ids = item
                elif key == 'name':
                    self.name = item 
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(item)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(item)
                elif key == 'id':
                    self.id = item 
            kwargs = {}
        else:
            storage.new(self)
