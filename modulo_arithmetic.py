import unittest


def modulo_addition():
    max_value = 1000
    m = 7
    for i in range(1, max_value):
        for j in range(1, max_value):
            if (i % m + j % m) % m != (i + j) % m:
                return False
    return True


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(modulo_addition(), True)


if __name__ == '__main__':
    unittest.main()
