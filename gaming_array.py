import unittest


andy = "ANDY"
bob = "BOB"


def gamingArray(arr):
    turns = 1
    max_value, position = arr[0], 1
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            turns += 1

    if turns % 2 == 0:
        return andy
    return bob


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(gamingArray([2, 3, 5, 4, 1]), bob)

    def test_b(self):
        self.assertEqual(gamingArray([5, 2, 6, 3, 4]), andy)

    def test_c(self):
        self.assertEqual(gamingArray([3, 1]), bob)


if __name__ == "__main__":
    unittest.main()
