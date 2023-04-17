import unittest


# https://www.hackerrank.com/challenges/priyanka-and-toys

def toys(w):
    w = sorted(w)
    container_count, index = 0, 0

    while index < len(w):
        max_weight = w[index] + 4
        for i in range(index, len(w)):
            if w[i] > max_weight:
                break
            index += 1
        container_count += 1

    return container_count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(toys([1, 2, 3, 21, 7, 12, 14, 21]), 4)


if __name__ == '__main__':
    unittest.main()
