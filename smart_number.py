import math
import unittest


# https://www.hackerrank.com/challenges/smart-number


def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(is_smart_number(169), True)

    def test_b(self):
        self.assertEqual(is_smart_number(4), True)

    def test_c(self):
        self.assertEqual(is_smart_number(17), False)

    def test_d(self):
        self.assertEqual(is_smart_number(100), True)

    def test_e(self):
        self.assertEqual(is_smart_number(16), True)


if __name__ == '__main__':
    unittest.main()
