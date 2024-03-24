#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
from models import storage

class User(BaseModel):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        
