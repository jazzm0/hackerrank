import unittest


def commonChild(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    lcs = [[0 for _ in range(s1_len + 1)]
           for _ in range(s2_len + 1)]

    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs[s1_len][s2_len]


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(commonChild('HARRY', 'SALLY'), 2)

    def test_b(self):
        self.assertEqual(commonChild('AA', 'BB'), 0)

    def test_c(self):
        self.assertEqual(commonChild('SHINCHAN', 'NOHARAAA'), 3)  # NHA

    def test_d(self):
        self.assertEqual(commonChild('ABCDEF', 'FBDAMN'), 2)

    def test_e(self):
        self.assertEqual(commonChild(
            'ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP',
            'FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX'), 27)

    def test_f(self):
        self.assertEqual(commonChild('ABCD', 'ABDC'), 3)


if __name__ == '__main__':
    unittest.main()
