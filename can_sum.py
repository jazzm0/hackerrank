import unittest


def can_sum(target, coins, memo=None, solutions=None, depth=None):
    if memo is None:
        memo = {}

    if depth is None:
        depth = 0

    if solutions is None:
        solutions = {}

    if target == 0:
        return []

    if target < 0:
        return None

    if target in memo:
        return memo[target]

    for i in range(len(coins)):
        if coins[i] <= target:
            result = can_sum(target - coins[i], coins, memo, solutions, depth + 1)
            if result is not None:
                result.append(coins[i])
                if depth == 0:
                    same_length = solutions.get(len(result), list())
                    same_length.append(result)
                    solutions[len(result)] = same_length
                else:
                    return result
            else:
                memo[target] = None

    if len(solutions) == 0:
        return None
    else:
        return solutions[sorted(solutions.keys())[0]][0]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(can_sum(1, [1, 2, 5]), [1])

    def test_b(self):
        self.assertEqual(can_sum(3, [1, 2, 5]), [1, 2])

    def test_c(self):
        self.assertEqual(can_sum(3, [2, 1, 5]), [1, 2])

    def test_d(self):
        self.assertEqual(can_sum(3, [2, 5]), None)

    def test_e(self):
        self.assertEqual(can_sum(17, [2, 8]), None)

    def test_f(self):
        self.assertEqual(can_sum(1007, [2, 8]), None)

    def test_g(self):
        self.assertEqual(can_sum(7, [5, 3, 4, 7]), [7])

    def test_h(self):
        self.assertEqual(can_sum(300, [14, 7]), None)

    def test_i(self):
        self.assertEqual(can_sum(21, [5, 6]), [6, 5, 5, 5])

    def test_j(self):
        self.assertEqual(can_sum(0, [5, 6]), [])


if __name__ == '__main__':
    unittest.main()
