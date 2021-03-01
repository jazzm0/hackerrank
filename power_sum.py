import unittest


# https://www.hackerrank.com/challenges/the-power-sum

def powerSum(x, n):
    numbers = int(pow(x, 1 / n))

    dp = [1] + [0] * x
    for i in range(1, numbers + 1):
        u = i ** n
        for j in range(x, u - 1, -1):
            dp[j] += dp[j - u]

    return dp[-1]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(powerSum(10, 2), 1)

    def test_b(self):
        self.assertEqual(powerSum(100, 2), 3)


if __name__ == '__main__':
    unittest.main()
