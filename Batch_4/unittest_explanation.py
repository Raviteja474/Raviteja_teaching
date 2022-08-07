import unittest


class DummyClass:
    x = 5


class TestMethods(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(2,2,"same")
        self.assertEqual(2,3,"Not same")


if __name__ == '__main__':
    unittest.main()