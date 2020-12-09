import unittest


# https://www.hackerrank.com/challenges/beautiful-3-set/problem?h_r=internal-search
# ?

def b3set(n):
    result = list()

    k = (2 * n) // 3
    print(k + 1)
    y = 2 * k - n
    x = n - 2 * y

    for i in range(0, y + 1):
        result.append((i, x + i, n - x - 2 * i))

    for i in range(0, k - y):
        result.append((i + y + 1, i, n - y - 1 - 2 * i))

    for i in range(len(result)):
        print("{0} {1} {2}".format(result[i][0], result[i][1], result[i][2]))

    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(b3set(3),
                         [(0, 1, 2),
                          (1, 2, 0),
                          (2, 0, 1)])

    def test_b(self):
        self.assertEqual(b3set(2),
                         [(0, 2, 0),
                          (1, 0, 1)])


if __name__ == '__main__':
    unittest.main()
