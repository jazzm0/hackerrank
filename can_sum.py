import unittest


def can_sum(n, arr, memo={}):
    if n in memo.keys():
        return memo[n]

    if n == 0:
        return True

    if n < 0:
        return False

    for a in arr:
        if (n - a) in memo.keys():
            return memo[n - a]
        if can_sum(n - a, arr):
            memo[n] = True
            return True

    memo[n] = False
    return False


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(can_sum(7, [2, 4, 3, 5, 7]), True)

    def test_b(self):
        self.assertEqual(can_sum(300, [2, 4, 3, 5, 7]), True)

    def test_c(self):
        self.assertEqual(can_sum(1000, [3, 4, 7, 5]), True)

    def test_d(self):
        self.assertEqual(can_sum(300, [7, 14]), False)

    def test_g(self):
        self.assertEqual(can_sum(301, [5, 25]), False)


if __name__ == '__main__':
    unittest.main()
