import unittest


# https://www.hackerrank.com/challenges/icecream-parlor

def icecreamParlor(m, arr):
    positions = {}
    for i in range(len(arr)):
        index = positions.get(arr[i], set())
        index.add(i)
        positions[arr[i]] = index

    for i in range(len(arr)):
        if (m - arr[i]) in positions.keys():
            for j in positions[m - arr[i]]:
                if j != i:
                    return i + 1, j + 1


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(icecreamParlor(4, [1, 4, 5, 3, 2]), (1, 4))

    def test_b(self):
        self.assertEqual(icecreamParlor(4, [2, 2, 4, 3]), (1, 2))


if __name__ == '__main__':
    unittest.main()
