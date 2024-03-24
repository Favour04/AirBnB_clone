import sys
sys.path.append('../..') # to access the parent directory
import unittest
from unittest.mock import patch, mock_open
from unittest import mock
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import logging

# Disable logging during test execution
logging.disable(logging.CRITICAL)

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage = None

    def test_all(self):
        # Test if all() returns the correct dictionary of objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.assertEqual(self.storage.all()['BaseModel.{}'.format(obj1.id)], obj1)
        self.assertEqual(self.storage.all()['BaseModel.{}'.format(obj2.id)], obj2)

    def test_new(self):
        # Test if new() adds the object to the dictionary
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all()['BaseModel.{}'.format(obj.id)], obj)