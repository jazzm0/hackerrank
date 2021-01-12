import unittest


def lonelyinteger(a):
    saw = {}
    r = -1
    for i in a:
        saw[i] = saw.get(i, 0) + 1

    for k, v in saw.items():
        if v == 1:
            return k

    return r


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(lonelyinteger([1, 2, 3, 4, 3, 2, 1]), 4)


if __name__ == '__main__':
    unittest.main()
