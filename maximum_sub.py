import unittest


def maxSubarray(arr):
    best_sum = 0
    current_sum = 0
    max_sequence = 0
    max_value = max(arr)

    if max_value < 0:
        return max_value, max_value

    for x in arr:
        if x > 0:
            max_sequence += x
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)

    return best_sum, max_sequence


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        result = maxSubarray([-1, 2, 3, -4, 5, 10])
        self.assertEqual(result, (16, 20))

    def test_b(self):
        result = maxSubarray([1, 2, 3, 4])
        self.assertEqual(result, (10, 10))

    def test_c(self):
        result = maxSubarray([2, -1, 2, 3, 4, -5])
        self.assertEqual(result, (10, 11))


if __name__ == '__main__':
    unittest.main()
