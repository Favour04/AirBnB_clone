#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
        this class conati.....
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.fromisoformat(str(datetime.now()))
        self.updated_at = datetime.fromisoformat(str(datetime.now()))
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    key = datetime.fromisoformat(value)
                if key == 'updated_at':
                    key = datetime.fromisoformat(value)
            del kwargs['__class__']
            self.__dict__.update(kwargs)
            
        else:
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.fromisoformat(str(datetime.now()))
        storage.save()

    def to_dict(self):
        dict = self.__dict__
        dict["__class__"] = f"{self.__class__.__name__}"
        if not isinstance(dict["created_at"], str):
            dict["created_at"] = \
                    f"{dict['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')}"
        if not isinstance(dict["updated_at"], str):
            dict["updated_at"] = \
                    f"{dict['updated_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')}"
        return dict
