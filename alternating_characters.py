import unittest


# https://www.hackerrank.com/challenges/alternating-characters

def alternatingCharacters(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(alternatingCharacters('AAAA'), 3)

    def test_b(self):
        self.assertEqual(alternatingCharacters('BBBBB'), 4)

    def test_c(self):
        self.assertEqual(alternatingCharacters('ABABABAB'), 0)

    def test_d(self):
        self.assertEqual(alternatingCharacters('BABABA'), 0)

    def test_e(self):
        self.assertEqual(alternatingCharacters('AAABBB'), 4)


if __name__ == '__main__':
    unittest.main()
