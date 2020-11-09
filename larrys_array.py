import unittest


def larrysArray(a):
    s = 0
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                s += 1

    if s % 2 == 0:
        return 'YES'
    else:
        return 'NO'


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(larrysArray([1, 2, 3, 5, 4]), 'NO')


if __name__ == '__main__':
    unittest.main()
