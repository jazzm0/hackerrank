import unittest


# https://www.hackerrank.com/challenges/strong-password

def minimumNumber(n, password):
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    lower_case = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y'}

    upper_case = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z'}

    special_characters = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'}

    n = l = u = s = 1

    for p in password:
        if n == 0 and l == 0 and u == 0 and s == 0:
            break
        if p in numbers and n == 1:
            n = 0
        if p in lower_case and l == 1:
            l = 0
        if p in upper_case and u == 1:
            u = 0
        if p in special_characters and s == 1:
            s = 0

    length = len(password)
    d = max(0, 6 - length)
    return max(d, n + l + u + s)


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(minimumNumber(3, "Ab1"), 3)


if __name__ == '__main__':
    unittest.main()
