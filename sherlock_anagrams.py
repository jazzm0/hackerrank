import unittest


def anagram(s, q):
    if len(s) != len(q):
        return False

    char_count_s = {}
    char_count_q = {}

    for i in range(len(s)):
        char_count_s[s[i]] = char_count_s.get(s[i], 0) + 1
        char_count_q[q[i]] = char_count_q.get(q[i], 0) + 1

    for k, v in char_count_s.items():
        if char_count_q.get(k) != v:
            return False

    return True


def sherlockAndAnagrams(s):
    count = 0

    for length in range(1, len(s)):
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if anagram(s[i:i + length], s[j:j + length]):
                    count += 1

    return count


class TestStringMethods(unittest.TestCase):
    def test_a1(self):
        self.assertEqual(anagram('abba', 'baba'), True)

    def test_a2(self):
        self.assertEqual(anagram('abba', 'babc'), False)

    def test_a(self):
        self.assertEqual(sherlockAndAnagrams('abba'), 4)

    def test_b(self):
        self.assertEqual(sherlockAndAnagrams('abcd'), 0)

    def test_c(self):
        self.assertEqual(sherlockAndAnagrams('ifailuhkqq'), 3)

    def test_d(self):
        self.assertEqual(sherlockAndAnagrams('kkkk'), 10)

    def test_e(self):
        self.assertEqual(sherlockAndAnagrams('ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel'), 399)

    def test_f(self):
        self.assertEqual(sherlockAndAnagrams('zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw'), 428)


if __name__ == '__main__':
    unittest.main()
