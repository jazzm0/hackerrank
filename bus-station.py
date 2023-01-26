import unittest


def solve(a):
    result = []
    s = sum(a)
    
    for x in range(1, s + 1):
        if s % x != 0:
            continue
        ps = 0
        i = 0
        while i < len(a):
            if ps < x:
                ps += a[i]
                i += 1
            elif ps == x:
                ps = 0
            else:
                break

        if i == len(a) and ps == x:
            result.append(x)

    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve([1, 2, 1, 1, 1, 2, 1, 3]), [3, 4, 6, 12])

    def test_b(self):
        a = [1] * 100000
        self.assertEqual(solve(a),
                         [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 80, 100, 125, 160, 200, 250, 400, 500, 625, 800,
                          1000, 1250, 2000, 2500, 3125, 4000, 5000, 6250, 10000, 12500, 20000, 25000, 50000, 100000])


if __name__ == '__main__':
    unittest.main()
