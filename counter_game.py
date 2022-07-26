import unittest

# https://www.hackerrank.com/challenges/counter-game
from math import log


def counterGame(n):
    counter = 1
    while n > 1:
        base = int(log(n, 2))
        next_lower = 2 ** base
        if n == next_lower:
            n /= 2
        else:
            n -= next_lower
        counter += 1

    if counter % 2 == 0:
        return 'Louise'

    return 'Richard'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(counterGame(132), 'Louise')

    def test_b(self):
        self.assertEqual(counterGame(6), 'Richard')


if __name__ == '__main__':
    unittest.main()
