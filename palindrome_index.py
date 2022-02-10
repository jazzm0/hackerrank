import unittest


# https://www.hackerrank.com/challenges/palindrome-index


def is_palindrome(s):
    return s == s[::-1]


def palindromeIndex(s):
    if is_palindrome(s):
        return -1

    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            if is_palindrome(s[0:i:] + s[i + 1::]):
                return i
            if is_palindrome(s[0:-i - 1:] + s[-i::]):
                return len(s) - i - 1
    return -1


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(palindromeIndex('aaab'), 3)

    def test_b(self):
        self.assertEqual(palindromeIndex('baa'), 0)

    def test_c(self):
        self.assertEqual(palindromeIndex('aaa'), -1)

    def test_d(self):
        self.assertEqual(palindromeIndex('aaabaa'), 2)

    def test_e(self):
        self.assertEqual(palindromeIndex('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'), 44)


if __name__ == '__main__':
    unittest.main()
