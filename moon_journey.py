import unittest


# https://www.hackerrank.com/challenges/journey-to-the-moon

def journeyToMoon(n, astronaut):
    sizes = [1] * n
    parents = [i for i in range(n)]

    def root(a):

        while parents[a] != a:
            # update parent to grandparent
            # this will flatten tree, improving performance
            parents[a] = parents[parents[a]]
            a = parents[a]
        return a

    def findset(a, b):
        return root(a) == root(b)

    def union(a, b):
        ra = root(a)
        rb = root(b)

        # keep tree balanced using sizes array
        if sizes[ra] < sizes[rb]:
            parents[ra] = rb
            sizes[rb] += sizes[ra]
        else:
            parents[rb] = ra
            sizes[ra] += sizes[rb]

    for astro in astronaut:
        a = astro[0]
        b = astro[1]
        if not findset(a, b):
            union(a, b)

    # print(sizes)
    # print(parents)

    roots = [p for i, p in enumerate(parents) if i == p]

    # print(roots)

    # n choose 2 - sum(country_i choose 2) =>
    # n*n/2 - n/2 - sum(country_i*county_i)/2 + sum(country_i)/2
    # sum(country_i) = n
    # so reduces to just
    # (n*n - sum(country_i*county_i))/2
    N = n ** 2
    C = 0
    for r in roots:
        C += sizes[r] ** 2

    return (N - C) // 2


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(journeyToMoon(5, [[0, 1], [2, 3], [0, 4]]), 6)

    def test_b(self):
        self.assertEqual(journeyToMoon(4, [[1, 2], [2, 3]]), 3)

    def test_c(self):
        self.assertEqual(journeyToMoon(4, [[0, 2]]), 5)

    def test_d(self):
        self.assertEqual(journeyToMoon(10, [[0, 2], [1, 8], [1, 4], [2, 8], [2, 6], [3, 5], [6, 9]]), 23)

    def test_e(self):
        self.assertEqual(journeyToMoon(10, [[0, 2], [1, 8], [1, 4], [2, 8], [2, 1], [3, 8], [6, 9]]), 29)


if __name__ == '__main__':
    unittest.main()
