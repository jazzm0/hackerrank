import unittest


# https://www.hackerrank.com/challenges/string-construction

def stringConstruction(s):
    cost = 0
    i = 0
    p = ''
    length_s = len(s)
    seen = set()
    while i < length_s:
        length = 1
        while s[i:i + length] in p and length < len(p):
            length += 1

        if length > 1 and s[i:i + length] not in p:
            length -= 1

        p = p + s[i:i + length]

        if length == 1 and s[i] not in seen:
            cost += 1

        for c in s[i:i + length]:
            seen.add(c)

        i += length

    return cost


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
