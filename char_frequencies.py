import unittest

MAX_LEN = 13
cnt = [{} for i in range(MAX_LEN)]


def preProcess(s):
    n = len(s)

    for i in range(0, n):
        cnt[i][s[i]] = cnt[i].get(s[i], 0) + 1

    for i in range(1, n):
        for k, v in cnt[i - 1].items():
            cnt[i][k] = cnt[i].get(k, 0) + v


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
