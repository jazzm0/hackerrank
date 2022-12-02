import unittest


# https://www.hackerrank.com/challenges/filling-jars

def solve(n, operations):
    avg = 0
    for operation in operations:
        avg += (operation[1] - operation[0] + 1) * operation[2]

    return avg // n


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve(5, [[1, 2, 10], [3, 5, 10]]), 10)

    def test_b(self):
        self.assertEqual(solve(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]), 160)


if __name__ == '__main__':
    unittest.main()
