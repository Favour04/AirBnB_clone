import unittest
import sys
sys.path.append('../..') # to access the parent directory
from models.state import State
from models.base_model import BaseModel
class TestState(unittest.TestCase):

    def test_state_inherits_from_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_state_attributes_types(self):
        state = State()
        self.assertEqual(type(state.name), str)

if __name__ == '__main__':
    unittest.main()
