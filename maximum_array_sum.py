import unittest


# https://www.hackerrank.com/challenges/max-array-sum

def maxSubsetSum(arr):
    if len(arr) == 1:
        return arr[0]

    return max(arr[0] + maxSubsetSum(arr[1:]), maxSubsetSum(arr[1:]))


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(maxSubsetSum([-2, 1, 3, -4, 5]), 8)

    def test_b(self):
        self.assertEqual(maxSubsetSum([3, 7, 4, 6, 5]), 13)

    def test_c(self):
        self.assertEqual(maxSubsetSum([3, 5, -7, 8, 10]), 15)

    def test_d(self):
        self.assertEqual(maxSubsetSum([1, 2, 3]), 4)

    def test_e(self):
        self.assertEqual(maxSubsetSum([-2, 1, 3, -4, 5, -6, -9, 10]), 8)

    def test_f(self):
        self.assertEqual(maxSubsetSum([-2, -1, -3]), 8)


if __name__ == '__main__':
    unittest.main()
