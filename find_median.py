import unittest


def findMedian(arr):
    arr = sorted(arr)
    return arr[len(arr) // 2]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(findMedian([0, 1, 2, 4, 6, 5, 3]), 3)


if __name__ == '__main__':
    unittest.main()
