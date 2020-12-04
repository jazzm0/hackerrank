import unittest


def commonChild(s1, s2):
    n = len(s1)
    c = [[0] * (n + 1) for i in range(n + 1)]
    m = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
            m = max(m, c[i][j])

    return m


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(commonChild('HARRY', 'SALLY'), 2)

    def test_b(self):
        self.assertEqual(commonChild('AA', 'BB'), 0)

    def test_c(self):
        self.assertEqual(commonChild('SHINCHAN', 'NOHARAAA'), 3)

    def test_d(self):
        self.assertEqual(commonChild('ABCDEF', 'FBDAMN'), 2)

    def test_e(self):
        self.assertEqual(commonChild(
            'ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP',
            'FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX'), 27)


if __name__ == '__main__':
    unittest.main()
