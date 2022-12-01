import unittest


# https://www.hackerrank.com/challenges/is-fibo

def isFibo(n):
    x0, x1, x = 0, 1, 0
    while x < n:
        x = x0 + x1
        x0 = x1
        x1 = x

    if x == n:
        return 'IsFibo'
    else:
        return 'IsNotFibo'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(isFibo(5), 'IsFibo')

    def test_b(self):
        self.assertEqual(isFibo(7), 'IsNotFibo')

    def test_c(self):
        self.assertEqual(isFibo(3), 'IsFibo')


if __name__ == '__main__':
    unittest.main()
