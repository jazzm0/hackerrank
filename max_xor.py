import unittest


# https://www.hackerrank.com/challenges/maximizing-xor/


def maximizingXor(l, r):
    result = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            result = max(result, i ^ j)
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(maximizingXor(10, 15), 7)

    def test_b(self):
        self.assertEqual(maximizingXor(11, 12), 7)


if __name__ == '__main__':
    unittest.main()
