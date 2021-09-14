import unittest


# https://www.hackerrank.com/challenges/pangrams

def pangrams(s):
    alphabet_letters = set()
    for i in range(len(s)):
        if s[i].isalpha() and not s[i].lower() in alphabet_letters:
            alphabet_letters.add(s[i].lower())
        if len(alphabet_letters) == 26:
            return 'pangram'
    return 'not pangram'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(pangrams('The quick brown fox jumps over the lazy dog'), 'pangram')

    def test_b(self):
        self.assertEqual(pangrams('We promptly judged antique ivory buckles for the next prize'), 'pangram')

    def test_c(self):
        self.assertEqual(pangrams('We promptly judged antique ivory buckles for the prize'), 'not pangram')


if __name__ == '__main__':
    unittest.main()
