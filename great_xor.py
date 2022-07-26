import unittest


# https://www.hackerrank.com/challenges/the-great-xor

def shift_bit_length(x):
    return 1 << (x - 1).bit_length()


def theGreatXor(x):
    next_power = shift_bit_length(x)
    if next_power == x:
        return x - 1
    return next_power - x - 1


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(theGreatXor(5), 2)

    def test_b(self):
        self.assertEqual(theGreatXor(10), 5)

    def test_c(self):
        self.assertEqual(theGreatXor(70), 57)

    def test_d(self):
        self.assertEqual(theGreatXor(56), 7)

    def test_e(self):
        self.assertEqual(theGreatXor(1023), 0)

    def test_f(self):
        self.assertEqual(theGreatXor(2), 1)

    def test_g(self):
        self.assertEqual(theGreatXor(64), 63)


if __name__ == '__main__':
    unittest.main()
