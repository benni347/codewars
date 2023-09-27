import unittest
from planet_by_id import get_planet_name


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(get_planet_name(2), "Venus")
        self.assertEqual(get_planet_name(5), "Jupiter")
        self.assertEqual(get_planet_name(3), "Earth")
        self.assertEqual(get_planet_name(4), "Mars")
        self.assertEqual(get_planet_name(8), "Neptune")
        self.assertEqual(get_planet_name(1), "Mercury")


if __name__ == "__main__":
    unittest.main()
