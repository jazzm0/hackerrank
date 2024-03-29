import unittest

# https://www.hackerrank.com/challenges/nimble-game-1

first, second = 'First', 'Second'


def nimbleGame(s):
    x = 0
    for i in range(1, len(s)):
        if s[i] % 2:
            x ^= i
    return first if x else second


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(nimbleGame([0, 2, 3, 0, 6]), first)

    def test_b(self):
        self.assertEqual(nimbleGame(
            [383, 886, 777, 915, 793, 335, 386, 492, 649, 421, 362, 27, 690, 59, 763, 926, 540, 426, 172, 736, 211, 368,
             567, 429, 782, 530, 862, 123, 67, 135, 929, 802, 22, 58, 69, 167, 393, 456, 11, 42, 229, 373, 421, 919,
             784, 537, 198, 324, 315, 370, 413, 526, 91, 980, 956, 873, 862, 170, 996, 281, 305, 925, 84, 327, 336, 505,
             846, 729, 313, 857, 124, 895, 582, 545, 814, 367, 434, 364, 43, 750, 87, 808, 276, 178, 788, 584, 403, 651,
             754, 399, 932, 60, 676, 368, 739, 12, 226, 586, 94, 539]), first)


if __name__ == '__main__':
    unittest.main()
