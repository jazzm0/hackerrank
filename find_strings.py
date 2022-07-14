import unittest


# https://www.hackerrank.com/challenges/find-strings

def get_substrings(s):
    substrings = set()
    for strlen in range(1, len(s) + 1):
        for idx in range(len(s) - strlen + 1):
            substrings.add(s[idx:idx + strlen])
    return substrings


def findStrings(w, queries):
    s = set()
    result = []
    for wi in w:
        for sub in get_substrings(wi):
            s.add(sub)
    s = sorted(s)
    for q in queries:
        if q - 1 < len(s):
            result.append(s[q - 1])
        else:
            result.append('INVALID')
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(findStrings(['abc', 'cde'], [1, 5, 20]), ['a', 'bc', 'INVALID'])


if __name__ == '__main__':
    unittest.main()
