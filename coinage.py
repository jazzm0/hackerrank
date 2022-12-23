import unittest


def solve(n, coins, memo=None, bad_coins=None):
    denominations = [1, 2, 5, 10]
    if memo is None:
        memo = set()

    if bad_coins is None:
        bad_coins = {}

    current_coins = (coins[0], coins[1], coins[2], coins[3])

    if current_coins in memo:
        return

    if n in bad_coins and current_coins in bad_coins[n]:
        return

    if n == 0:
        memo.add(current_coins)

    if n < 0:
        return

    max_sum = 0
    for i in range(len(denominations)):
        max_sum += coins[i] * denominations[i]

    if max_sum < n:
        bad_solutions = bad_coins.get(n, set())
        bad_solutions.add(current_coins)
        bad_coins[n] = bad_solutions

    for i in range(len(denominations)):
        if denominations[i] <= n and coins[i] > 0:
            coins[i] -= 1
            solve(n - denominations[i], coins, memo, bad_coins)
            coins[i] += 1

    return len(memo)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve(15, [2, 3, 1, 1]), 2)

    def test_b(self):
        self.assertEqual(solve(12, [2, 2, 1, 1]), 2)

    def test_c(self):
        self.assertEqual(solve(112, [234, 68, 68, 39]), 2950)

    def test_d(self):
        self.assertEqual(solve(983, [898, 63, 63, 42]), 174793)


if __name__ == '__main__':
    unittest.main()
