import unittest


# https://www.hackerrank.com/challenges/diwali-lights

def lights(n):
    return ((2 ** n) - 1) % 10 ** 5


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(lights(1), 1)

    def test_b(self):
        self.assertEqual(lights(2), 3)

    def test_c(self):
        self.assertEqual(lights(8291), 4447)


if __name__ == '__main__':
    unittest.main()
