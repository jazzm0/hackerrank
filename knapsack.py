import sys
import unittest

sys.setrecursionlimit(5000)


# https://www.hackerrank.com/challenges/unbounded-knapsack

def solve(target, array, target_values=None):
    if target_values is None:
        target_values = set()

    target_values.add(target)

    if target == 0:
        return target_values

    if target < 0:
        return None

    for i in range(len(array)):
        if array[i] <= target:
            solve(target - array[i], array, target_values)
            if 0 in target_values:
                return target_values

    return target_values


def unboundedKnapsack(target, array):
    result = sorted(solve(target, array))
    return target - result[0]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(unboundedKnapsack(12, [1, 6, 9]), 12)

    def test_b(self):
        self.assertEqual(unboundedKnapsack(9, [3, 4, 4, 4, 8]), 9)

    def test_c(self):
        self.assertEqual(unboundedKnapsack(7, [3, 4, 4, 4, 8]), 7)

    def test_d(self):
        self.assertEqual(unboundedKnapsack(5, [3, 4, 4, 4, 8]), 4)

    def test_e(self):
        self.assertEqual(unboundedKnapsack(2000, [1]), 2000)


if __name__ == '__main__':
    unittest.main()
