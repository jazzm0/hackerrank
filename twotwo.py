import math
import unittest


# https://www.hackerrank.com/challenges/two-two/

def strength(i, j, a):
    if a[i] == 0:
        return 0
    v = 0
    for k in range(i, j + 1):
        v = v * 10 + a[k]
    return v


def twoTwo(a):
    query = []
    a = int(a)
    while a != 0:
        query.append(a % 10)
        a //= 10

    query.reverse()
    count = 0

    for j in range(len(query)):
        for i in range(j + 1):
            s = strength(i, j, query)
            if s != 0:
                base = math.log(s, 2)
                if s % 2 == 0 and base != 0 and base.is_integer():
                    count += 1

    return count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(twoTwo('2222222'), 7)

    def test_b(self):
        self.assertEqual(twoTwo(24256), 4)

    def test_c(self):
        self.assertEqual(twoTwo(65536), 1)

    def test_d(self):
        self.assertEqual(twoTwo(23223), 4)

    def test_e(self):
        self.assertEqual(twoTwo(33579), 0)

    def test_f(self):
        self.assertEqual(twoTwo(10), 0)


if __name__ == '__main__':
    unittest.main()
