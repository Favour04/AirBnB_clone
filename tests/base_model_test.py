import unittest
from datetime import datetime
from models.base_model import BaseModel


class test_basemodel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, previous_updated_at)

    def test_to_dict_returns_dictionary(self):
        result = self.base_model.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_includes_id(self):
        result = self.base_model.to_dict()
        self.assertIn('id', result)

    def test_to_dict_formats_created_at_and_updated_at(self):
        result = self.base_model.to_dict()
        self.assertIsInstance(result['created_at'], str)
        self.assertIsInstance(result['updated_at'], str)
        self.assertEqual(result['created_at'], self.base_model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(result['updated_at'], self.base_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

    def test_init_with_id(self):
        id_value = '12345'
        model = BaseModel(id=id_value)
        self.assertEqual(model.id, id_value)

    def test_init_with_created_at(self):
        created_at_value = '2023-07-01T12:34:56'


if __name__ == '__main__':
    unittest.main()
