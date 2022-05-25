import unittest
import convert_str_int


class TestBasic(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(convert_str_int.string_to_number("1234"), 1234)
        self.assertEqual(convert_str_int.string_to_number("605"), 605)
        self.assertEqual(convert_str_int.string_to_number("1405"), 1405)
        self.assertEqual(convert_str_int.string_to_number("-7"), -7)


if __name__ == '__main__':
    unittest.main()
