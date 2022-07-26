import unittest


# https://www.hackerrank.com/challenges/and-product

def shift_bit_length(x):
    return 1 << (x - 1).bit_length()


def andProduct(a, b):
    return a & ~(shift_bit_length(a ^ b) - 1)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(andProduct(12, 15), 12)

    def test_b(self):
        self.assertEqual(andProduct(2, 3), 2)

    def test_c(self):
        self.assertEqual(andProduct(8, 13), 8)

    def test_d(self):
        self.assertEqual(andProduct(8, 14), 8)

    def test_e(self):
        self.assertEqual(andProduct(1, 64), 0)

    def test_f(self):
        self.assertEqual(andProduct(1024, 2047), 1024)

    def test_g(self):
        self.assertEqual(andProduct(100799171, 102441676), 100663296)


if __name__ == '__main__':
    unittest.main()
