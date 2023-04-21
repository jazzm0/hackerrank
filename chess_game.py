import unittest

# https://www.hackerrank.com/challenges/a-chessboard-game-1/

first, second = 'First', 'Second'


def mod4(n):
    return n % 4 == 0 or (n + 1) % 4 == 0


def chessboardGame(x, y):
    if mod4(x) or mod4(y):
        return first
    return second


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(chessboardGame(5, 2), second)

    def test_b(self):
        self.assertEqual(chessboardGame(5, 3), first)

    def test_c(self):
        self.assertEqual(chessboardGame(8, 8), first)


if __name__ == '__main__':
    unittest.main()
