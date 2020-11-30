import unittest


def superReducedString(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s.replace(s[i] + s[i + 1], '')
            if i > 0:
                i -= 2
            elif i == 0:
                i = -1

        i += 1

    if len(s) == 0:
        print('Empty String')
        return 'Empty String'

    print(s)
    return s


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(superReducedString('aaabccddd'), 'abd')

    def test_b(self):
        self.assertEqual(superReducedString('aa'), 'Empty String')

    def test_c(self):
        self.assertEqual(superReducedString('baab'), 'Empty String')

    def test_d(self):
        self.assertEqual(superReducedString(
            'ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx'),
                         'Empty String')


if __name__ == '__main__':
    unittest.main()
