import unittest


# https://www.hackerrank.com/challenges/beautiful-binary-string

def beautifulBinaryString(b):
    change_counter = 0
    b = list(b)
    for i in range(len(b) - 2):
        if b[i] == '0' and b[i + 1] == '1' and b[i + 2] == '0':
            change_counter += 1
            b[i + 2] = '1'
    return change_counter


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(beautifulBinaryString('0101010'), 2)


if __name__ == '__main__':
    unittest.main()
