import unittest

# https://www.hackerrank.com/challenges/missing-numbers
from collections import Counter


def missingNumbers(a, b):
    a, b, result = Counter(a), Counter(b), set()
    for e in b:
        if e not in a or b[e] != a[e]:
            result.add(e)
    return list(sorted(result))


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(missingNumbers([7, 2, 5, 3, 5, 3], [7, 2, 5, 4, 6, 3, 5, 3]), [4, 6])

    def test_b(self):
        self.assertEqual(missingNumbers([7, 2, 5, 3, 5, 3, 2, 7], [7, 2, 5, 4, 6, 3, 5, 3]), [2, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
