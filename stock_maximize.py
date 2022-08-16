import sys
import unittest

# https://www.hackerrank.com/challenges/stockmax/

sys.setrecursionlimit(5000)


def stockmax(prices, day=0, share_count=0, profit=0, cost=0, memo=None):
    if memo is None:
        memo = {}

    if (day, share_count, profit, cost) in memo:
        return memo[(day, share_count, profit, cost)]

    memo[(day, share_count, profit, cost)] = profit + share_count * prices[day] - cost

    if day == (len(prices) - 1):
        return memo[(day, share_count, profit, cost)]

    profit = max(
        max(stockmax(prices, day + 1, share_count + 1, profit, cost + prices[day], memo),
            stockmax(prices, day + 1, 0, profit + share_count * prices[day], cost, memo)),
        stockmax(prices, day + 1, share_count, profit, cost, memo))

    return profit


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
