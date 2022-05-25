import unittest
import even_odd


class TestEvenOdd(unittest.TestCase):
    def test_odd(self):
        e = even_odd.even_or_odd(1)
        self.assertEqual(e, "Odd")

    def test_even(self):
        e = even_odd.even_or_odd(2)
        self.assertEqual(e, "Even")


if __name__ == '__main__':
    unittest.main()
