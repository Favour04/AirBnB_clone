import json
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects.update({f"{key}": obj})

    def save(self):
        obj = {}
        obj.update(FileStorage.__objects)
        for key in obj.keys():
            obj[key] = obj[key].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj, file)

    def reload(self):
        try:
            objects = {}
            with open(FileStorage.__file_path, "r") as file:
                objects = json.load(file)
                for key, value in objects.items():
                    # imported here to prevent circular importation
                    # from ..amenity import Amenity
                    from ..base_model import BaseModel
                    # from ..city import City
                    # from ..place import Place
                    # from ..review import Review
                    # from ..state import State
                    # from ..user import User
                    classes = {
                        # 'Amenity': Amenity,
                        'BaseModel': BaseModel,
                        # 'City': City,
                        # 'Place': Place,
                        # 'Review': Review,
                        # 'State': State,
                        # 'User': User,
                    }
                    FileStorage.__objects.update({f"{key}": classes[value['__class__']](**value)})
        except Exception as err:
            print(err)