import sys
import unittest

# https://www.hackerrank.com/challenges/stockmax/

sys.setrecursionlimit(5000)


def stockmax(prices):
    m = prices.pop()
    maxsum = 0
    arrsum = 0
    for p in reversed(prices):
        m = max(m, p)
        maxsum += m
        arrsum += p
    return maxsum - arrsum


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(stockmax([5, 3, 2]), 0)

    def test_b(self):
        self.assertEqual(stockmax([1, 2, 100]), 197)

    def test_c(self):
        self.assertEqual(stockmax([1, 3, 1, 2]), 3)

    def test_d(self):
        self.assertEqual(stockmax(
            [38430, 35991, 26818, 19088, 37402, 82378]), 254161)


if __name__ == '__main__':
    unittest.main()
