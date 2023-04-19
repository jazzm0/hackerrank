import unittest
from bisect import bisect_left


# https://www.hackerrank.com/challenges/sherlock-and-minimax

def sherlockAndMinimax(arr, p, q):
    arr.sort()
    n = len(arr)
    numbers = set(arr)

    if p < arr[0] and q > arr[n - 1]:
        if (arr[0] - p) >= (q - arr[n - 1]):
            return p
        else:
            return q

    if q < arr[0]:
        return p

    if p > arr[n - 1]:
        return q

    max_distance, actual_min, result = 0, 0, -1

    x = p

    while x <= q:
        if x in numbers:
            x += 1
            continue

        position = bisect_left(arr, x, 0, n)

        if 0 < position < n:
            actual_min = min(abs(arr[position] - x), abs(arr[position - 1] - x))

        elif position == 0:
            actual_min = arr[0] - x

        elif position == n:
            actual_min = x - arr[n - 1]

        if actual_min > max_distance:
            result = x
            max_distance = actual_min

        x += 1

    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(sherlockAndMinimax([3, 5, 7, 9], 6, 8), 6)

    def test_b(self):
        self.assertEqual(sherlockAndMinimax([5, 8, 14], 4, 9), 4)

    def test_c(self):
        self.assertEqual(sherlockAndMinimax([38, 50, 60, 30, 48], 23, 69), 69)

    # def test_d(self):
    #     self.assertEqual(sherlockAndMinimax(
    #         [263044060, 323471968, 60083128, 764550014, 209332334, 735326740, 558683912, 626871620, 232673588,
    #          428805364, 221674872, 261029278, 139767646, 146996700, 200921412, 121542678, 96223500, 239197414,
    #          407346706, 143348970, 60722446, 664904326, 352123022, 291011666, 594294166, 397870656, 60694236, 376586636,
    #          486260888, 114933906, 493037208, 5321608, 90019990, 601686988, 712093982, 575851770, 411329684, 462785470,
    #          563110618, 232790384, 511246848, 521904074, 550301294, 142371172, 241067834, 14042944, 249208926, 36834004,
    #          69321106, 467588012, 92173320, 360474676, 221615472, 340320496, 62541478, 360772498, 372355942, 445408968,
    #          342087972, 685617022, 307398890, 437939090, 720057720, 718957462, 387059594, 583359512, 589920332,
    #          500463226, 770726204, 434976772, 567860154, 510626506, 614077600, 620953322, 570332092, 623026436,
    #          502427638, 640333172, 370673998], 70283784, 302962359), 173959056)

    def test_e(self):
        self.assertEqual(sherlockAndMinimax([1, 101], 1, 9), 9)

    def test_f(self):
        self.assertEqual(sherlockAndMinimax([3, 102], 1, 98), 52)


if __name__ == '__main__':
    unittest.main()
