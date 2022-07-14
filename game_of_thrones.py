import unittest
from collections import Counter


# https://www.hackerrank.com/challenges/game-of-thrones

def gameOfThrones(s):
    counts = Counter(s)
    odd = 0
    for k, v in counts.items():
        if v % 2 != 0:
            odd += 1
        if odd > 1:
            return 'NO'

    return 'YES'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(gameOfThrones('abcddcba'), 'YES')

    def test_b(self):
        self.assertEqual(gameOfThrones('aaabbbb'), 'YES')

    def test_c(self):
        self.assertEqual(gameOfThrones('cdefghmnopqrstuvw'), 'NO')

    def test_d(self):
        self.assertEqual(gameOfThrones('cdcdcdcdeeeef'), 'YES')


if __name__ == '__main__':
    unittest.main()
