import unittest


def maxSubsetSum(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n + 1)]
    for i in range(n):
        dp[0][i] = dp[i + 1][0] = arr[i]

    for i in range(1, n + 1):
        for j in range(1, n):
            if j != i - 1:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j] + dp[i][0])

    return dp


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(maxSubsetSum([-2, 1, 3, -4, 5]), 8)

    def test_b(self):
        self.assertEqual(maxSubsetSum([3, 7, 4, 6, 5]), 13)

    def test_c(self):
        self.assertEqual(maxSubsetSum([3, 5, -7, 8, 10]), 15)

    def test_d(self):
        self.assertEqual(maxSubsetSum([1, 2, 3]), 5)


if __name__ == '__main__':
    unittest.main()
