import unittest
from collections import Counter


# https://www.hackerrank.com/challenges/game-of-thrones


def twoStrings(s1, s2):
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)

    for k, v in count_s1.items():
        if k in count_s2:
            return 'YES'

    return 'NO'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(twoStrings('and', 'art'), 'YES')

    def test_b(self):
        self.assertEqual(twoStrings('hello', 'world'), 'YES')

    def test_c(self):
        self.assertEqual(twoStrings('hi', 'world'), 'NO')


if __name__ == '__main__':
    unittest.main()
