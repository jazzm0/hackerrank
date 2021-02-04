import unittest


def arrayManipulation(n, queries):
    a = [0] * n
    for q in queries:
        for i in range(q[0] - 1, q[1]):
            a[i] += q[2]

    result = 0
    for i in range(n):
        result = max(result, a[i])
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


if __name__ == '__main__':
    unittest.main()
