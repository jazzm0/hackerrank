import unittest


def grid_traveller(n, m, memo=None):
    if memo is None:
        memo = {}

    if (n, m) in memo:
        return memo[(n, m)]

    if (m, n) in memo:
        return memo[(m, n)]

    if n == 1 and m == 1:
        return 1

    if n == 0 or m == 0:
        return 0

    result = grid_traveller(n - 1, m, memo) + grid_traveller(n, m - 1, memo)
    memo[(n, m)] = result
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(grid_traveller(1, 1), 1)

    def test_b(self):
        self.assertEqual(grid_traveller(3, 2), 3)

    def test_c(self):
        self.assertEqual(grid_traveller(18, 18), 2333606220)


if __name__ == '__main__':
    unittest.main()
