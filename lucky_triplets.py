import unittest


# 2 <= len(l) <= 2000
# 1 <= l[i] <= 999999

def solution(l):
    n = len(l)
    c = [0] * n
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if l[j] % l[i] == 0:
                c[j] += 1
                count += c[i]

    return count


# def solution(l):
#     count = 0
#     for i in range(len(l)):
#         for j in range(i + 1, len(l)):
#             if l[j] % l[i] == 0:
#                 for k in range(j + 1, len(l)):
#                     if l[k] % l[j] == 0:
#                         count += 1
#     return count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 3)

    def test_b(self):
        self.assertEqual(solution([1, 1, 1]), 1)

    def test_c(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36]), 43)


if __name__ == '__main__':
    unittest.main()
