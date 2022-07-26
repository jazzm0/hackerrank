import unittest


# https://www.hackerrank.com/challenges/sum-vs-xor

def sumXor(n):
    if n == 0:
        return 1
    return 2 ** bin(n)[2:].count('0')


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(sumXor(4), 4)

    def test_b(self):
        self.assertEqual(sumXor(5), 2)

    def test_c(self):
        self.assertEqual(sumXor(8), 8)

    def test_d(self):
        self.assertEqual(sumXor(16), 16)

    def test_e(self):
        self.assertEqual(sumXor(15), 1)


if __name__ == '__main__':
    unittest.main()
