import unittest
from reader import Reader


class ReaderTestCase(unittest.TestCase):

    def test_filler(self):
        x = 0
        self.assertEqual(x, 0)


if __name__ == '__main__':
    unittest.main()
