import unittest
import find_divisors


class TestDivisors(unittest.TestCase):
    def test_single_divisor(self):
        self.assertEqual(find_divisors.divisors(25), [5])

    def test_two_divisors(self):
        self.assertEqual(find_divisors.divisors(15), [3, 5])
        self.assertEqual(find_divisors.divisors(253), [11, 23])

    def test_12(self):
        self.assertEqual(find_divisors.divisors(12), [2, 3, 4, 6])

    def test_prime(self):
        self.assertEqual(find_divisors.divisors(3), "3 is prime")
        self.assertEqual(find_divisors.divisors(5), "5 is prime")
        self.assertEqual(find_divisors.divisors(11), "11 is prime")
        self.assertEqual(find_divisors.divisors(13), "13 is prime")


if __name__ == "__main__":
    unittest.main()
