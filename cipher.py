import unittest


# https://www.hackerrank.com/challenges/cipher

# 1001010000
# 0100101000
# 0010010100
# 0001001010
# ----------
# 1110100110

# XOR
# A|B|A^B
# 0|0|0
# 0|1|1
# 1|0|1
# 1|1|0


def cipher(k, s):
    total_length = len(s)
    decrypted = ['0'] * total_length
    p = n = 0
    xor = 0
    for i in range(k):
        suffix = int(s[-i - 1])
        decrypted[-i - 1] = str(suffix ^ p)
        p = suffix
        if i < k - 1:
            prefix = int(s[i])
            decrypted[i + k - 1] = str(prefix ^ n)
            xor ^= int(decrypted[i + k - 1])
            n = prefix

    left = total_length - 3 * k + 2

    for i in range(left):
        decrypted[2 * k + i - 2] = str(xor ^ int(s[i + k - 1]))
        xor = xor ^ int(decrypted[2 * k + i - 2]) ^ int(decrypted[k + i - 1])

    return str(''.join(decrypted[k - 1:]))


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(cipher(4, '1110100110'), '1001010')

    def test_b(self):
        self.assertEqual(cipher(2, '1110001'), '101111')

    def test_c(self):
        self.assertEqual(cipher(4, '1110101001'), '1001011')

    def test_d(self):
        self.assertEqual(cipher(3, '1110011011'), '10000101')

    def test_e(self):
        self.assertEqual(cipher(4, '1101011110100'), '1011011100')


if __name__ == '__main__':
    unittest.main()
