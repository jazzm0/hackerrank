import unittest


# https://www.hackerrank.com/challenges/camelcase

def camelcase(s):
    count = 0
    for i in range(len(s)):
        if s[i].isalpha() and s[i].isupper():
            count += 1
    return count + 1


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(camelcase('oneTwoThree'), 3)

    def test_b(self):
        self.assertEqual(camelcase('saveChangesInTheEditor'), 5)


if __name__ == '__main__':
    unittest.main()
