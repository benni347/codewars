import unittest
from find_uniq import find_uniq


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
        self.assertEqual(find_uniq([3, 10, 3, 3, 3]), 10)

    def test_last_item(self):
        self.assertEqual(find_uniq([3, 3, 3, 3, 10]), 10)
        self.assertEqual(find_uniq([0.8, 0.8, 0.8, 0.8, 0.11]), 0.11)


if __name__ == "__main__":
    unittest.main()
