import math
import unittest


# https://www.hackerrank.com/challenges/k-candy-store


def solve(n, k):
    return math.comb(n + k - 1, k)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve(4, 1), 4)

    def test_b(self):
        self.assertEqual(solve(2, 3), 4)


if __name__ == '__main__':
    unittest.main()
