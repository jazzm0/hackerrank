import unittest
from itertools import combinations


# https://www.hackerrank.com/challenges/iterables-and-iterators

def solve(letters: list[str], k: int):
    c = list(combinations(letters, k))
    count = [1 for x in c if 'a' in x]
    return float('{0:.4f}'.format(len(count) / len(c)))

class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve(['a', 'a' ,'c' ,'d'], 2), 0.8333)




if __name__ == '__main__':
    unittest.main()
