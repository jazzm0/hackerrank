import unittest


# https://www.hackerrank.com/challenges/marcs-cakewalk

def marcsCakewalk(calorie):
    calorie = sorted(calorie, reverse=True)
    result = 0

    for i in range(len(calorie)):
        result += 2 ** i * calorie[i]

    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(marcsCakewalk([1, 3, 2]), 11)


if __name__ == '__main__':
    unittest.main()
