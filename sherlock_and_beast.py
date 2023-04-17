import unittest


# https://www.hackerrank.com/challenges/sherlock-and-the-beast

def output(n):
    print(n)
    return n


def decentNumber(n):
    if n < 3:
        return output(-1)

    count_five = n // 3

    while count_five > 0 and (n - count_five * 3) % 5 != 0:
        count_five -= 1

    if count_five == 0 and n % 5 != 0:
        return output(-1)

    f = ['5'] * count_five * 3
    t = ['3'] * (n - count_five * 3)
    solution = int(''.join(f + t))
    return output(solution)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(decentNumber(3), 555)

    def test_b(self):
        self.assertEqual(decentNumber(5), 33333)

    def test_c(self):
        self.assertEqual(decentNumber(11), 55555533333)

    def test_d(self):
        self.assertEqual(decentNumber(13), 5553333333333)

    def test_e(self):
        self.assertEqual(decentNumber(101),
                         55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555533333)

    def test_f(self):
        self.assertEqual(decentNumber(1), -1)

    def test_g(self):
        self.assertEqual(decentNumber(100),
                         5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553333333333)


if __name__ == '__main__':
    unittest.main()
