import unittest
from collections import Counter


def sherlockAndAnagrams(string):
    buckets = {}
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i + j]).items())
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key] - 1) // 2
    return count


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(sherlockAndAnagrams('abba'), 4)

    def test_b(self):
        self.assertEqual(sherlockAndAnagrams('abcd'), 0)

    def test_c(self):
        self.assertEqual(sherlockAndAnagrams('ifailuhkqq'), 3)

    def test_d(self):
        self.assertEqual(sherlockAndAnagrams('kkkk'), 10)

    def test_e(self):
        self.assertEqual(sherlockAndAnagrams(
            'ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel'),
            399)

    def test_f(self):
        self.assertEqual(sherlockAndAnagrams(
            'zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw'),
            428)


if __name__ == '__main__':
    unittest.main()
