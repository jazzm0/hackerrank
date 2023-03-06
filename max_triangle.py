import unittest


# https://www.hackerrank.com/challenges/maximum-perimeter-triangle

def maximumPerimeterTriangle(sticks):
    sticks = sorted(sticks)
    i = len(sticks) - 1
    a, b, c, max_sum, temp_sum = -1, -1, -1, 0, 0
    while i > 1:
        temp_sum = sticks[i - 1] + sticks[i - 2]
        if sticks[i] < temp_sum:
            temp_sum += sticks[i]
            if temp_sum > max_sum:
                c, b, a, max_sum = sticks[i], sticks[i - 1], sticks[i - 2], temp_sum
        i -= 1

    if a > 0:
        return [a, b, c]
    else:
        return [-1]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(maximumPerimeterTriangle([1, 2, 3, 4, 5, 10]), [3, 4, 5])

    def test_b(self):
        self.assertEqual(maximumPerimeterTriangle([1, 1, 1, 3, 3]), [1, 3, 3])

    def test_c(self):
        self.assertEqual(maximumPerimeterTriangle([1, 1, 1, 2, 3, 5]), [1, 1, 1])

    def test_d(self):
        self.assertEqual(maximumPerimeterTriangle([1, 2, 3]), [-1])


if __name__ == '__main__':
    unittest.main()
