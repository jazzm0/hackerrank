import unittest

# www.hackerrank.com/challenges/game-of-stones-1

first = 'First'
second = 'Second'


def gameOfStones(n):
    if n % 7 == 0 or (n - 1) % 7 == 0:
        return second
    return first


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(gameOfStones(4), first)

    def test_b(self):
        self.assertEqual(gameOfStones(7), second)


if __name__ == '__main__':
    unittest.main()
