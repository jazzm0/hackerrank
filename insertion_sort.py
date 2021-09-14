import unittest


# https://www.hackerrank.com/challenges/correctness-invariant/

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(insertion_sort([7, 4, 3, 5, 6, 2]), [2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
