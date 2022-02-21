import unittest


def can_construct(target, words, memo=None):
    if len(target) == 0:
        return True

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    for i in range(len(words)):
        if target.startswith(words[i]):

            memo[target] = can_construct(target[len(words[i]):], words, memo)

            if memo[target] is True:
                return True
            else:
                memo[target] = False

    return False


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(can_construct("abcdef", ["abc", "de", "g", "f"]), True)

    def test_b(self):
        self.assertEqual(can_construct("abcdef", ["abc", "de", "g"]), False)

    def test_c(self):
        self.assertEqual(can_construct("abcdef", ["abc", "de", "g"]), False)

    def test_d(self):
        self.assertEqual(can_construct("abcdef", ["abc", "ab", "de", "g", "cdef"]), True)

    def test_e(self):
        self.assertEqual(
            can_construct("abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabdeg", ["abc", "ab", "de", "g", "cdef"]),
            True)

    def test_f(self):
        self.assertEqual(can_construct("abcdef", ["cde", "abf", "ab", "de", "g"]), False)

    def test_g(self):
        self.assertEqual(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]), False)


if __name__ == '__main__':
    unittest.main()
