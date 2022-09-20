import unittest
from house_number_sum import house_numbers_sum


class MyTestCase(unittest.TestCase):
    def test_main(self):
        tests = [
            # (input, expected),
            ([5, 1, 2, 3, 0, 1, 5, 0, 2], 11),
            ([4, 2, 1, 6, 0], 13),
            ([4, 1, 2, 3, 0, 10, 2], 10),
            ([0, 1, 2, 3, 4, 5], 0),
        ]

        for inp, exp in tests:
            self.assertEqual(house_numbers_sum(inp), exp)


if __name__ == '__main__':
    unittest.main()
