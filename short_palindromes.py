import unittest


# https://www.hackerrank.com/challenges/short-palindrome

def shortPalindrome(s):
    # Write your code here
    # dim1[i] - number of times character i has been seen so far
    # dim2[i][j] - number of tuples of (i, j) characters seen so far
    # dim3[i] - number of tuples of (i,j,j) tuples seen so far
    dim1 = [0] * 26
    dim2 = [0] * 26 * 26
    dim3 = [0] * 26
    count = 0
    mod = 1000000007
    for k in s:
        c = ord(k) - ord('a')
        count = (count + dim3[c]) % mod
        ic = c
        for i in range(26):
            dim3[i] = (dim3[i] + dim2[ic]) % mod
            dim2[ic] = (dim2[ic] + dim1[i]) % mod
            ic += 26
        dim1[c] += 1
    return count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(shortPalindrome('kkkkkkz'), 15)


if __name__ == '__main__':
    unittest.main()
