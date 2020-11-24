import unittest


def isValid(s):
    char_count = {}

    for i in range(len(s)):
        char_count[s[i]] = char_count.get(s[i], 0) + 1

    count = {}

    for x in char_count.values():
        count[x] = count.get(x, 0) + 1

    if len(count) == 1:
        print('YES')
        return 'YES'

    if len(count) == 2:
        for k, v in count.items():
            if v == 1 and (k == 1 or (k - 1) in count.keys()):
                print('YES')
                return 'YES'

    print('NO')
    return 'NO'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(isValid('abc'), 'YES')

    def test_b(self):
        self.assertEqual(isValid('abcc'), 'YES')

    def test_c(self):
        self.assertEqual(isValid('abccc'), 'NO')

    def test_d(self):
        self.assertEqual(isValid('aabbc'), 'YES')


if __name__ == '__main__':
    unittest.main()
