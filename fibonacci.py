import unittest

memo = {}


def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    f = fib(n - 1) + fib(n - 2)
    memo[n] = f
    return f


def fib_it(n):
    previous_result, result = 1, 2
    if n <= 2:
        return 1
    for i in range(n - 3):
        previous_result, result = result, result + previous_result
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(fib(50), 12586269025)

    def test_f(self):
        self.assertEqual(fib(12), 144)

    def test_h(self):
        self.assertEqual(fib_it(1001),
                         70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501)

    def test_g(self):
        self.assertEqual(fib_it(7), 13)

    def test_i(self):
        self.assertEqual(fib_it(50), 12586269025)


if __name__ == '__main__':
    unittest.main()
