import unittest
from build import generate_shape


class MyTestCase(unittest.TestCase):
    def test_small(self):
        self.assertEqual(generate_shape(3), '+++\n+++\n+++')
        self.assertEqual(generate_shape(8),
                           '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++')



if __name__ == '__main__':
    unittest.main()
