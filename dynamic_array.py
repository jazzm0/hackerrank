import unittest


def dynamicArray(n, queries):
    a = list()
    arr = [[] for x in range(n)]
    last_answer = 0
    for q in queries:
        idx = (q[1] ^ last_answer) % n
        if q[0] == 1:
            arr[idx].append(q[2])
        elif q[0] == 2:
            last_answer = arr[idx][q[2] % len(arr[idx])]
            a.append(last_answer)
    return a


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(dynamicArray(2, [
            [1, 0, 5],
            [1, 1, 7],
            [1, 0, 3],
            [2, 1, 0],
            [2, 1, 1]]), [7, 3])


if __name__ == '__main__':
    unittest.main()
