import unittest


def hackerlandRadioTransmitters(x, k):
    x = sorted(set(x))
    count = 0
    i = 0
    while i < len(x):
        count += 1
        location = x[i] + k
        while i < len(x) and x[i] <= location:
            i += 1
        location = x[i - 1] + k
        while i < len(x) and x[i] <= location:
            i += 1

    return count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(hackerlandRadioTransmitters([1, 2, 3, 5, 9], 1.3), 3)

    def test_b(self):
        self.assertEqual(hackerlandRadioTransmitters([1, 2, 3, 4, 5], 1), 2)

    def test_c(self):
        self.assertEqual(hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9, 12, 11], 2), 3)

    def test_d(self):
        self.assertEqual(hackerlandRadioTransmitters([2, 2, 2, 2, 1, 1], 1), 1)

    def test_e(self):
        self.assertEqual(hackerlandRadioTransmitters([9, 5, 4, 2, 6, 15, 12], 2), 4)


if __name__ == '__main__':
    unittest.main()
