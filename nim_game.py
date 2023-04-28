import unittest

# https://www.hackerrank.com/challenges/nim-game-1


first, second = 'First', 'Second'


def nimGame(pile):
    x = 0

    for p in pile:
        x ^= p

    if x == 0:
        return second

    return first


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(nimGame([1, 1]), second)

    def test_b(self):
        self.assertEqual(nimGame([2, 1, 4]), first)

    def test_c(self):
        self.assertEqual(nimGame([3, 5]), first)

    def test_d(self):
        self.assertEqual(nimGame([1, 3, 5, 7]), second)


if __name__ == '__main__':
    unittest.main()
