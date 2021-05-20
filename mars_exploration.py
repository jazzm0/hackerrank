import unittest


def marsExploration(s):
    sos = 'SOS'
    i = 0
    counter = 0
    while i < len(s):
        for j in range(len(sos)):
            if sos[j] != s[i + j]:
                counter += 1
        i += 3
    return counter


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(marsExploration("SOSSPSSQSSOR"), 3)


if __name__ == '__main__':
    unittest.main()
