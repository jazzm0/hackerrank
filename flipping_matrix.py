import unittest


# https://www.hackerrank.com/challenges/flipping-the-matrix

def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n // 2):
        for j in range(n // 2):
            s += max(max(max(matrix[i][j], matrix[i][n - j - 1]),
                         max(matrix[i][j], matrix[n - i - 1][j])),
                     max(matrix[i][j], matrix[n - i - 1][n - j - 1]))
    return s


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(flippingMatrix([[112, 42, 83, 119],
                                         [56, 125, 56, 49],
                                         [15, 78, 101, 43],
                                         [62, 98, 114, 108]]), 414)


if __name__ == '__main__':
    unittest.main()
