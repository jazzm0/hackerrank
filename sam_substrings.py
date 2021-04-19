import unittest

# https://www.hackerrank.com/challenges/sam-and-substrings/

p = pow(10, 9) + 7


def substrings(s):
    sum = 0
    actual_len = 1

    while actual_len <= len(s):
        for i in range(0, len(s) - actual_len + 1):
            sum += int(s[i:i + actual_len]) % p
        actual_len += 1
        
    return sum % p


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
