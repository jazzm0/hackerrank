import unittest


# https://www.hackerrank.com/challenges/equal

def equal(arr):
    m = min(arr)
    t = [0] * 4
    for i in arr:
        for j in range(4):
            x = i - (m - j)
            x = x // 5 + (x % 5) // 2 + (x % 5) % 2
            t[j] += x
    return min(t)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(equal([10, 7, 12]), 3)

    def test_b(self):
        self.assertEqual(equal([2, 2, 3, 7]), 2)


if __name__ == '__main__':
    unittest.main()
