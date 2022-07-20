import unittest


# https://www.hackerrank.com/challenges/fibonacci-modified/

def fibonacciModified1(t1, t2, n, memo=None):
    if memo is None:
        memo = {1: t1, 2: t2}

    if n in memo:
        return memo[n]

    f = fibonacciModified1(t1, t2, n - 2, memo)
    memo[n - 2] = f

    g = fibonacciModified1(t1, t2, n - 1, memo) ** 2

    memo[n] = f + g
    return memo[n]


def fibonacciModified2(t1, t2, n):
    f = [t1, t2]
    for i in range(2, n):
        f.append(f[i - 2] + f[i - 1] ** 2)

    return f[n - 1]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(fibonacciModified1(0, 1, 5), 5)

    def test_b(self):
        self.assertEqual(fibonacciModified2(0, 1, 10), 84266613096281243382112)


if __name__ == '__main__':
    unittest.main()
