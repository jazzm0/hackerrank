import unittest


# https://www.hackerrank.com/challenges/a-chocolate-fiesta

def solve(a):
    mod = 10 ** 9 + 7
    n = len(a)
    if all(a[i] == a[0] for i in range(len(a))):
        return ((2 ** n) - 1) % mod
    return ((2 ** (n - 1)) - 1) % mod


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve([2, 4, 6, 1]), 7)

    def test_b(self):
        self.assertEqual(solve([1, 2, 2]), 3)

    def test_c(self):
        self.assertEqual(solve(
            [233, 960, 27, 817, 961, 919, 450, 19, 882, 278, 217, 304, 742, 920, 605, 92, 376, 64, 837, 31, 893, 273,
             689, 188, 18, 334, 952, 807, 847, 296, 630, 80, 256, 657, 249, 570, 928, 699, 589, 811, 977, 806, 467, 71,
             78, 72, 515, 806, 137, 352, 837, 382, 626, 879, 571, 996, 565, 875, 803, 412, 523, 785, 844, 780, 443, 93,
             350, 723, 792, 291, 534, 121, 97, 353, 544, 527, 426, 412, 333, 915, 764, 523, 649, 742, 402, 572, 90, 319,
             447, 246, 731, 323, 31, 927, 103, 826, 20, 805, 550, 164]), 988185645)


if __name__ == '__main__':
    unittest.main()
