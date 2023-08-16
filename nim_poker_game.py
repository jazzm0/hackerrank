import unittest

# https://www.hackerrank.com/challenges/poker-nim-1


first, second = 'First', 'Second'


def pokerNim(k, c):
    x = 0

    for p in c:
        x ^= p

    if x == 0:
        return second

    return first


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(pokerNim(5, [1, 2]), first)

    def test_b(self):
        self.assertEqual(pokerNim(5, [2, 1, 3]), second)


if __name__ == '__main__':
    unittest.main()
