import unittest
from collections import Counter


# https://www.hackerrank.com/challenges/making-anagrams/

def makingAnagrams(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    result = 0
    for k in s1.keys():
        if k not in s2:
            result += s1[k]
        else:
            result += abs(s1[k] - s2[k])
    for k in s2.keys():
        if k not in s1:
            result += s2[k]
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(makingAnagrams('abc', 'amnop'), 6)

    def test_b(self):
        self.assertEqual(makingAnagrams('abc', 'cde'), 4)


if __name__ == '__main__':
    unittest.main()
