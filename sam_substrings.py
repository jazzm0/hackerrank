import unittest

# https://www.hackerrank.com/challenges/sam-and-substrings/

p = pow(10, 9) + 7


def substrings(s):
    size = len(s)
    prev = int(s[0])
    total = prev
    for i in range(1, size):
        total = (total * 10 + int(s[i]) * (i + 1)) % p
        prev = (total + prev) % p
    return prev


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(substrings('42'), 48)

    def test_b(self):
        self.assertEqual(substrings('16'), 23)

    def test_c(self):
        self.assertEqual(substrings('231'), 291)

    def test_d(self):
        self.assertEqual(substrings('123'), 164)

    def test_e(self):
        self.assertEqual(substrings('972698438521'), 445677619)


if __name__ == '__main__':
    unittest.main()
