import unittest


# https://www.hackerrank.com/challenges/gridland-metro

def gridlandMetro(n, m, k, track):
    d = {}
    for t in track:
        r = d.get(t[0] - 1, list())
        r.append((t[1], t[2]))
        d[t[0] - 1] = r

    for k, v in d.items():
        v = sorted(v)
        i = 0
        while i < len(v) - 1:
            if v[i + 1][0] <= v[i][0] or v[i + 1][0] <= v[i][1]:
                merged = (min(v[i][0], v[i + 1][0]), max(v[i][1], v[i + 1][1]))
                v.pop(i)
                v[i] = merged
            else:
                i += 1
        d[k] = v

    occupied = 0

    for k, v in d.items():
        for i in range(len(v)):
            occupied += v[i][1] - v[i][0] + 1

    return n * m - occupied


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(gridlandMetro(4, 4, 3,
                                       [
                                           [2, 2, 3],
                                           [3, 1, 4],
                                           [4, 4, 4]]), 9)

    def test_b(self):
        self.assertEqual(gridlandMetro(1, 5, 3,
                                       [
                                           [1, 1, 2],
                                           [1, 3, 5],
                                           [1, 2, 4]]), 0)


if __name__ == '__main__':
    unittest.main()
