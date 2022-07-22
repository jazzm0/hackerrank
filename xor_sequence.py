import unittest


# https://www.hackerrank.com/challenges/xor-se

# A = [0] * 10 ** 5
# for i in range(1, len(A)):
#     A[i] = A[i - 1] ^ i


def index(ind):
    values = {
        **dict.fromkeys([0, 1], ind),
        **dict.fromkeys([2, 3], 2),
        **dict.fromkeys([4, 5], ind + 2),
        **dict.fromkeys([6, 7], 0),
    }

    return values.get(ind % 8)


def xorSequence(left, right):
    result = index(right) ^ index(left - 1)
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
