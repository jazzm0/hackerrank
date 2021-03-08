import unittest


def separateNumbers(s):
    length = 1
    i = 0
    beautiful = False
    first = s[0:length]
    while i + length < len(s):
        actual = int(s[i:i + length])
        if actual == 0:
            return 'NO'
        next = actual + 1
        if int(s[i + len(str(actual)):i + len(str(actual)) + len(str(next))]) == next:
            i += length
            length = len(str(next))
            beautiful = True
        else:
            i = 0
            length += 1
            first = s[0:length]
            beautiful = False

    if beautiful:
        return 'YES ' + first

    return 'NO'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(separateNumbers('1234'), 'YES 1')

    def test_b(self):
        self.assertEqual(separateNumbers('91011'), 'YES 9')

    def test_c(self):
        self.assertEqual(separateNumbers('99100'), 'YES 99')

    def test_d(self):
        self.assertEqual(separateNumbers('101103'), 'NO')

    def test_e(self):
        self.assertEqual(separateNumbers('010203'), 'NO')

    def test_f(self):
        self.assertEqual(separateNumbers('99910001001'), 'YES 999')


if __name__ == '__main__':
    unittest.main()
