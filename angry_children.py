import unittest


# https://www.hackerrank.com/challenges/angry-children

def maxMin(k, arr):
    arr = sorted(arr)
    diff = 10 ** 9
    for i in range(0, len(arr) - k + 1):
        diff = min(diff, arr[i + k - 1] - arr[i])
    return diff


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(maxMin(2, [1, 4, 7, 2]), 1)

    def test_b(self):
        self.assertEqual(maxMin(3, [10, 100, 300, 200, 1000, 20, 30]), 20)


if __name__ == '__main__':
    unittest.main()
