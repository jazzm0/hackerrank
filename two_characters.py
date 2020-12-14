import unittest
from collections import Counter


def is_alternating(s):
    a = s[0]
    b = s[1]

    for i in range(2, len(s), 2):
        if s[i] != a or (i + 1 < len(s) and s[i + 1] != b):
            return False
    return True


def alternate(s):
    counts = Counter(s)
    maxcount = 0

    for i in counts.keys():
        for j in counts.keys():
            if i == j or abs(counts[i] - counts[j]) > 1:
                continue
            remaining = set(counts.keys())
            remaining.remove(i)
            remaining.remove(j)
            test_string = s
            for r in remaining:
                test_string = test_string.replace(r, '')
            if is_alternating(test_string):
                maxcount = max(maxcount, len(test_string))

    return maxcount


class TestStringMethods(unittest.TestCase):

    def test_a1(self):
        self.assertEqual(is_alternating('bababa'), True)

    def test_a2(self):
        self.assertEqual(is_alternating('bababc'), False)

    def test_a3(self):
        self.assertEqual(is_alternating('babab'), True)

    def test_a(self):
        self.assertEqual(alternate('beabeefeab'), 5)

    def test_b(self):
        self.assertEqual(alternate('asdcbsdcagfsdbgdfanfghbsfdab'), 8)


if __name__ == '__main__':
    unittest.main()
