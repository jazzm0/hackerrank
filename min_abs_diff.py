import unittest


# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    result = abs(arr[0] - arr[len(arr) - 1])

    for i in range(len(arr) - 1):
        result = min(result, abs(arr[i] - arr[i + 1]))

    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(minimumAbsoluteDifference([-2, 2, 4]), 2)

    def test_b(self):
        self.assertEqual(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]), 1)


if __name__ == '__main__':
    unittest.main()
