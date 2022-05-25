import unittest
import x_o


class TestXO(unittest.TestCase):
    def test_same(self):
        self.assertEqual(x_o.xo("xo"), True)

    def test_different(self):
        self.assertEqual(x_o.xo("xxo"), False)
        self.assertEqual(x_o.xo("xoo"), False)

    def test_with_diffrent_symbol(self):
        self.assertEqual(x_o.xo("xo0"), True)
        self.assertEqual(x_o.xo("xo0o"), False)
        self.assertEqual(x_o.xo("x1090"), False)



if __name__ == '__main__':
    unittest.main()
