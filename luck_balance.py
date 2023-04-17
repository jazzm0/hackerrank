import unittest


# https://www.hackerrank.com/challenges/luck-balance

def luckBalance(k, contests):
    contests = sorted(contests, reverse=True)
    luck_balance = 0

    for i in range(len(contests)):
        if contests[i][1] == 1:
            if k > 0:
                k -= 1
                luck_balance += contests[i][0]
            else:
                luck_balance -= contests[i][0]
        else:
            luck_balance += contests[i][0]

    return luck_balance


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(luckBalance(2, [[5, 1], [1, 1], [4, 0]]), 10)

    def test_b(self):
        self.assertEqual(luckBalance(1, [[5, 1], [1, 1], [4, 0]]), 8)


if __name__ == '__main__':
    unittest.main()
