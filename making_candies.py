import math
import sys
import unittest


# https://www.hackerrank.com/challenges/making-candies

def minimumPasses(m, w, p, n):
    candy = 0
    invest = 0
    spend = sys.maxsize
    while candy < n:
        passes = (p - candy) // (m * w)
        if passes <= 0:
            mw = (candy // p) + m + w
            half = math.ceil(mw / 2)
            if m > w:
                m = max(m, half)
                w = mw - m
            else:
                w = max(w, half)
                m = mw - w
            candy %= p
            passes = 1
        candy += passes * m * w
        invest += passes
        spend = min(spend, invest + math.ceil((n - candy) / (m * w)))
    return min(invest, spend)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(minimumPasses(3, 1, 2, 12), 3)

    def test_b(self):
        self.assertEqual(minimumPasses(1, 2, 1, 60), 4)

    def test_c(self):
        self.assertEqual(minimumPasses(1, 1, 6, 45), 16)


if __name__ == '__main__':
    unittest.main()
