import unittest


def almostSorted(arr):
    sorted_a = sorted(arr)

    ret = 0
    wrong = list()

    for i in range(len(arr)):
        if arr[i] != sorted_a[i]:
            ret += 1
            wrong.append(i)

    if ret == 2:
        print('yes')
        print('swap {} {}'.format(wrong[0] + 1, wrong[1] + 1))
        return 'yes'
    else:
        for i in range(len(wrong) - 1):
            if arr[wrong[i]] < arr[wrong[i + 1]]:
                print('no')
                return 'no'
        print('yes')
        print('reverse {} {}'.format(wrong[0] + 1, wrong[len(wrong) - 1] + 1))
        return 'yes'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(almostSorted([1, 2, 3, 5, 4]), 'yes')

    def test_b(self):
        self.assertEqual(almostSorted([1, 5, 4, 3, 2, 6]), 'yes')

    def test_c(self):
        self.assertEqual(almostSorted([1, 5, 3, 4, 6, 2]), 'no')

    def test_d(self):
        self.assertEqual(almostSorted([3, 1, 2]), 'no')

    def test_e(self):
        with open('almost_sorted_test_a.txt') as ifile:
            for line in ifile:
                line = [int(i) for i in line.split(' ')]

        self.assertEqual(almostSorted(line), 'yes')


if __name__ == '__main__':
    unittest.main()
