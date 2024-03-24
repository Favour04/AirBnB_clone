import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_initialization(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes(self):
        city = City()
        city.state_id = "123"
        city.name = "New York"
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "New York")

if __name__ == '__main__':
    unittest.main()