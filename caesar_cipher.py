import unittest


# https://www.hackerrank.com/challenges/caesar-cipher-1

def get_r_alphabet(k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    caesar_map = {}

    for i in range(len(original)):
        caesar_map[original[i]] = original[(i + k) % len(original)]

    return caesar_map


def caesarCipher(s, k):
    caesar_alphabet = get_r_alphabet(k)
    result = ''
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                result += caesar_alphabet[s[i].lower()].upper()
            else:
                result += caesar_alphabet[s[i]]
        else:
            result += s[i]

    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(caesarCipher('middle-Outz', 2), 'okffng-Qwvb')

    def test_b(self):
        self.assertEqual(caesarCipher('There\'s-a-starman-in-the-sky', 3), 'Wkhuh\'v-d-vwdupdq-lq-wkh-vnb')


if __name__ == '__main__':
    unittest.main()
