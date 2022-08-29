import unittest


# https://www.hackerrank.com/challenges/greedy-florist

def getMinimumCost(k, c):
    c = sorted(c, reverse=True)
    result = 0
    multiplier = 1
    for i in range(len(c)):
        result += c[i] * multiplier
        if (i + 1) % k == 0:
            multiplier += 1
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(getMinimumCost(3, [2, 5, 6]), 13)

    def test_b(self):
        self.assertEqual(getMinimumCost(3, [1, 3, 5, 7, 9]), 29)

    def test_c(self):
        self.assertEqual(getMinimumCost(3,
                                        [390225, 426456, 688267, 800389, 990107, 439248, 240638, 15991, 874479, 568754,
                                         729927, 980985, 132244, 488186, 5037, 721765, 251885, 28458, 23710, 281490,
                                         30935, 897665, 768945, 337228, 533277, 959855, 927447, 941485, 24242, 684459,
                                         312855, 716170, 512600, 608266, 779912, 950103, 211756, 665028, 642996, 262173,
                                         789020, 932421, 390745, 433434, 350262, 463568, 668809, 305781, 815771,
                                         550800]), 163578911)


if __name__ == '__main__':
    unittest.main()
