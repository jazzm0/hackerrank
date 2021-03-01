import unittest


# https://www.hackerrank.com/challenges/coin-change

def getWays(n, c):
    ways = 0
    return ways


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(getWays(3, [8, 3, 1, 2]), 3)

    def test_b(self):
        self.assertEqual(getWays(4, [3, 1, 2]), 4)

    def test_c(self):
        self.assertEqual(getWays(12, [1, 2, 5, 10]), 15)


if __name__ == '__main__':
    unittest.main()
