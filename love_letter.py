import unittest


# https://www.hackerrank.com/challenges/the-love-letter-mystery

def theLoveLetterMystery(s):
    count = 0
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            count += abs(ord(s[i]) - ord(s[-(i + 1)]))
    return count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(theLoveLetterMystery('abc'), 2)

    def test_b(self):
        self.assertEqual(theLoveLetterMystery('abcba'), 0)

    def test_c(self):
        self.assertEqual(theLoveLetterMystery('abcd'), 4)

    def test_d(self):
        self.assertEqual(theLoveLetterMystery('cba'), 2)


if __name__ == '__main__':
    unittest.main()
