import unittest
from conv_bool import bool_to_word


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(bool_to_word(True), "Yes")
        self.assertEqual(bool_to_word(False), "No")


if __name__ == "__main__":
    unittest.main()
