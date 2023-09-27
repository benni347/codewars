import unittest
import convert_int_str


class TestBasic(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(convert_int_str.number_to_string(67), "67")
        self.assertEqual(convert_int_str.number_to_string(79585), "79585")
        self.assertEqual(convert_int_str.number_to_string(79585), "79585")
        self.assertEqual(convert_int_str.number_to_string(1 + 2), "3")
        self.assertEqual(convert_int_str.number_to_string(1 - 2), "-1")


if __name__ == "__main__":
    unittest.main()
