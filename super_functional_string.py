import unittest
from collections import Counter


def superFunctionalStrings(s):
    modulo = 10 ** 9 + 7
    result = 0
    seen = set()
    for current_length in range(1, len(s) + 1):
        for i in range(len(s) - current_length + 1):
            if s[i:i + current_length] not in seen:
                seen.add(s[i:i + current_length])
                counts = Counter(s[i:i + current_length])
                result += current_length ** len(counts) % modulo

    return result % modulo


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(superFunctionalStrings('aa'), 3)

    def test_b(self):
        self.assertEqual(superFunctionalStrings('aba'), 19)

    def test_c(self):
        self.assertEqual(superFunctionalStrings('abc'), 38)

    def test_d(self):
        self.assertEqual(superFunctionalStrings('swokbwzbur'), 112609122)

    def test_e(self):
        self.assertEqual(superFunctionalStrings('yyracwirtwjhpyatphxrxzptxitgiweiiweipzwjtjcxhgagyrhhrcicyzjggijgrwitwijtjrpxhgzhatgyxhgxyhjcttxwzrehprrejxiwrttwaepgartcjeageacphhxeraixjgwpjpaherxatgipptgyhyyihaipitzxxrywrpaeewwxrcigxayaijwceiwrcjhczehjxhzpziyxpgcrhtchxytihpptjarrwwjghycjextzjhxaghapywxaxajzyygpzyicczgtgggcgrceayzyayethxrxjaigiyphhygzhejiytgcwhwhwzexczzjgxrawxpxwgyywrzgepxayzhxwiythhhiprrixe'),
                         5972473)


if __name__ == '__main__':
    unittest.main()
