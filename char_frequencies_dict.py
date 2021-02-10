import unittest


def preProcess(s):
    count = [{} for _ in range(len(s) + 1)]
    count[0][s[0]] = 1
    for i in range(1, len(s)):
        count[i] = count[i - 1].copy()
        count[i][s[i]] = count[i].get(s[i], 0) + 1
    return count


def findCharFreq(left, right, character, count):
    return count[right].get(character, 0) - count[left - 1].get(character, 0)


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
