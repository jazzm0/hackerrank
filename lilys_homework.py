import unittest


def count(arr, b):
    m = {}
    for i in range(len(arr)):
        m[arr[i]] = i

    sorted_a = sorted(arr, reverse=b)
    ret = 0

    for i in range(len(arr)):
        if arr[i] != sorted_a[i]:
            ret += 1

            ind_to_swap = m[sorted_a[i]]
            m[arr[i]] = m[sorted_a[i]]
            arr[i], arr[ind_to_swap] = sorted_a[i], arr[i]

    return ret


def lilysHomework(arr):
    a = count(list(arr), False)
    b = count(list(arr), True)
    return min(a, b)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(lilysHomework([7, 15, 12, 3]), 2)

    def test_b(self):
        self.assertEqual(lilysHomework([2, 5, 3, 1]), 2)


if __name__ == '__main__':
    unittest.main()
