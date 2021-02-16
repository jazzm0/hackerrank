import unittest


def maximumSum(a, m):
    for i in range(len(a)):
        a[i] %= m

    max_value = 0
    for i in range(len(a)):
        current_value = 0
        for j in range(i, len(a)):
            current_value = (current_value + a[j]) % m
            max_value = max(max_value, current_value)
    return max_value


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(maximumSum([3, 3, 9, 9, 5], 7), 6)

    def test_b(self):
        self.assertEqual(maximumSum([1, 2, 3], 2), 1)

    def test_c(self):
        self.assertEqual(
            maximumSum([846930887, 1681692778, 1714636916, 1957747794, 424238336, 719885387, 1649760493, 596516650,
                        1189641422, 1025202363, 1350490028, 783368691, 1102520060, 2044897764, 1967513927, 1365180541,
                        1540383427, 304089173, 1303455737, 35005212, 521595369, 294702568, 1726956430, 336465783,
                        861021531,
                        278722863, 233665124, 2145174068, 468703136, 1101513930, 1801979803, 1315634023, 635723059,
                        1369133070,
                        1125898168, 1059961394, 2089018457, 628175012, 1656478043, 1131176230, 1653377374, 859484422,
                        1914544920,
                        608413785, 756898538, 1734575199, 1973594325, 149798316, 2038664371, 1129566414], 1804289384),
            1802192837)


if __name__ == '__main__':
    unittest.main()
