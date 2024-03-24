#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
from models import storage

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.state_id = ""
        self.name = ""
