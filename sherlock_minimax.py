import unittest
from bisect import bisect_left


# https://www.hackerrank.com/challenges/sherlock-and-minimax

def sherlockAndMinimax(arr, p, q):
    arr.sort()
    n = len(arr)
    max_distance, max_position = 0, -1

    position = bisect_left(arr, q, 0, n)

    if position < n:
        distance = min(arr[position] - q, q - arr[position - 1])
        max_distance, max_position = distance, q

    if p < arr[0]:
        distance = arr[0] - p
        if distance > max_distance or (distance == max_distance and p < max_position):
            max_distance, max_position = distance, p

    if q > arr[n - 1]:
        distance = q - arr[n - 1]
        if distance > max_distance or (distance == max_distance and q < max_position):
            max_distance, max_position = distance, q

    for i in range(n - 1):
        position = (arr[i] + arr[i + 1]) // 2
        distance = min(arr[i + 1] - position, position - arr[i])
        if p <= position <= q and (distance > max_distance or (distance == max_distance and position < max_position)):
            max_distance, max_position = distance, position

    return max_position


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(sherlockAndMinimax([3, 5, 7, 9], 6, 8), 6)

    def test_b(self):
        self.assertEqual(sherlockAndMinimax([5, 8, 14], 4, 9), 4)

    def test_c(self):
        self.assertEqual(sherlockAndMinimax([38, 50, 60, 30, 48], 23, 69), 69)

    def test_d(self):
        self.assertEqual(sherlockAndMinimax(
            [263044060, 323471968, 60083128, 764550014, 209332334, 735326740, 558683912, 626871620, 232673588,
             428805364, 221674872, 261029278, 139767646, 146996700, 200921412, 121542678, 96223500, 239197414,
             407346706, 143348970, 60722446, 664904326, 352123022, 291011666, 594294166, 397870656, 60694236, 376586636,
             486260888, 114933906, 493037208, 5321608, 90019990, 601686988, 712093982, 575851770, 411329684, 462785470,
             563110618, 232790384, 511246848, 521904074, 550301294, 142371172, 241067834, 14042944, 249208926, 36834004,
             69321106, 467588012, 92173320, 360474676, 221615472, 340320496, 62541478, 360772498, 372355942, 445408968,
             342087972, 685617022, 307398890, 437939090, 720057720, 718957462, 387059594, 583359512, 589920332,
             500463226, 770726204, 434976772, 567860154, 510626506, 614077600, 620953322, 570332092, 623026436,
             502427638, 640333172, 370673998], 70283784, 302962359), 173959056)

    def test_e(self):
        self.assertEqual(sherlockAndMinimax([1, 101], 1, 9), 9)

    def test_f(self):
        self.assertEqual(sherlockAndMinimax([3, 102], 1, 98), 52)

    def test_g(self):
        self.assertEqual(sherlockAndMinimax([12, 10, 50, 24, 40], 9, 16), 16)


if __name__ == '__main__':
    unittest.main()
