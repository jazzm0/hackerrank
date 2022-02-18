import unittest


def can_sum(target, coins, memo=None):
    if memo is None:
        memo = {}

    if target == 0:
        return True

    if target < 0:
        return False

    if target in memo:
        return memo[target]

    for i in range(len(coins)):
        if coins[i] <= target:
            result = can_sum(target - coins[i], coins, memo)
            if result:
                return result
            else:
                memo[target] = result

    return False


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(can_sum(1, [1, 2, 5]), True)

    def test_b(self):
        self.assertEqual(can_sum(3, [1, 2, 5]), True)

    def test_c(self):
        self.assertEqual(can_sum(3, [1, 2, 5]), True)

    def test_d(self):
        self.assertEqual(can_sum(3, [2, 5]), False)

    def test_e(self):
        self.assertEqual(can_sum(17, [2, 8]), False)

    def test_f(self):
        self.assertEqual(can_sum(1007, [2, 8]), False)

    def test_g(self):
        self.assertEqual(can_sum(7, [5, 3, 4, 7]), True)

    def test_h(self):
        self.assertEqual(can_sum(300, [14, 7]), False)


if __name__ == '__main__':
    unittest.main()
