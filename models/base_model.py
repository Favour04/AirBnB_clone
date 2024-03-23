from datetime import datetime
from models import storage
from uuid import uuid4
class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            del kwargs["__class__"]
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
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict