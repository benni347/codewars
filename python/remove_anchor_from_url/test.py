import unittest
from remove_anchor_from_url import remove_url_anchor


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
        self.assertEqual(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
        self.assertEqual(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")


if __name__ == '__main__':
    unittest.main()
