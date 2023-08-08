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
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    kwargs[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at':
                    kwargs[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
            
        else:
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict = {}
        dict.update(self.__dict__)
        dict["__class__"] = f"{self.__class__.__name__}"
        if not isinstance(dict["created_at"], str):
            dict["created_at"] = self.updated_at.isoformat()
        if not isinstance(dict["updated_at"], str):
            dict["updated_at"] = self.updated_at.isoformat()
        return dict
