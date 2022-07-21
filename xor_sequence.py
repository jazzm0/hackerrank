import unittest


# https://www.hackerrank.com/challenges/xor-se

# A = [0] * 10 ** 5
# for i in range(1, len(A)):
#     A[i] = A[i - 1] ^ i


def index(ind):
    if ind % 4 == 0:
        return ind
    if ind % 4 == 1:
        return 1
    if ind % 4 == 2:
        return ind + 1
    if ind % 4 == 3:
        return 0


def xorSequence(l, r):
    result = index(l)
    for j in range(l + 1, r + 1):
        result ^= index(j)
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(xorSequence(2, 4), 7)

    def test_b(self):
        self.assertEqual(xorSequence(2, 8), 9)

    def test_c(self):
        self.assertEqual(xorSequence(5, 9), 15)


if __name__ == '__main__':
    unittest.main()
