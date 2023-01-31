import unittest


# https://www.hackerrank.com/challenges/picking-cards

def solve(c):
    mod = 10 ** 9 + 7
    c = sorted(c)
    result = 1
    card_count = 0
    for card in c:
        if card_count < card:
            return 0

        card_count += 1
        result *= card_count - card

    return result % mod


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve([0, 0, 0]), 6)

    def test_b(self):
        self.assertEqual(solve([0, 0, 1]), 4)

    def test_c(self):
        self.assertEqual(solve([0, 3, 3]), 0)

    def test_d(self):
        self.assertEqual(solve([3, 3, 6, 1, 3, 9, 4, 2, 13, 5, 5, 1, 3, 11, 2, 1, 0]), 759833446)

    def test_e(self):
        self.assertEqual(solve([0, 0, 0, 1, 1, 2, 2, 2]), 8640)


if __name__ == '__main__':
    unittest.main()
