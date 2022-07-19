import unittest


# https://www.hackerrank.com/challenges/build-a-string

def lcs(s1, s2):
    longest = 1
    while s2[0:longest] in s1 and longest < len(s2) + 1:
        longest += 1
    return longest - 1


def buildString(a, b, s):
    i = 1
    cost = a
    while i < len(s):
        longest = lcs(s[0:i], s[i:])
        if longest * a > b:
            cost += b
            i += longest
        else:
            cost += a
            i += 1

    return cost


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(buildString(4, 5, 'aabaacaba'), 26)

    def test_b(self):
        self.assertEqual(buildString(8, 9, 'bacbacacb'), 42)

    def test_c(self):
        self.assertEqual(buildString(2709, 2712,
                                     'caackncaacknggikncaacknggaacknggikncaackggikncaacknggaacknggikncakqoaacknggikncacggihikncaomhikncaom'),
                         65040)

    def test_d(self):
        self.assertEqual(buildString(7890, 7891,
                                     'acbcrsjcrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcrsjrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcsbcbcrsjh'),
                         126246)

    def test_e(self):
        self.assertEqual(buildString(7078, 7078,
                                     'abbciabbcabciabbcmabbciabbcahlbchgcmabbcmggcmababciabbcagerafrciabbcsrhgcmcabciabbchgcmabbcmsfabcmsr'),
                         268964)

    def test_f(self):
        self.assertEqual(buildString(10, 11, 'cbcjbcbcjh'), 71)


if __name__ == '__main__':
    unittest.main()
