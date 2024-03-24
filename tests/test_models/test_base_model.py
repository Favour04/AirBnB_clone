import unittest
import sys
sys.path.append('../..') # to access the parent directory
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        self.assertEqual(model_str, f"[BaseModel] ({model.id}) {model.__dict__}")

    def test_kwargs(self):
        model = BaseModel()
        model.name = ""
        model.my_number = 89
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertEqual(new_model.name, model.name)
        self.assertEqual(new_model.my_number, model.my_number)

if __name__ == '__main__':
    unittest.main()