import unittest


def rotateLeft(d, arr):
    return arr[d:] + arr[:d]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(rotateLeft(2, [1, 2, 3, 4, 5]), [3, 4, 5, 1, 2])


if __name__ == '__main__':
    unittest.main()
