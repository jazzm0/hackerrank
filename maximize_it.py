import unittest


# https://www.hackerrank.com/challenges/maximize-it

def maximize_it(lists, m):
    k = len(lists)

    # Initialize the dp table
    dp = [[0] * m for _ in range(k)]

    # Initialize the first row of dp table
    for num in lists[0]:
        dp[0][num * num % m] = max(dp[0][num * num % m], num * num % m)

    # Fill the dp table
    for i in range(1, k):
        for num in lists[i]:
            num_sq_mod = num * num % m
            for j in range(m):
                if dp[i - 1][j] != 0 or (i == 1 and j == 0):
                    new_mod = (j + num_sq_mod) % m
                    dp[i][new_mod] = max(dp[i][new_mod], dp[i - 1][j] + num_sq_mod)

    # The result is the maximum value in the last row of dp table
    return max(dp[k - 1])


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(maximize_it([
            [2, 5, 4],
            [3, 7, 8, 9],
            [5, 5, 7, 8, 9, 10]
        ], 1000), 206)


if __name__ == '__main__':
    unittest.main()
