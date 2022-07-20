import unittest


# https://www.hackerrank.com/challenges/lego-blocks


def tetranacci(n):
    arr = [1, 2, 4, 8]
    if n <= 4:
        return arr[:n]
    else:
        for i in range(4, n):
            arr.append(sum(arr[i - 4:i]) % (10 ** 9 + 7))
    return arr


def legoBlocks(n, m):
    modulo = 10 ** 9 + 7
    a, s = [(v ** n) % modulo for v in tetranacci(m)], [1]

    for i in range(1, len(a)):
        sums = sum([x * y for x, y in zip(a[:i], s[::-1])])
        s.append((a[i] - sums) % modulo)
    return s[-1]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(legoBlocks(2, 2), 3)

    def test_b(self):
        self.assertEqual(legoBlocks(2, 3), 9)

    def test_c(self):
        self.assertEqual(legoBlocks(3, 2), 7)

    def test_d(self):
        self.assertEqual(legoBlocks(4, 4), 3375)

    def test_f(self):
        self.assertEqual(legoBlocks(4, 15), 484570337)


if __name__ == '__main__':
    unittest.main()
