import unittest
from collections import Counter


# https://www.hackerrank.com/challenges/anagram


def anagram(s):
    if len(s) % 2 != 0:
        return -1

    first = Counter(s[len(s) // 2:])
    second = Counter(s[:len(s) // 2])
    chars = list(set(s))
    count = 0

    for i in range(len(chars)):
        count += abs(first[chars[i]] - second[chars[i]])

    return count // 2


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(anagram('aaabbb'), 3)

    def test_b(self):
        self.assertEqual(anagram('ab'), 1)

    def test_c(self):
        self.assertEqual(anagram('abc'), -1)

    def test_d(self):
        self.assertEqual(anagram('xaxbbbxx'), 1)


if __name__ == '__main__':
    unittest.main()
