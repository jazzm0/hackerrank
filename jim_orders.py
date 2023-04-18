import unittest


# https://www.hackerrank.com/challenges/jim-and-the-orders

def jimOrders(orders):
    priorities = []
    customer_number = 1
    for order in orders:
        priorities.append((sum(order), customer_number))
        customer_number += 1

    priorities.sort()
    return [p[1] for p in priorities]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(jimOrders([[1, 2], [2, 3], [3, 3]]), [1, 2, 3])

    def test_b(self):
        self.assertEqual(jimOrders([[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]), [4, 2, 5, 1, 3])


if __name__ == '__main__':
    unittest.main()
