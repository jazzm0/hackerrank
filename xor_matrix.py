import unittest


# https://www.hackerrank.com/challenges/xor-matrix/

# XOR
# A|B|A^B
# 0|0|0
# 0|1|1
# 1|0|1
# 1|1|0

def xorMatrix(m, first_row):
    n = len(first_row)
    m -= 1
    mb = str(bin(m))[2:]
    lmb = len(mb)
    result = first_row.copy()
    for i in range(lmb):
        if mb[i] == '1':
            tmp = result.copy()
            offset = 2 ** (lmb - 1 - i)
            for j in range(n):
                result[j] = tmp[j] ^ tmp[(j + offset) % n]
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(xorMatrix(2, [6, 7, 1, 3]), [1, 6, 2, 5])

    def test_b(self):
        self.assertEqual(xorMatrix(4, [1, 7, 14, 8, 2]), [0, 3, 5, 12, 10])

    def test_c(self):
        self.assertEqual(xorMatrix(1000000000, [325, 483, 252, 71, 592, 866, 473, 991, 570, 985]),
                         [325, 899, 29, 776, 393, 172, 820, 862, 997, 889])


if __name__ == '__main__':
    unittest.main()
