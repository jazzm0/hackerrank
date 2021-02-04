import unittest

MAX_LEN = 13
cnt = [{} for i in range(MAX_LEN)]


def preProcess(s):
    cnt[0][s[0]] = 1
    for i in range(1, len(s)):
        cnt[i] = cnt[i - 1].copy()
        cnt[i][s[i]] = cnt[i].get(s[i], 0) + 1


def findCharFreq(l, r, c):
    return cnt[r].get(c, 0) - cnt[l].get(c, 0)


class TestStringMethods(unittest.TestCase):

    def test_median_a(self):
        s = "geeksforgeeks"
        preProcess(s)
        self.assertEqual(findCharFreq(0, 5, 'e'), 2)
        self.assertEqual(findCharFreq(2, 6, 'f'), 1)
        self.assertEqual(findCharFreq(4, 7, 'm'), 0)
        self.assertEqual(findCharFreq(0, 12, 'e'), 4)


if __name__ == '__main__':
    unittest.main()
