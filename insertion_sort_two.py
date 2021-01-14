import unittest


def sort(i, arr):
    a = arr[i]
    i -= 1
    while a < arr[i] and i >= 0:
        arr[i + 1] = arr[i]
        i -= 1

    arr[i + 1] = a
    print(*arr, sep=" ")


def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        sort(i, arr)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(insertionSort2(5, [2, 4, 6, 8, 3]), None)

    def test_b(self):
        self.assertEqual(insertionSort2(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]), None)

    def test_c(self):
        self.assertEqual(insertionSort2(6, [1, 4, 3, 5, 6, 2]), None)

    def test_d(self):
        self.assertEqual(insertionSort2(7, [3, 4, 7, 5, 6, 2, 1]), None)


if __name__ == '__main__':
    unittest.main()
