import unittest


def count(s1, s2):
    c = 0
    minlen = min(len(s1), len(s2))
    for i in range(minlen):
        if s1[i] == s2[i]:
            c += 1
        else:
            break
    return c


def stringSimilarity(s):
    c = 0
    for i in range(len(s)):
        c += count(s, s[i:])

    return c


class TestStringMethods(unittest.TestCase):

    def test_a1(self):
        self.assertEqual(count("abc", "abd"), 2)

    def test_a2(self):
        self.assertEqual(count("aaa", "aaab"), 3)

    def test_a(self):
        self.assertEqual(stringSimilarity("ababaa"), 11)

    def test_b(self):
        self.assertEqual(stringSimilarity("aa"), 3)


if __name__ == '__main__':
    unittest.main()
