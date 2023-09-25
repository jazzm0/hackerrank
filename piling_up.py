# import unittest
import unittest
from collections import deque


def solve(numbers):
    numbers = deque(numbers)
    top = max(numbers[0], numbers[-1])
    while len(numbers) > 0:
        if len(numbers) == 1 and numbers[0] <= top:
            numbers.pop()
            break
        if numbers[-1] < numbers[0] <= top:
            top = numbers.popleft()
        elif numbers[0] < numbers[-1] <= top:
            top = numbers.pop()
        elif numbers[0] == numbers[-1]:
            numbers.pop()
            numbers.popleft()
        else:
            break
    if len(numbers) == 0:
        return "Yes"
    return "No"


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(solve([1, 2, 3, 8, 7]), "No")

    def test_b(self):
        self.assertEqual(solve([4, 3, 2, 1, 3, 4]), "Yes")

    def test_c(self):
        self.assertEqual(solve([1, 3, 2]), "No")

    if __name__ == "__main__":
        unittest.main()
