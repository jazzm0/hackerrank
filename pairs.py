import unittest


def pairs(k, arr):
    count = 0
    arr = set(arr)
    for i in arr:
        if (k + i) in arr:
            count += 1

    return count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(pairs(2, [1, 5, 3, 4, 2]), 3)

    def test_b(self):
        self.assertEqual(pairs(1, [1, 2, 3, 4]), 3)


if __name__ == '__main__':
    unittest.main()
