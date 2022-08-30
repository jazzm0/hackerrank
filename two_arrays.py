import unittest


# https://www.hackerrank.com/challenges/two-arrays

def twoArrays(k, a, b):
    a, b = sorted(a), sorted(b)
    for i in range(len(a)):
        j = 0
        while a[i] + b[j] < k:
            j += 1
            if j > len(b) - 1:
                return 'NO'
        del b[j]
    return 'YES'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(twoArrays(1, [0, 1], [0, 2]), 'YES')

    def test_b(self):
        self.assertEqual(twoArrays(10, [1, 2, 3], [9, 8, 7]), 'YES')

    def test_c(self):
        self.assertEqual(twoArrays(11, [2, 2, 3], [9, 8, 7]), 'NO')


if __name__ == '__main__':
    unittest.main()
