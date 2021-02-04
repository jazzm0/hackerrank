import unittest


def arrayManipulation(n, queries):
    a = {(queries[0][0], queries[0][1]): queries[0][2]}
    for q in range(1, len(queries)):
        overlap = False
        for k, v in a.items():
            if (k[0] <= queries[q][0] <= k[1]) or \
                    (k[0] <= queries[q][1] <= k[1]) or \
                    (k[0] >= queries[q][0] or queries[q][0] >= k[1]):
                a[k] += queries[q][2]
                overlap = True
        if not overlap:
            a[(queries[q][0], queries[q][1])] = queries[q][2]

    result = 0
    for k, v in a.items():
        result = max(result, v)
    return result


class TestStringMethods(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
