import math
import unittest
from bisect import bisect_left


def median(a, u):
    return 0.5 * (a[math.floor(u / 2)] + a[math.ceil(u / 2)])


def activityNotifications(expenditure, d):
    notifications = 0
    sorted_history = list()
    history = list()
    for i in range(len(expenditure) - 1):

        index = bisect_left(sorted_history, expenditure[i])
        sorted_history.insert(index, expenditure[i])
        history.append(expenditure[i])

        if len(sorted_history) > d:
            removed = history.pop(0)
            del sorted_history[bisect_left(sorted_history, removed)]

        if len(sorted_history) == d:
            m = median(sorted_history, d - 1)
            if expenditure[i + 1] >= 2 * m:
                notifications += 1

    return notifications


class TestStringMethods(unittest.TestCase):

    def test_median_a(self):
        self.assertEqual(median([10, 20, 30, 40, 50], 2), 20)

    def test_median_b(self):
        self.assertEqual(median([10, 20, 30, 40, 50], 3), 25)

    def test_median_c(self):
        self.assertEqual(median([10, 20, 30, 40, 50], 4), 30)

    def test_a(self):
        self.assertEqual(activityNotifications([10, 20, 30, 40, 50], 3), 1)

    def test_b(self):
        self.assertEqual(activityNotifications([10, 20, 30, 50, 80, 60, 70, 150], 4), 2)

    def test_c(self):
        self.assertEqual(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5), 2)


if __name__ == '__main__':
    unittest.main()
