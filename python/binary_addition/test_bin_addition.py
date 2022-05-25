import unittest
import bin_addition


class TestBinAddition(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(bin_addition.add_binary(1, 1), "10")
        self.assertEqual(bin_addition.add_binary(0, 1), "1")
        self.assertEqual(bin_addition.add_binary(1, 0), "1")
        self.assertEqual(bin_addition.add_binary(2, 2), "100")
        self.assertEqual(bin_addition.add_binary(51, 12), "111111")


if __name__ == '__main__':
    unittest.main()
