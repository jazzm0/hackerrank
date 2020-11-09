import unittest


def highestValuePalindrome(s, n, k):
    s = list(s)
    m = set()

    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            if s[i] > s[len(s) - i - 1]:
                s[len(s) - i - 1] = s[i]
            else:
                s[i] = s[len(s) - i - 1]

            k -= 1

            m.add(i)

            if k < 0:
                print(-1)
                return '-1'

    for i in range(0, len(s)):
        if s[i] != '9' and k > 0 and i in m:
            s[i] = s[len(s) - i - 1] = '9'
            k -= 1

        if k < 1:
            break

    for i in range(0, len(s)):
        if s[i] != '9' and k >= 2:
            s[i] = s[len(s) - i - 1] = '9'
            k -= 2

        if k < 2:
            break

    if k == 1 and n % 2 == 1:
        s[n // 2] = '9'

    print(s)
    return ''.join(s)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(highestValuePalindrome('3943', 4, 1), '3993')

    def test_b(self):
        self.assertEqual(highestValuePalindrome('39543', 5, 1), '39593')

    def test_d(self):
        self.assertEqual(highestValuePalindrome('0011', 4, 1), '-1')

    def test_e(self):
        self.assertEqual(highestValuePalindrome('932239', 6, 2), '992299')

    def test_f(self):
        self.assertEqual(highestValuePalindrome('5', 1, 1), '9')

    def test_g(self):
        self.assertEqual(highestValuePalindrome('12321', 5, 1), '12921')

    def test_i(self):
        self.assertEqual(highestValuePalindrome(
            '128392759430124',
            15, 8), '929394959493929')


if __name__ == '__main__':
    unittest.main()
