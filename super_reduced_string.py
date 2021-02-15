import unittest


def superReducedString(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            i = max(i - 2, -1)

        i += 1
    return s


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(superReducedString('aaabccddd'), 'abd')

    def test_b(self):
        self.assertEqual(superReducedString('aa'), '')

    def test_c(self):
        self.assertEqual(superReducedString('baab'), '')

    def test_d(self):
        self.assertEqual(superReducedString(
            'ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx'),
            '')


if __name__ == '__main__':
    unittest.main()
