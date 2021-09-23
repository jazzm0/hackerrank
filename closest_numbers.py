import unittest


# https://www.hackerrank.com/challenges/gem-stones


def closestNumbers(arr):
    result = {}
    arr = sorted(arr)
    minkey = 10 ** 7
    for i in range(len(arr) - 1):
        key = arr[i + 1] - arr[i]
        value = (arr[i], arr[i + 1])
        if key < minkey:
            minkey = key
        if key in result.keys():
            result[key].append(value)
        else:
            result[key] = [value]

    tuple_list = []
    for v in result[minkey]:
        tuple_list.append(v[0])
        tuple_list.append(v[1])
        print(v[0], end=' ')
        print(v[1], end=' ')

    return tuple_list


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(
            closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]),
            [-20, 30])

    def test_b(self):
        self.assertEqual(
            closestNumbers(
                [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]),
            [-520, -470, -20, 30])


if __name__ == '__main__':
    unittest.main()
