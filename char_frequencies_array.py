import unittest


def preProcess(s):
    n = len(s)
    max_char = 26

    count = [[0 for _ in range(max_char)]
             for _ in range(n + 1)]

    for i in range(0, n):
        count[i][ord(s[i]) - ord('a')] += 1

    for i in range(0, n):
        for j in range(0, 26):
            count[i][j] += count[i - 1][j]

    return count


def findCharFreq(left, right, c, count):
    return count[right][ord(c) - 97] - count[left - 1][ord(c) - 97]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        s = "geeksforgeeks"
        count = preProcess(s)
        self.assertEqual(findCharFreq(0, 5, 'e', count), 2)
        self.assertEqual(findCharFreq(2, 6, 'f', count), 1)
        self.assertEqual(findCharFreq(4, 7, 'm', count), 0)
        self.assertEqual(findCharFreq(0, 12, 'e', count), 4)
        self.assertEqual(findCharFreq(0, 3, 'g', count), 1)
        self.assertEqual(findCharFreq(1, 1, 'e', count), 1)
        self.assertEqual(findCharFreq(11, 12, 's', count), 1)


if __name__ == '__main__':
    unittest.main()
