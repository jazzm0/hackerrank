import unittest


def minimumLoss(price):
    min_loss = 100000000000000000
    sorted_prices = sorted(price)

    positions = {}
    for i in range(len(price)):
        positions[price[i]] = i

    for i in range(len(sorted_prices) - 1):
        actual_difference = sorted_prices[i + 1] - sorted_prices[i]
        if actual_difference < min_loss and positions[sorted_prices[i]] > positions[sorted_prices[i + 1]]:
            min_loss = actual_difference

    return min_loss


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(minimumLoss([20, 15, 8, 2, 12]), 3)

    def test_b(self):
        self.assertEqual(minimumLoss([20, 7, 8, 2, 5]), 2)


if __name__ == '__main__':
    unittest.main()
