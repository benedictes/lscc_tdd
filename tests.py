import unittest


class firsttests(unittest.TestCase):
    def test_1_plus_1_not_3(self):
        self.assertNotEqual(1+1, 3)

    def test_1_plus_1_eq_3(self):
        self.assertEqual(1+1, 2)


if __name__ == '__main__':
    unittest.main()