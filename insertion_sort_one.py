import unittest


def insertionSort1(n, arr):
    i = len(arr) - 1
    a = arr[i]
    i -= 1
    while a < arr[i] and i >= 0:
        arr[i + 1] = arr[i]
        print(*arr, sep=" ")
        i -= 1

    arr[i + 1] = a
    print(*arr, sep=" ")


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(insertionSort1(5, [2, 4, 6, 8, 3]), None)

    def test_b(self):
        self.assertEqual(insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]), None)


if __name__ == '__main__':
    unittest.main()
