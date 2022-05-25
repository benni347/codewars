import unittest
import odd


class TestOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(odd.is_odd(2), False)

    def test_odd(self):
        self.assertEqual(odd.is_odd(3), True)

    def test_negative(self):
        self.assertEqual(odd.is_odd(-1), True)

    def test_zero(self):
        self.assertEqual(odd.is_odd(0), False)

    def test_decimal(self):
        self.assertEqual(odd.is_odd(1.5), False)


if __name__ == '__main__':
    unittest.main()
