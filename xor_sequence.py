import unittest


# https://www.hackerrank.com/challenges/xor-se

# A = [0] * 10 ** 5
# for i in range(1, len(A)):
#     A[i] = A[i - 1] ^ i


def index(ind):
    values = {
        0: ind,
        1: 1,
        2: ind + 1,
        3: 0,
    }

    return values.get(ind % 4)


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
        self.assertEqual(xorSequence(5, 25), 31)


if __name__ == '__main__':
    unittest.main()
