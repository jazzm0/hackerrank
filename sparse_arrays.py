import unittest
from collections import Counter


def matchingStrings(strings, queries):
    counts = Counter(strings)
    result = []
    for q in queries:
        result.append(counts.get(q, 0))
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(matchingStrings(["ab", "ab", "abc"], ["ab", "abc", "bc"]), [2, 1, 0])


if __name__ == '__main__':
    unittest.main()
