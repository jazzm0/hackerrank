import unittest


def solve(numbers, a, b):
    happiness = 0
    a = set(a)
    b = set(b)
    for n in numbers:
        if n in a:
            happiness += 1
        elif n in b:
            happiness -= 1
    return happiness


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(solve([1, 5, 3], [3, 1], [5, 7]), 1)


if __name__ == "__main__":
    unittest.main()
