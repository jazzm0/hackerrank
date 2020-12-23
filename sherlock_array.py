import unittest


def balancedSums(arr):
    sum_arr = 0
    for s in arr:
        sum_arr += s

    partial_sum = 0
    for i in arr:
        if (2 * partial_sum) == (sum_arr - i):
            return 'YES'
        partial_sum += i

    return 'NO'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(balancedSums([5, 6, 8, 11]), 'YES')

    def test_b(self):
        self.assertEqual(balancedSums([1, 2, 3]), 'NO')

    def test_c(self):
        self.assertEqual(balancedSums([1, 2, 3, 3]), 'YES')


if __name__ == '__main__':
    unittest.main()
