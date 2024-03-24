import unittest
import sys
sys.path.append('../..') # to access the parent directory
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Review class for testing
        self.review = Review()

    def test_inherited_attributes(self):
        # Test inherited attributes from BaseModel
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_inherited_methods(self):
        # Test inherited methods from BaseModel
        self.assertTrue(hasattr(self.review, 'save'))
        self.assertTrue(hasattr(self.review, 'to_dict'))


    def test_place_id(self):
        # Test the place_id attribute
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        # Test the user_id attribute
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        # Test the text attribute
        self.assertEqual(self.review.text, "")

if __name__ == '__main__':
    unittest.main()