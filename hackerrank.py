import unittest


def hackerrankInString(s):
    hacker_rank = "hackerrank"
    index = 0
    for letter in s:

        if letter == hacker_rank[index]:
            index += 1

        if index == len(hacker_rank) - 1:
            return "YES"

    return "NO"


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(hackerrankInString('hhaacckkekraraannk'), 'YES')

    def test_b(self):
        self.assertEqual(hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'), 'NO')


if __name__ == '__main__':
    unittest.main()
