import unittest
from collections import Counter


# https://www.hackerrank.com/challenges/string-construction


def stringConstruction(s):
    counts = Counter(s)
    return len(counts)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(stringConstruction('abcabc'), 3)

    def test_b(self):
        self.assertEqual(stringConstruction('abcd'), 4)

    def test_c(self):
        self.assertEqual(stringConstruction('aaaaaaa'), 1)

    def test_d(self):
        self.assertEqual(stringConstruction(
            'gbcebabbfffcdgfeeaadecaeecabbabbgcafeabgecfeffcbafgdegdacefcadabbfdcgcebegbfgeeebfegfacdagbbgeagaaceefcaedceacceebdgebeecedcbdbeebecgcfcgdaaaegfbcbfffccffabbceafaagdedadbfcaedaffbaggebfedegfabefafefgdbafedbggabccaedabfgfgggbcfgeggdcdfeebaedaaccefgegbffaaggdcbbbfdbgaaffbbgcfafccdgcaabccbfbgbabegddagcgfbcdfdaccegbabfedbbdaddebddgegedgaabebfeeggddagaeececcafdgddceddcbdagaecceacgfabgccecgecgcefaafcaedfccdeeceffefadeffefggaeggbbfgcacgfaeefbfbccggcbcgeagcaacdcbegcdaacdgbebdaabddeagafbfagfebfefffcbcgefbcfeggafccabfagegccefe'),
            7)

    def test_e(self):
        self.assertEqual(stringConstruction(
            'acacacabcbbccacadcabcbadcbdddbbcbcadbbccadbdaddaaadaddbdbabbaadbcdaccaddccbbcbbaddcabcadbaaddbdaabcdcbabaacbccbbabcccdbdabacccdacbcbabacabcdadcbcdccd'),
            4)


if __name__ == '__main__':
    unittest.main()
