import unittest


# https://www.hackerrank.com/challenges/tower-breakers-1

def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    return 1


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(towerBreakers(2, 2), 2)


if __name__ == '__main__':
    unittest.main()
