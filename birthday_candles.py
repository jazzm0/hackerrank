import unittest


def birthdayCakeCandles(candles):
    counts = {}
    max_value = -1
    for i in range(len(candles)):
        counts[candles[i]] = counts.get(candles[i], 0) + 1
        if candles[i] > max_value:
            max_value = candles[i]

    return counts[max_value]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(birthdayCakeCandles([4, 4, 1, 3]), 2)


if __name__ == '__main__':
    unittest.main()
