import unittest


def countArray(n, k, x):
    MOD = 10 ** 9 + 7
    dp0 = dp1 = 0
    dp0old = 1
    for end in range(2, n + 1):
        dp0 = (dp1 * (k - 1)) % MOD
        dp1 = (dp0old + dp1 * (k - 2)) % MOD
        dp0old = dp0
    if x == 1:
        return dp0
    return dp1


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(countArray(4, 3, 2), 3)


if __name__ == '__main__':
    unittest.main()
