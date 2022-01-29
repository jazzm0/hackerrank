import unittest


# https://www.hackerrank.com/challenges/flipping-bits

def flippingBits(n):
    return 2 ** 32 - 1 ^ n


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(flippingBits(9), 4294967286)

    def test_b(self):
        self.assertEqual(flippingBits(0), 4294967295)

    def test_c(self):
        self.assertEqual(flippingBits(802743475), 3492223820)

    def test_d(self):
        self.assertEqual(flippingBits(2147483647), 2147483648)


if __name__ == '__main__':
    unittest.main()
