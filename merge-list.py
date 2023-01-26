import unittest
from math import comb


def solve(n, m):
    return comb(n + m, m) % (10 ** 9 + 7)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve(2, 2), 6)

    def test_b(self):
        self.assertEqual(solve(3, 2), 10)

    def test_c(self):
        self.assertEqual(solve(59, 67), 885566595)


if __name__ == '__main__':
    unittest.main()
