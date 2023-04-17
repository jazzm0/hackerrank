import unittest


# https://www.hackerrank.com/challenges/largest-permutation

def largestPermutation(k, arr):
    index_map = {}
    for i in range(len(arr)):
        index_map[arr[i]] = i

    next_highest_digit = len(arr)
    for index in range(len(arr)):

        if k == 0:
            break

        if index != index_map[next_highest_digit]:
            tmp = arr[index]
            arr[index] = arr[index_map[next_highest_digit]]
            arr[index_map[next_highest_digit]] = tmp
            k -= 1
            index_map[tmp] = index_map[next_highest_digit]
            index_map[next_highest_digit] = index

        next_highest_digit -= 1

    return arr


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(largestPermutation(1, [1, 2, 3, 4]), [4, 2, 3, 1])

    def test_b(self):
        self.assertEqual(largestPermutation(2, [1, 2, 3, 4]), [4, 3, 2, 1])

    def test_c(self):
        self.assertEqual(largestPermutation(1, [4, 2, 3, 5, 1]), [5, 2, 3, 4, 1])


if __name__ == '__main__':
    unittest.main()
