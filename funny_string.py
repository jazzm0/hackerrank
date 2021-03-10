import unittest


def funnyString(s):
    n = len(s)
    for i in range(n - 1):
        if abs(ord(s[i + 1]) - ord(s[i])) != abs(ord(s[n - i - 2]) - ord(s[n - i - 1])):
            return "Not Funny"

    return "Funny"


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_b(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_c(self):
        self.assertEqual(funnyString("ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq"), "Funny")

    def test_d(self):
        self.assertEqual(funnyString("ponml"), "Funny")


if __name__ == '__main__':
    unittest.main()
