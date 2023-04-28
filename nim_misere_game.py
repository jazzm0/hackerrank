import unittest

# https://www.hackerrank.com/challenges/misere-nim-1


first, second = 'First', 'Second'


def misereNim(pile):
    x = 0
    ones = True

    for p in pile:
        x ^= p
        if p != 1:
            ones = False

    if ones:
        if len(pile) % 2 == 0:
            return first
        else:
            return second

    if x == 0:
        return second

    return first


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(misereNim([1, 1, 1]), second)

    def test_b(self):
        self.assertEqual(misereNim([1, 1, 1, 1]), first)

    def test_c(self):
        self.assertEqual(misereNim([1, 2, 2]), first)

    def test_d(self):
        self.assertEqual(misereNim([2, 1, 3]), second)

    def test_e(self):
        self.assertEqual(misereNim([1, 1]), first)


if __name__ == '__main__':
    unittest.main()
