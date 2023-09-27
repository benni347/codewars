import unittest
import multiply


class TestMultiply(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(multiply.multiply(2, 3), 6)
        self.assertEqual(multiply.multiply(-10, -10), 100)
        self.assertEqual(multiply.multiply(2, 0.5), 1)


if __name__ == "__main__":
    unittest.main()
