import unittest


def sherlockAndAnagrams(s):
    char_count = {}

    for i in range(len(s)):
        char_count[s[i]] = char_count.get(s[i], 0) + 1

    return 0


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(sherlockAndAnagrams('abba'), 4)

    def test_b(self):
        self.assertEqual(sherlockAndAnagrams('abcd'), 0)

    def test_c(self):
        self.assertEqual(sherlockAndAnagrams('ifailuhkqq'), 3)

    def test_d(self):
        self.assertEqual(sherlockAndAnagrams('kkkk'), 10)


if __name__ == '__main__':
    unittest.main()
