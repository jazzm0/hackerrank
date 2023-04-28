import unittest


# https://www.hackerrank.com/challenges/strings-xor


def strings_xor(s, t):
    #     return bin(int(s, 2) ^ int(t, 2))[2:]
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(strings_xor('10101', '00101'), '10000')


if __name__ == '__main__':
    unittest.main()
