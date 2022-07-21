import unittest


# https://www.hackerrank.com/challenges/sherlock-and-cost


def cost(B):
    cost_a, cost_b = 0, 0
    for i in range(len(B) - 1):
        cost_a, cost_b = max(cost_a + abs(B[i + 1] - B[i]), cost_b + (B[i + 1] - 1)), max(cost_a + abs(B[i] - 1),
                                                                                          cost_b)
    return max(cost_a, cost_b)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(cost([1, 2, 3]), 2)

    def test_b(self):
        self.assertEqual(cost([10, 1, 10, 1, 10]), 36)

    def test_c(self):
        self.assertEqual(cost([1, 2, 5]), 4)

    def test_d(self):
        self.assertEqual(cost(
            [69, 19, 15, 81, 93, 100, 35, 18, 81, 16, 65, 20, 4, 45, 81, 83, 90, 14, 82, 85, 43, 7, 64, 76, 33, 47, 95,
             12, 78, 93, 14, 22, 97, 36, 65, 66, 36, 26, 59, 81, 81, 82, 44, 79, 89, 94, 32, 94, 22, 33, 19, 46, 46, 62,
             19, 47, 70, 91, 97, 62, 17, 43, 11, 25, 74, 73, 64, 98, 73, 7, 40, 8, 2, 96, 89, 81, 80, 17, 88, 13, 31,
             44, 64]), 5001)

    def test_e(self):
        self.assertEqual(cost([69, 19, 15, 81, 93]), 228)


if __name__ == '__main__':
    unittest.main()
