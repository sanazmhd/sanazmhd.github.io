import unittest
from main import binaryserach

class MyTestCase(unittest.TestCase):
    def test_Emptylist(self):
        result = binaryserach([], 10)
        self.assertEqual(result, -1)

    def test_NotFound(self):
        result = binaryserach([1, 3, 5, 6, 8], 2)
        self.assertEqual(result, -1)

    def test_Found(self):
        result = binaryserach([3, 4, 5, 9, 12], 9)
        self.assertEqual(result, 3)

    def test_Duplicate(self):
        result = binaryserach([1, 2, 5, 4, 6, 5, 3, 8, 34, 54, 54, 54, 98], 54)
        self.assertEqual(result, [9, 10, 11])

    def test_FindMid(self):
        result = binaryserach([3, 4, 5, 6, 7], 6)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
