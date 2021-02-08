import unittest


def arrayManipulation(n, queries):
    c = {}
    for a, b, k in queries:
        c[a] = c.get(a, 0) + k
        c[b + 1] = c.get(b + 1, 0) - k
    array_sum = 0
    max_sum = 0
    for i in sorted(c):
        array_sum += c[i]
        max_sum = max(max_sum, array_sum)
    return max_sum


class TestStringMethods(unittest.TestCase):

    def test_a1(self):
        self.assertEqual(arrayManipulation(10,
                                           [[1, 5, 3],
                                            [4, 8, 7]
                                            ]), 10)

    def test_a11(self):
        self.assertEqual(arrayManipulation(10,
                                           [[1, 5, 3],
                                            [4, 5, 7]
                                            ]), 10)

    def test_a2(self):
        self.assertEqual(arrayManipulation(10,
                                           [[4, 8, 7],
                                            [1, 5, 3]
                                            ]), 10)

    def test_a3(self):
        self.assertEqual(arrayManipulation(10,
                                           [[3, 7, 1],
                                            [4, 6, 3]
                                            ]), 4)

    def test_a4(self):
        self.assertEqual(arrayManipulation(10,
                                           [[4, 6, 3],
                                            [3, 7, 1]
                                            ]), 4)

    def test_a(self):
        self.assertEqual(arrayManipulation(10,
                                           [[1, 5, 3],
                                            [4, 8, 7],
                                            [6, 9, 1]
                                            ]), 10)

    def test_b(self):
        self.assertEqual(arrayManipulation(10,
                                           [[1, 2, 100],
                                            [2, 5, 100],
                                            [3, 4, 100]
                                            ]), 200)

    def test_c(self):
        self.assertEqual(arrayManipulation(10,
                                           [[2, 6, 8],
                                            [3, 5, 7],
                                            [1, 8, 1],
                                            [5, 9, 15]
                                            ]), 31)

    def test_d(self):
        self.assertEqual(arrayManipulation(4,
                                           [[2, 3, 603],
                                            [1, 1, 286],
                                            [4, 4, 882]
                                            ]), 882)

    def test_f(self):
        self.assertEqual(arrayManipulation(40,
                                           [[29, 40, 787],
                                            [9, 26, 219],
                                            [21, 31, 214],
                                            [8, 22, 719],
                                            [15, 23, 102],
                                            [11, 24, 83],
                                            [14, 22, 321],
                                            [5, 22, 300],
                                            [11, 30, 832],
                                            [5, 25, 29],
                                            [16, 24, 577],
                                            [3, 10, 905],
                                            [15, 22, 335],
                                            [29, 35, 254],
                                            [9, 20, 20],
                                            [33, 34, 351],
                                            [30, 38, 564],
                                            [11, 31, 969],
                                            [3, 32, 11],
                                            [29, 35, 267],
                                            [4, 24, 531],
                                            [1, 38, 892],
                                            [12, 18, 825],
                                            [25, 32, 99],
                                            [3, 39, 107],
                                            [12, 37, 131],
                                            [3, 26, 640],
                                            [8, 39, 483],
                                            [8, 11, 194],
                                            [12, 37, 502],
                                            ]), 8628)


if __name__ == '__main__':
    unittest.main()
